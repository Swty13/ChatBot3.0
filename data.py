import pandas as pd

df = pd.read_json("data.json")
df_reach = pd.read_json("reach.json")

def places(ids):
    for i in range(0, len(df['rajdata'])):
        for k, v in df['rajdata'][i].items():
            if k == 'name' and v == ids.lower():
               return  df['rajdata'][i]


def reach(ids):
    for i in range(0, len(df_reach['reach'])):
        for k, v in df_reach['reach'][i].items():
            if k == 'city_name' and v == ids.lower():
               return  df_reach['reach'][i]