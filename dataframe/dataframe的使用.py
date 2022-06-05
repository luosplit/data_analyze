import pandas as pd
from pandas import DataFrame

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

# 增加多行
# 用字典表示

# 删除数学中包含88，语文小于110的行
df.drop(index=df[df['数学'].isin([88])].index[0], axis=0, inplace=True)
df.drop(index=df[df['语文'] < 110].index[0], inplace=True)
print(df)


