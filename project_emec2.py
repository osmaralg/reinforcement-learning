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
days = 30
df = init_state()
df_total = pd.DataFrame()
model = load_model('articles/model_ann_3layer')

for day in range(days):

    df, daily_reward, daily_action = calculate_reward_action(model, df=df)
    df['Day'] = day
    reward.append(daily_reward)
    action.append(daily_action)
    df_total = pd.concat([df_total, df], axis=0)
    print(day)

scatterplot_dict = create_scatter_plot(df_total, reward, action)
total_inf=[]
total_sus=[]
total_dead=[]
total_newinf=[]
for key in scatterplot_dict:
    inf = scatterplot_dict[key]["total_infectious"]
    total_inf.append(inf)
    sus = scatterplot_dict[key]["total_susceptible"]
    total_sus.append(sus)
    dead = scatterplot_dict[key]["total_dead"]
    total_dead.append(dead)
    newinf = scatterplot_dict[key]["total_newly_infected"]
    total_newinf.append(newinf)
    
static_graph = {}
static_graph["Reward"] = reward
static_graph["Action"] = action   
static_graph["Infectious"] = total_inf 
static_graph["Susceptible"] = total_sus
static_graph["Death Cases"] = total_dead
static_graph["Newly Infected"] = total_newinf

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
