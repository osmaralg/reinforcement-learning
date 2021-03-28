# %%
import sys
sys.path.append('c:/users/mahit/appdata/local/packages/pythonsoftwarefoundation.python.3.8_qbz5n2kfra8p0/localcache/local-packages/python38/site-packages')
import pandas as pd
import numpy as np
import random
# import time
import datetime
import json
from articles.functions import create_scatter_plot, calculate_reward_action, simulate

# %%

# Inputs
s = 50  # size of the grid
N = 100  # size of population
M = round(N * 0.07)  # Number of infectious population
Et = 2  # Number of days staying exposed
It = 21  # Number of days staying infectious
Mt = 2  # Number of daily movements
D = 30  # Number of days
death_rate = 100
expose_rate = 3

# %%

# Initialization
S = N - M  # Susceptible population
E = 0  # Exposed population
I = M  # Number of infectious population
R = 0  # Recovered population
P = S + E + I + R  # Total population
Economy = 0  # Daily economic transaction
Cum_Economy = 0  # Total economic transaction

# %%

dummy_array = np.zeros(shape=(P, 9))
df = pd.DataFrame(dummy_array,
                  columns=['x', 'y', 'Day', 'Susceptible', 'Exposed', 'Infectious', 'Recovered', 'GG', 'Status'])

df = df.astype(
    {'x': int, 'y': int, 'Day': int, 'Susceptible': bool, 'Exposed': int, 'Infectious': int, 'Recovered': bool,
     'GG': bool, 'Status': str})
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

# %%

KPI_df = pd.DataFrame(
    columns=['Active Cases', 'Newly Infected', 'Cured Cases', 'Death Cases', 'Reproduction Rate', 'Economy',
             'Current Movement Restriction'])
initial = []
initial.insert(0, {'Active Cases': I,
                   'Newly Infected': df.loc[df['Infectious'] == 1].Infectious.count(),
                   'Cured Cases': 0,
                   'Death Cases': 0,
                   'Reproduction Rate': df.loc[df['Infectious'] == 1].Infectious.count(),
                   # 'Reproduction Rate':  df[df.assign(key=df.Infectious == 1).groupby(['Infectious']).key.transform('any')].Infectious.sum(),
                   'Economy': Economy,
                   'Current Movement Restriction': 0
                   })
KPI_df = pd.concat([pd.DataFrame(initial), KPI_df])
# %%
df_total = pd.DataFrame()
df_day = pd.DataFrame()
df_infectious = df.loc[(df['Infectious'] > 0)]
df_infectious = df_infectious[['x', 'y']]


# %%

for day in range(D):

    #start = datetime.datetime.now()
    Economy = 0  # Economy per day
    for mt in range(Mt):

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

                df.at[index, 'Day'] = day + 1  # updating the day counter

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
                        df.at[
                            index, 'Infectious'] = 1  # Increase the infectious day counter, now the person is infectious
                        df_infectious.append(person)
                    elif mt + 1 == Mt:
                        df.at[index, 'Exposed'] = person['Exposed'] + 1  # Increase the exposed day counter

                elif person['Susceptible']:  # If the person is in susceptible state

                    x_temp = int(person['x'])
                    df_xtemp = df_infectious[['x']].to_numpy()

                    if (x_temp in df_xtemp)or ((x_temp - 1) in df_xtemp) or ((x_temp + 1) in df_xtemp):

                        y_temp = int(person['y'])
                        df_ytemp = df_infectious[['y']].to_numpy()
                        if (y_temp in df_ytemp) or ((y_temp - 1) in df_ytemp) or ((y_temp + 1) in df_ytemp):
                            if random.choice(range(0, expose_rate)) > (expose_rate - 2):
                                df.at[index, 'Exposed'] = 1
                                df.at[index, 'Susceptible'] = False

                Cum_Economy = Cum_Economy + round(random.uniform(0.8, 1), 2)
                Economy = Economy + round(random.uniform(0.8, 1), 2)

    df_day = df.copy(deep=True)
    #  end = datetime.datetime.now()
    #  print("day: ", day, " took this time", end - start)
    # Gathering the data
    KPI_df.loc[day + 1, 'Active Cases'] = df.loc[df['Infectious'] > 0].Infectious.count()
    KPI_df.loc[day + 1, 'Newly Infected'] = df.loc[df['Infectious'] == 1].Infectious.count()
    KPI_df.loc[day + 1, 'Cured Cases'] = df.loc[df['Recovered'] == True].Recovered.count()
    KPI_df.loc[day + 1, 'Death Cases'] = df.loc[df['GG'] == True].GG.count()
    KPI_df.loc[day + 1, 'Susceptible'] = df.loc[df['Susceptible'] == True].Susceptible.count()
    KPI_df.loc[day + 1, 'Reproduction Rate'] = df.loc[df['Infectious'] == 1].Infectious.count()
    KPI_df.loc[day + 1, 'Economy'] = Economy
    KPI_df.loc[day + 1, 'Current Movement Restriction'] = 0

    df_total = pd.concat([df_total, df_day], axis=0)


scatterplot_dict  = create_scatter_plot(df_total)

with open('static/data/dynamic_graphs_data.json', 'w', encoding='utf-8') as f:
    json.dump(scatterplot_dict, f, ensure_ascii=False, indent=4)
    f.close()

static_graph_df = KPI_df[['Active Cases', 'Susceptible', 'Death Cases']].copy(deep=True)
static_graph_df.drop(static_graph_df.head(1).index, inplace=True)
static_graph = static_graph_df.to_dict("list")


reward = []
action=[]
days = D #to ensure local variable D is used - may not be needed
for day in range(days):
    daily_reward, daily_action = calculate_reward_action()
    #daily_reward, daily_action = simulate("calc")
    reward.append(daily_reward)
    action.append(daily_action)
    print(day)

static_graph["Reward"] = reward
static_graph["Action"] = action    

for key in static_graph:
    for value in range(len(static_graph[key])):
        static_graph[key][value] = int(static_graph[key][value]) if not np.isnan(static_graph[key][value]) else None

with open('static/data/static_graphs_data.json', 'w', encoding='utf-8') as j:
    json.dump(static_graph, j, ensure_ascii=False, indent=4)
    j.close()




    
# %%


# %%
