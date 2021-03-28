# %%

import pandas as pd
import numpy as np
import random
#import time
import datetime
import json

# %%

# Inputs
s = 250  # size of the grid
N = 100  # size of population
M = round(N * .07)  # Number of infectious population
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
df = pd.DataFrame(dummy_array, columns=['x', 'y', 'Day', 'Susceptible', 'Exposed', 'Infectious', 'Recovered', 'GG','Status'])

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

KPI_df = pd.DataFrame(columns = ['Active Cases', 'Newly Infected', 'Cured Cases', 'Death Cases', 'Reproduction Rate', 'Economy',
        'Current Movement Restriction'])
initial = []
initial.insert(0, {'Active Cases': I, 
                 'Newly Infected': df.loc[df['Infectious'] == 1].Infectious.count(),
                 'Cured Cases': 0,
                 'Death Cases': 0,
                 'Reproduction Rate':  df.loc[df['Infectious'] == 1].Infectious.count(),
                 #'Reproduction Rate':  df[df.assign(key=df.Infectious == 1).groupby(['Infectious']).key.transform('any')].Infectious.sum(),
                 'Economy': Economy,
                 'Current Movement Restriction':0                 
                 })
KPI_df = pd.concat([pd.DataFrame(initial), KPI_df])
# %%
df_total = pd.DataFrame()
df_day = pd.DataFrame()
df_infectious = df.loc[(df['Infectious'] > 0)]
df_infectious = df_infectious[['x', 'y']]


def rule(infections,susceptible,dead):
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

                if index in df_infectious.index: #assigning whats in person (row) to df_infectious at the correct index
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
                        df.at[index, 'Infectious'] = 1  # Increase the infectious day counter, now the person is infectious
                        df_infectious.append(person)
                    elif mt + 1 == Mt:
                        df.at[index, 'Exposed'] = person['Exposed'] + 1  # Increase the exposed day counter

                elif person['Susceptible']:  # If the person is in susceptible state

                    x_temp = int(person['x'])
                    df_xtemp = df_infectious[['x']].to_numpy()
                
                    if (x_temp in df_xtemp) or ((x_temp- 1) in df_xtemp) or ((x_temp+ 1) in df_xtemp):
                        y_temp = int(person['y'])
                        df_ytemp = df_infectious[['y']].to_numpy()
                        if (y_temp in df_ytemp) or ((y_temp - 1) in df_ytemp) or ((y_temp + 1) in df_ytemp):
                            if random.choice(range(0, expose_rate)) > (expose_rate - 2):
                                df.at[index, 'Exposed'] = 1
                                df.at[index, 'Susceptible'] = False
                    
                                
                Cum_Economy = Cum_Economy + round(random.uniform(0.8, 1), 2)
                Economy = Economy + round(random.uniform(0.8, 1), 2)
    df_day = df.copy(deep=True)
    #end = datetime.datetime.now()
    #print("day: ", day, " took this time", end - start)
    # Gathering the data
    KPI_df.loc[day + 1, 'Active Cases'] = df.loc[df['Infectious'] > 0].Infectious.count()
    KPI_df.loc[day + 1, 'Newly Infected'] = df.loc[df['Infectious'] == 1].Infectious.count()
    KPI_df.loc[day + 1, 'Cured Cases'] = df.loc[df['Recovered'] == True].Recovered.count()
    KPI_df.loc[day + 1, 'Death Cases'] = df.loc[df['GG'] == True].GG.count()
    KPI_df.loc[day + 1, 'Susceptible'] = df.loc[df['Susceptible'] == True].Susceptible.count()
    KPI_df.loc[day + 1, 'Reproduction Rate'] = df.loc[df['Infectious'] == 1].Infectious.count()
    KPI_df.loc[day + 1, 'Economy'] = Economy
    KPI_df.loc[day + 1, 'Current Movement Restriction'] = 0
    
    df_total= pd.concat([df_total, df_day], axis=0)
    
status = ["healthy","dead","infectious","susceptible"]
df_total['Status'] = df_total.apply(lambda x: rule(x['Infectious'], x['Susceptible'], x['GG']), axis =  1)
daily_status = df_total[['x','y','Day','Status']].copy(deep=True).reset_index()
daily_status["Position"] = list(zip(daily_status['x'],daily_status['y']))
daily_status.rename(columns={"index":"Person"}, inplace=True)
   
