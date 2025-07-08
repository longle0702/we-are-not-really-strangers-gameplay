import pandas as pd
lv1 = pd.read_csv('1.csv')
wildcard = pd.read_csv('wildcard.csv')
lv2 = pd.read_csv('2.csv')
lv3 = pd.read_csv('3.csv')
lv1['Source'] = 'Level 1'
lv2['Source'] = 'Level 2'
lv3['Source'] = 'Level 3'
wildcard['Source'] = 'Wildcard'
lvwc = pd.concat([lv1, lv2, lv3, wildcard], ignore_index=True)
lvwc.to_csv('Full.csv', index=False)