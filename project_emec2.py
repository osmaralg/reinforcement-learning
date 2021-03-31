# %%
#import sys
#sys.path.append('C:/Users/mahit/Documents/MSc/RWTH/3rd sem/EMEC_Project/reinforment-learning')

import pandas as pd
import numpy as np
#import random
# import time
#import datetime
import json
import tensorflow as tf
from articles.functions import init_state, load_model, create_scatter_plot, calculate_reward_action

reward = []
action= []
days = 100
df = init_state()
df_total = pd.DataFrame()
model = load_model('articles/model_ann_3layer')

for day in range(days):


    df, daily_reward, daily_action = calculate_reward_action(tf, model, df=df)
    df['Day'] = day
    reward.append(daily_reward)
    action.append(daily_action)
    df_total = pd.concat([df_total, df], axis=0)
 

scatterplot_dict = create_scatter_plot(df_total, reward, action)

static_graph = {k: [] for k in ["Infectious","Newly Infected","Death Cases","Susceptible"]}

for key in scatterplot_dict:
    static_graph["Infectious"].append(scatterplot_dict[key]["total_infectious"]) 
    static_graph["Newly Infected"].append(scatterplot_dict[key]["total_newly_infected"])
    static_graph["Death Cases"].append(scatterplot_dict[key]["total_dead"])
    static_graph["Susceptible"].append(scatterplot_dict[key]["total_susceptible"])

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

