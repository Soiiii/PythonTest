def read_data(filename):
    records = []
    with open(filename) as f:
        for line in f:

            records.append(r)
    return records

d = read_data('file.csv')


def read_data(lines):
    records = []
    for line in lines:
        records.append(r)
    return records

with open('file.csv') as f:
    d = read_data(f)