import pandas as pd
lvwc = pd.read_csv('lvwc.csv')
sample = lvwc.sample(n=1)
for _, row in sample.iterrows():
    print(f"{row['Source']}: {row['Questions']}")