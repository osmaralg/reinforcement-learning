# %%
#import sys
#sys.path.append('C:/Users/mahit/Documents/MSc/RWTH/3rd sem/EMEC_Project/reinforment-learning')

import pandas as pd
import numpy as np
#import random
# import time
#import datetime
import json
from articles.functions import init_state, load_model, health_state, create_scatter_plot, calculate_reward_action

reward = []
action= []
daily_KPI = []
days = 30
df = init_state()
df_total = pd.DataFrame()
model = load_model('articles/model_ann_3layer')
KPI_df = pd.DataFrame()

for day in range(days):

    df, daily_reward, daily_action = calculate_reward_action(model, df=df)
    df['Day'] = day
    reward.append(daily_reward)
    action.append(daily_action)
    daily_KPI = health_state(df=df)
    KPI_df = KPI_df.append(pd.DataFrame(daily_KPI).T)
    df_total = pd.concat([df_total, df], axis=0)
    print(day)

scatterplot_dict = create_scatter_plot(df_total, reward, action)

KPI_df.rename(columns = {0:'Cured Cases', 1:'Susceptible', 2:'Exposed', 3:'Infectious', 4:'Newly Infected' , 5:'Death Cases'}, inplace=True)
static_graph_df = KPI_df[['Susceptible', 'Infectious', 'Newly Infected','Death Cases']].copy(deep=True)
static_graph = static_graph_df.to_dict("list")
static_graph["Reward"] = reward
static_graph["Action"] = action

for key in static_graph:
    for value in range(len(static_graph[key])):
        static_graph[key][value] = int(static_graph[key][value]) if not np.isnan(static_graph[key][value]) else None

with open('static/data/dynamic_graphs_data.json', 'w', encoding='utf-8') as f:
    json.dump(scatterplot_dict, f, ensure_ascii=False, indent=4)
    f.close()

with open('static/data/static_graphs_data.json', 'w', encoding='utf-8') as j:
    json.dump(static_graph, j, ensure_ascii=False, indent=4)
    j.close()



    
# %%


# %%
