import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    res = customers.drop_duplicates(subset=['email'],keep='first')
    return res