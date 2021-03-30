# -*- coding: utf-8 -*-
"""project_EMEC.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11KiW2eJptlMiX4M6ZeyAJocT0RRBSsUS
"""

# %%

import numpy as np
#import sys
#sys.path.append('c:/users/mahit/appdata/local/packages/pythonsoftwarefoundation.python.3.8_qbz5n2kfra8p0/localcache/local-packages/python38/site-packages')

import pandas as pd
import random
import json

# %%

# Load the model

# %%


economy = 0  # Daily economic transaction

# Inputs
s = 50  # size of the grid
N = 1000  # size of population
M = round(N * 0.007)  # Number of infectious population
Et = 1  # Number of days staying exposed (Incubation rate)
It = 21  # Number of days staying infectious
Mt = 5  # Number of daily movements
D = 200  # Number of days
death_rate = 100
expose_rate = 5 # transmission rate

# Initialization
S = N - M  # Susceptible population
E = 0  # Exposed population
I = M  # Number of infectious population
R = 0  # Recovered population
P = S + E + I + R  # Total population

# %%

# Create a virtual environment actions
def init_state():  # init

    global P, M, It, s
    dummy_array = np.zeros(shape=(P, 8))
    df = pd.DataFrame(dummy_array, columns=['x', 'y', 'Day', 'Susceptible', 'Exposed', 'Infectious', 'Recovered', 'GG'])
    df = df.astype(
        {'x': int, 'y': int, 'Day': int, 'Susceptible': bool, 'Exposed': int, 'Infectious': int, 'Recovered': bool,
         'GG': bool})
    df['Susceptible'] = True
    # Appending infectious population in
    dfupdate = df.sample(M)
    dfupdate['Infectious'] = np.random.randint(1, It, size=len(dfupdate))
    dfupdate['Susceptible'] = False
    df.update(dfupdate)
    update_list = dfupdate.index.tolist()
    # Dispersing people randomly among grid
    df['x'] = np.random.randint(0, s, size=len(df))
    df['y'] = np.random.randint(0, s, size=len(df))

    return df


def load_model(path):
    from tensorflow import keras
    return keras.models.load_model(path)

def one_day(df, action=0):
    # start_time = time.time()
    global P, M, It, S, death_rate, expose_rate
    policy_match = {0: 1, 1: 0.75, 2: 0.25}  # assign action to policy
    moves_under_policy = int(round(Mt * policy_match[action], 0))

    df_infectious = df.loc[(df['Infectious'] > 0)]
    df_infectious = df_infectious[['x', 'y']]

    for mt in range(moves_under_policy):
        for index, person in df.iterrows():

            if not person['GG']:  # If the person is not dead

                new_move_x = random.choice(range(-1, 2))
                new_move_y = random.choice(range(-1, 2))

                person['x'] = max(min(person['x'] + new_move_x, s), 0)
                person['y'] = max(min(person['y'] + new_move_y, s), 0)

                df.iat[index, 0] = int(person['x'])
                df.iat[index, 1] = int(person['y'])

                if index in df_infectious.index:  # assigning whats in person (row) to df_infectious at the correct index
                    df_infectious.at[index, 'x'] = person['x']
                    df_infectious.at[index, 'y'] = person['y']

                if (person['Infectious'] > 0) and (person['Recovered'] == False):  # If a person is in infectious state
                    if person['Infectious'] - random.choice(range(0, 7)) >= It:  # If the infectious days are completed
                        if random.choice(range(0, death_rate)) > (
                                death_rate - 2):  # If the person dies(with probability distribution 1:4)
                            df.at[index, 'Infectious'] = 0
                            if index in df_infectious.index:
                                df_infectious.drop([index])

                            df.at[index, 'GG'] = True  # Kill the person
                        else:  # If the person survives
                            df.at[index, 'Infectious'] = 0
                            if index in df_infectious.index:
                                df_infectious.drop([index])
                            df.at[index, 'Recovered'] = True  # Recover the person
                    elif mt + 1 == Mt:
                        df.at[index, 'Infectious'] = person['Infectious'] + 1  # Increase the infectious day counter
                elif (person['Exposed'] > 0) and (person['Infectious'] == 0):  # If a person is in exposed state
                    if (person['Exposed'] - random.choice(
                            range(0, 2))) >= Et:  # If the person has reached the exposed day limit?  7
                        df.at[index, 'Exposed'] = 0
                        df.at[index, 'Infectious'] = 1  # Increase the infectious day counter, now the person is infectious
                        df_infectious.append(person)
                    elif mt + 1 == Mt:
                        df.at[index, 'Exposed'] = person['Exposed'] + 1  # Increase the exposed day counter

                elif person['Susceptible']:  # If the person is in susceptible state

                    x_temp = int(person['x'])
                    df_xtemp = df_infectious[['x']].to_numpy()

                    if (x_temp in df_xtemp) or ((x_temp - 1) in df_xtemp) or ((x_temp + 1) in df_xtemp):

                        y_temp = int(person['y'])
                        df_ytemp = df_infectious[['y']].to_numpy()
                        if (y_temp in df_ytemp) or ((y_temp - 1) in df_ytemp) or ((y_temp + 1) in df_ytemp):
                            if random.choice(range(0, expose_rate)) > (expose_rate - 2):
                                df.at[index, 'Exposed'] = 1
                                df.at[index, 'Susceptible'] = False
    # print("--- %s seconds ---" % (time.time() - start_time))

    return df  # time.time() - start_time #


def economy_gain(df):
    economy_gain = len(df[(df.GG == False) & (df.Infectious == 0)]) * round(random.uniform(0.8, 1), 2)
    return economy_gain

