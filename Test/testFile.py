# import csv
#
# file_path = ''
#
# with open(file_path, mode='r', encoding='utf-8') as file:
#     csv_reader = csv.reader(file)
#     for row in csv_reader:
#         print(row)

import pandas as pd

file_path = ''

df = pd.read_csv(file_path)

print(df)