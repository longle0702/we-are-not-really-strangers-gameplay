import pandas as pd
lv1 = pd.read_csv('questions/1.csv')
lv2 = pd.read_csv('questions/2.csv')
lv3 = pd.read_csv('questions/3.csv')
wildcard = pd.read_csv('questions/wildcard.csv')

dfs = [lv1, lv2, lv3, wildcard]
filenames = ['1.csv', '2.csv', '3.csv', 'wildcard.csv']

for df, filename in zip(dfs, filenames):
    df.reset_index(drop=True, inplace=True)
    df.index = df.index + 1
    df.index.name = 'Index'
    if df.columns.size > 0:
        df.columns = ['Questions'] + list(df.columns[1:])
    df.to_csv(filename, index=True)