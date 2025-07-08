import pandas as pd

wildcard = pd.read_csv('wildcard.csv')
wildcard['Source'] = 'Wildcard'
levels = {
    '1.csv': 'Level 1',
    '2.csv': 'Level 2',
    '3.csv': 'Level 3'
}

for filename, label in levels.items():
    level_df = pd.read_csv(filename)
    level_df['Source'] = label
    combined = pd.concat([level_df, wildcard], ignore_index=True)
    output_filename = filename.replace('.csv', 'wc.csv')
    combined.to_csv(output_filename, index=False)