def current_state(df):
    inf = len(df.loc[df['Infectious'] > 0])
    exposed = len(df.loc[df['Exposed'] > 0])
    recovered = len(df.loc[df['Recovered'] == True])
    sus = len(df.loc[df['Susceptible'] == True])
    gg = df.loc[df['GG'] == True].GG.count()
    print(inf)
    return np.array([recovered, sus, exposed, inf, gg])


# %%


def create_scatter_plot(df_total, reward, action):
    status = ["healthy", "dead", "infectious", "susceptible"]
    df_total['Status'] = df_total.apply(
        lambda x: rule(x['Infectious'], x['Susceptible'], x['GG']), axis=1)
    daily_status = df_total[['x', 'y', 'Day', 'Status']].copy(
        deep=True).reset_index()
    daily_status["Position"] = list(zip(daily_status['x'], daily_status['y']))
    daily_status.rename(columns={"index": "Person"}, inplace=True)
    complete_status = []
    for i, x in daily_status.to_dict('index').items():
        complete_status.append(x)
        for stat in status:
            if stat not in daily_status.at[i, "Status"]:
                complete_status.append({"Position": None, "Status": stat, "Day": daily_status.at[i, "Day"],
                                        "Person": daily_status.at[i, "Person"]})
    complete_status_df = pd.DataFrame(complete_status)
    complete_status_df.Position = complete_status_df.Position.apply(lambda x: list(x) if type(x) == tuple else x)
    complete_status_df.sort_values(['Day', 'Person'], ascending=[True, True], inplace=True)
    # complete_status_df.to_excel('output1.xlsx')
    # limited_status = complete_status_df.drop(complete_status_df[(complete_status_df['Status'] == "healthy") | (complete_status_df['Status'] == "dead")].index)

    scatterplot = complete_status_df.groupby(['Day', 'Status'], as_index=False)['Position'].apply(list).to_frame()
    scatterplot_dict = {level: scatterplot.xs(level).to_dict('index') for level in scatterplot.index.levels[0]}
    # for every day and every person and every status we need an entry
    for key in scatterplot_dict:
        scatterplot_dict[key]["susceptible"] = scatterplot_dict[key]["susceptible"][0]
        scatterplot_dict[key]["infectious"] = scatterplot_dict[key]["infectious"][0]
        scatterplot_dict[key]["total_susceptible"] = (
            sum(x is not None for x in scatterplot_dict[key]["susceptible"]))
        scatterplot_dict[key]["reward"] = int(reward[key])
        scatterplot_dict[key]["action"] = int(action[key])
        scatterplot_dict[key]["total_dead"] = (
            sum(x is not None for x in scatterplot_dict[key]["dead"][0]))
        scatterplot_dict[key]["total_infectious"] = (
            sum(x is not None for x in scatterplot_dict[key]["infectious"]))
        scatterplot_dict[key]["total_healthy"] = (
            sum(x is not None for x in scatterplot_dict[key]["healthy"][0]))
        del [scatterplot_dict[key]["healthy"]]
        del [scatterplot_dict[key]["dead"]]

    return scatterplot_dict


def rule(infections, susceptible, dead):
    if infections > 0 and not susceptible and not dead:
        return "infectious"
    elif susceptible and not dead:
        return "susceptible"
    elif infections == 0 and not susceptible and not dead:
        return "healthy"
    elif dead:
        return "dead"
    else:
        return np.nan


def simulate(model, df=init_state(), current_day=0):
    # Use the agent to make decisions
    # calculate reward and action
    import tensorflow as tf
    #  model = load_model("model_ann_3layer")
    economy = 0
    state = current_state(df)
    state = tf.reshape(state, [1, 5])
    prediction = model.predict(state, steps=1)
    action_by_agent = np.argmax(prediction)
    df = one_day(df, action=action_by_agent)
    gain = economy_gain(df)
    economy += gain
    return df, gain, action_by_agent

def calculate_reward_action(df=init_state()):
    # calculate reward and action
    import tensorflow as tf
    model = load_model("model_ann_3layer")
    economy = 0
    state = current_state(df)
    state = tf.reshape(state, [1, 5])
    prediction = model.predict(state, steps=1)
    action_by_agent = np.argmax(prediction)
    df = one_day(df, action=action_by_agent)
    gain = economy_gain(df)
    economy += gain
    return df, gain, action_by_agent

"""
alternatively function simulate can be changed as below:
( another parameter has to be added
 the line that calls the function will have to be changed everywhere
 i have left it as a comment where i also call the function in project_emec2.py line 183)

def simulate(df=reset(), current_day=0, usecase):
    # Use the agent to make decisions

    economy = 0
    model = load_model("model_ann_3layer")
    state = current_state(df)
    state = tf.reshape(state, [1, 5])
    prediction = model.predict(state, steps=1)
    action_by_agent = np.argmax(prediction)
    df = one_day(df, action=action_by_agent)
    gain = economy_gain(df)
    economy += gain
    #print(f"Day {current_day + 1}: take action {action_by_agent}, total_reward: {economy}. {prediction}")
    plot_dict = create_scatter_plot(df)
    if usecase == "plot":
        return plot_dict
    if usecase == "calc":
        return gain, action_by_agent

"""

if __name__ == "__main__":

    df = simulate()
    colors = []
    result = []
    df_dict = df.to_dict('index')

    for key in df_dict:
        result.append(df_dict[key])
        if df_dict[key]['Infectious']:
            colors.append('red')
        else:
            colors.append('black')
