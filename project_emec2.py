# %%

import pandas as pd
import numpy as np
import random
import time
import datetime

# %%

# Inputs
s = 250  # size of the grid
N = 10000  # size of population
M = round(N * .007)  # Number of infectious population
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

# %%

KPIs = ['Active Cases', 'Newly Infected', 'Cured Cases', 'Death Cases', 'Reproduction Rate', 'Economy',
        'Current Movement Restriction']
KPI_df = pd.DataFrame(columns=KPIs)
KPI_df = KPI_df.fillna(0)
KPI_df.loc[0, 'Active Cases'] = I
KPI_df.loc[0, 'Newly Infected'] = df.loc[df['Infectious'] == 1].Infectious.count()
KPI_df.loc[0, 'Cured Cases'] = 0
KPI_df.loc[0, 'Death Cases'] = 0
KPI_df.loc[0, 'Reproduction Rate'] = df.loc[df['Infectious'] == 1].Infectious.count()
KPI_df.loc[0, 'Economy'] = Economy
KPI_df.loc[0, 'Current Movement Restriction'] = 0

# %%

print("done")
df_infectious = df.loc[(df['Infectious'] > 0)]
df_infectious = df_infectious[['x', 'y']]
# %%

print("example")
# ['x','y','Day','Susceptible','Exposed','Infectious','Recovered','GG']
# ['x','y','Day','Susceptible','Exposed','Infectious','Recovered','GG']
for day in range(D):
    print("day", day)
    Economy = 0  # Economy per day
    for mt in range(Mt):
        print("movement", mt)
        start = datetime.datetime.now()

        for index, person in df.iterrows():

            if not person['GG']:  # If the person is not dead

                new_move_x = random.choice(range(-1, 2))
                new_move_y = random.choice(range(-1, 2))

                person['x'] = max(min(person['x'] + new_move_x, S), 0)
                person['y'] = max(min(person['y'] + new_move_y, S), 0)

                df.iat[index, 0] = person['x']
                df.iat[index, 1] = person['y']

                if index in df_infectious.index:
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

                    #df_infectious = np.asarray([df_infectious['x'], df_infectious['y']]).T

                    df_x = df_infectious.loc[
                        (df_infectious['x'] == person['x']) |
                        (df_infectious['x'] == person['x'] - 1) |
                        (df_infectious['x'] == person['x'] + 1)
                        ]
                    if not df_x.empty:
                        df_y = df_x.loc[
                            (df_infectious['y'] == person['y']) |
                            (df_infectious['y'] == person['y'] - 1) |
                            (df_infectious['y'] == person['y'] + 1)
                            ]
                        if not df_y.empty:

                            if random.choice(range(0, expose_rate)) > (expose_rate - 2):
                                df.at[index, 'Exposed'] = 1
                                df.at[index, 'Susceptible'] = False

                if person['Infectious'] == 0:
                    Cum_Economy = Cum_Economy + round(random.uniform(0.8, 1), 2)
                    Economy = Economy + round(random.uniform(0.8, 1), 2)

    end = datetime.datetime.now()
    print("took this time", end - start)

    # Gathering the data
    KPI_df.loc[day + 1, 'Active Cases'] = df.loc[df['Infectious'] > 0].Infectious.count()
    KPI_df.loc[day + 1, 'Newly Infected'] = df.loc[df['Infectious'] == 1].Infectious.count()
    KPI_df.loc[day + 1, 'Cured Cases'] = df.loc[df['Recovered'] == True].Recovered.count()
    KPI_df.loc[day + 1, 'Death Cases'] = df.loc[df['GG'] == True].GG.count()
    KPI_df.loc[day + 1, 'Reproduction Rate'] = df.loc[df['Infectious'] == 1].Infectious.count()
    KPI_df.loc[day + 1, 'Economy'] = Economy
    KPI_df.loc[day + 1, 'Current Movement Restriction'] = 0

# %%

df

# %%
