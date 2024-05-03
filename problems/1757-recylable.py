import pandas as pd
def find_products(products: pd.DataFrame) -> pd.DataFrame:
    res_df = products[(products['low_fats'] == 'Y') && (products['product_id'] == 'Y')
    return [["product_id"]]
