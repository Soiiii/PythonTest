import os

os.getcwd()

# file = open('Data/portfolio.csv', 'rt')
# header = next(file)
# print(header)

records = []
listA = []
with open('Data/portfolio.csv', 'rt') as f:
    # data = file.read()
    next(f)
    for i in f:
        aa = i.split(',')
        listA.append((aa[0], aa[1], aa[2]))
    print(listA)
    # next(f) # 헤더를 건너뜀
    # for line in f:
    #     row = line.split(',')
    #     records.append((row[0], int(row[1]), float(row[2])))
    # print(records)