import pandas as pd


# data = {
#     'num': [11111111111111111119, 22222222222229],  # 11111111111111100000
#     'name': ['alex', 'bob']
# }

# df = pd.DataFrame(data=data)

# df.to_csv('test.csv',index=False)


df = pd.read_csv(r'D:\data_analyse\data.txt',sep='\t')

print(df)