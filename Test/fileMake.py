# import csv
#
# def read_portfolio(filename):
#     total_cost = 0
#     portfolio = []
#
#     with open('Data/report.py', 'w') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             nshares = int(row[1])
#             price = float(row[2])
#             total_cost += nshares * price
#         return total_cost

import csv
f = open('Data/prices.csv', 'r')
rows = csv.reader(f)
listA = []
for row in rows:
    print(row)
    listA.append(row)
print(listA)

d = open('Data/report.py', 'w')
for rowA in listA:
    rowA_str = ''.join(rowA)
    d.write(f'{rowA_str}\n')