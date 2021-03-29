# %%
import sys
sys.path.append('c:/users/mahit/appdata/local/packages/pythonsoftwarefoundation.python.3.8_qbz5n2kfra8p0/localcache/local-packages/python38/site-packages')
import tensorflow as tf
from articles.functions import *

reward = []
action=[]
days = 30 #to ensure local variable D is used - may not be needed
df = init_state()
df_total = pd.DataFrame()
model = load_model('articles/model_ann_3layer')

for day in range(days):

    df, daily_reward, daily_action = calculate_reward_action(model, tf, df=df)
    reward.append(daily_reward)
    action.append(daily_action)
    print(day)
    df_total = pd.concat([df_total, df], axis=0)

scatterplot_dict  = create_scatter_plot(df_total)

with open('static/data/dynamic_graphs_data.json', 'w', encoding='utf-8') as f:
    json.dump(scatterplot_dict, f, ensure_ascii=False, indent=4)
    f.close()

with open('static/data/dynamic_graphs_data.json', 'w', encoding='utf-8') as f:
    json.dump(scatterplot_dict, f, ensure_ascii=False, indent=4)
    f.close()

static_graph_df = KPI_df[['Active Cases', 'Susceptible', 'Death Cases']].copy(deep=True)
static_graph_df.drop(static_graph_df.head(1).index, inplace=True)
static_graph = static_graph_df.to_dict("list")


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
