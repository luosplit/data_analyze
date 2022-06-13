import pandas as pd
from pandas import DataFrame
from regex import F


pd.set_option('display.unicode.east_asian_width', True)

# 创建原始数据

data = {
    '语文': {'甲': 110, '乙': 105, '丙': 109, '丁': 112},
    '数学': {'甲': 105, '乙': 88, '丙': 120, '丁': 115},
    '英语': {'甲': 99, '乙': 115, '丙': 130, '丁': 140},
}

df = DataFrame(data)

# 纵向添加数据
"""
1.直接给DataFrame赋值
2.用loc属性添加数据
3.在列中插入一列数据,利用insert
"""

#  横向添加数据
# 增加一行
df.loc['戊'] = [110, 102, 113]
# print(df)
# 增加多行
# 用字典表示

# 删除数学中包含88，语文小于110的行
# df.drop(index=df[df['数学'].isin([88])].index,axis=1,inplace=True)

# 修改列名，将数学改为数学上

# df.rename(columns={"数学":'数学上'}, inplace=True)

# print(df)

# 给甲同学的成绩每个加10
print(df)

# df.loc['甲'] = df.loc['甲'] + 10

# print(df)

# 查询语文大于105的行

# print(df[df['语文']> 105])

# 查询语文大于105，数学大于88的行

# print(df[(df['语文'] > 105) & (df['数学'] > 88)])

# 使用query简化代码
# print(df.query('语文>105'))

# 练习between方法

# print(df.query('105<语文<112'))

# print(df[df['语文'].between(105,112)])

# 按语文分数降序排列
# print(df.sort_values(by='语文',ascending=False))


df['数学排名'] = df['数学'].rank(method='max',ascending=False)

print(df)