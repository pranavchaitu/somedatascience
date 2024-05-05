.feedkeys".run(1)
import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    res_df = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    return res_df[['name','population','area']]

# -- Write your PostgreSQL query statement below
# SELECT "name", "population", "area" from World 
# WHERE "area" >= 3000000 OR "population" >= 25000000
