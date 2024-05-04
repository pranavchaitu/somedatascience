import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    customer["referee_id"] = customer["referee_id"].fillna(0)
    res_df = customer[(customer['referee_id'] != 2)]
    return res_df[['name']]    

