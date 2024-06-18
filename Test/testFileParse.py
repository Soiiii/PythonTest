import pandas as pd

path = '#filesystem/Report_Usage2.csv'
df = pd.read_csv(filepath_or_buffer=path, skiprows=0)

project_name = df['project_name'].tolist()
workbook_name = df['workbook_name'].tolist()
distinct_count_of_view = df['distinct_count_of_view'].tolist()
workbook_last_accessed_date = df['workbook_last_accessed_date'].tolist()
load_date = df['load_date'].tolist()

listA = []
for row in df.iterrows():
    listA.append(row)
print(listA)