complete_status = []
for i, x in daily_status.to_dict('index').items():
    complete_status.append(x) 
    for stat in status:
        if stat not in daily_status.at[i,"Status"]:
            complete_status.append({"Position": None, "Status": stat, "Day": daily_status.at[i,"Day"], "Person": daily_status.at[i,"Person"]})

complete_status_df = pd.DataFrame(complete_status)
complete_status_df.Position= complete_status_df.Position.apply(lambda x: list(x) if type(x)== tuple else x)
complete_status_df.sort_values(['Day', 'Person'], ascending=[True, True], inplace=True)
#complete_status_df.to_excel('output1.xlsx')
#limited_status = complete_status_df.drop(complete_status_df[(complete_status_df['Status'] == "healthy") | (complete_status_df['Status'] == "dead")].index)

scatterplot = complete_status_df.groupby(['Day','Status'],as_index=False)['Position'].apply(list).to_frame()
scatterplot_dict = {level: scatterplot.xs(level).to_dict('index') for level in scatterplot.index.levels[0]}
#for every day and every person and every status we need an entry
for key in scatterplot_dict: 
    scatterplot_dict[key]["susceptible"] = scatterplot_dict[key]["susceptible"][0] 
    scatterplot_dict[key]["infectious"] = scatterplot_dict[key]["infectious"][0] 
    scatterplot_dict[key]["total_susceptible"] = (sum(x is not None for x in scatterplot_dict[key]["susceptible"]))
    scatterplot_dict[key]["total_dead"] = (sum(x is not None for x in scatterplot_dict[key]["dead"][0]))
    scatterplot_dict[key]["total_infectious"] = (sum(x is not None for x in scatterplot_dict[key]["infectious"]))
    scatterplot_dict[key]["total_healthy"] = (sum(x is not None for x in scatterplot_dict[key]["healthy"][0]))
    del[scatterplot_dict[key]["healthy"]]
    del[scatterplot_dict[key]["dead"]]

    
with open('dynamic_graphs_data.json', 'w', encoding='utf-8') as f:
    json.dump(scatterplot_dict, f, ensure_ascii=False, indent=4)
    f.close()

KPI_df = KPI_df.replace(np.nan, 0)
static_graph_df = KPI_df[['Active Cases','Susceptible','Death Cases','Economy']].copy(deep=True)
static_graph = static_graph_df.to_dict("list")
for key in static_graph:
    for value in range(len(static_graph[key])):
        static_graph[key][value] = int(static_graph[key][value]) 

with open('static_graphs_data.json', 'w', encoding='utf-8') as j:
    json.dump(static_graph, j, ensure_ascii=False, indent=4)
    j.close()

# %%

"""df_x = df_infectious.loc[
                        (df_infectious['x'] == person['x']) |
                        (df_infectious['x'] == person['x'] - 1) |
                        (df_infectious['x'] == person['x'] + 1)
                        ] #TODO
                    if not df_x.empty:
                        df_y = df_x.loc[
                            (df_infectious['y'] == person['y']) |
                            (df_infectious['y'] == person['y'] - 1) |
                            (df_infectious['y'] == person['y'] + 1)
                            ]#comparison of all rows of x and y col to the 'person' series
                        if not df_y.empty:

                            if random.choice(range(0, expose_rate)) > (expose_rate - 2):
                                df.at[index, 'Exposed'] = 1
                                df.at[index, 'Susceptible'] = False"


df_temp = scatterplot.groupby('Day')[['Status']].apply(lambda x: x.set_index('Position').to_dict()).to_dict()
df_temp=scatterplot.groupby(['Day','Status'],as_index=False)['Position'].apply(lambda x : x.values.tolist()[0]).to_frame()

line = pd.DataFrame()
#len_daily_status = len(daily_status)
for stat in status:
    start = datetime.datetime.now()
    #begin = len(daily_status) - len_daily_status
    for index in range(len(daily_status)):        
        if stat not in daily_status.at[index,"Status"]:
            line = pd.DataFrame({"Position": None, "Status": stat, "Day": daily_status.at[index,"Day"], "index": daily_status.at[index,"index"]}, index=[index])
            #daily_status = pd.concat([daily_status.iloc[:index-1], line, daily_status.iloc[index-1:]]).reset_index(drop=True)
            
    end = datetime.datetime.now()
    print("index: ", index, " took this time", end - start)    
                #sort by day first and then by index

"""

# %%
