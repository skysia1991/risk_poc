import pandas as pd


def dateTransformer(df, col_list):
    for col in col_list:
        new_s = pd.to_datetime(df[col], errors='coerce')
        df[col+'_year'] = new_s.map(lambda x: x.year, na_action='ignore')
        df[col+'_month'] = new_s.map(lambda x: x.month, na_action='ignore')
        df[col+'_day'] = new_s.map(lambda x: x.day, na_action='ignore')
        df.drop(col, axis=1, inplace=True)
    return naTransformer(df)

def naTransformer(df):
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col].fillna('0', inplace=True)
        else:
            df[col].fillna(df[col].mean(), inplace=True)
    return df
