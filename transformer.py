import pandas as pd

def dateTransformer(df, col_list):
    for col in col_list:
        new_s = pd.to_datetime(df[col])
        df[col+'_year'] = new_s.map(lambda x: x.year)
        df[col+'_month'] = new_s.map(lambda x: x.month)
        df[col+'_day'] = new_s.map(lambda x: x.day)
        df.drop(col, axis=1, inplace=True)
    return df

def naTransformer(df):
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col].fillna('Missing', inplace=True)
        else:
            df[col].fillna(df[col].mean(), inplace=True)
    return df
