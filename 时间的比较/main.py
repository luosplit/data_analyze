import pandas as pd


standard_file = pd.read_csv(r'D:\data_analyse\时间的比较\test_1.csv')
aim_file = pd.read_csv(r'D:\data_analyse\时间的比较\test_2.csv')


# 进行比较

data_list = standard_file.loc[standard_file['time'] == aim_file['time']]

print(data_list['name'])

# 相同的时间段可以直接进行比较 