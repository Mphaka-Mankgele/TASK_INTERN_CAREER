import pandas as pd

# sep = ','

# file = open("customers-100.csv", "r")

# header = file.readline().strip().split(sep)
# data = []

# for l, line in enumerate(file):
#     values = line.strip().split(sep)
#     data.append(dict(zip(header, values)))

# df = pd.DataFrame(data).reset_index(drop=True)
# print(df)

df = pd.read_csv('machine-readable-business-employment-data-sep-2023-quarter.csv')
print(df)