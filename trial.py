import pandas as pd

data = pd.read_csv('tennis.csv')
column_value = data.columns.tolist()
print(data[column_value[1]].unique())
#trial something...
