"""
测试isin中index的作用

"""

import pandas as pd
from pandas import DataFrame

# 对齐
pd.set_option('display.unicode.east_asian_width', True)

data = {
    '语文': {'甲': 110, '乙': 105, '丙': 109, '丁': 112},
    '数学': {'甲': 105, '乙': 88, '丙': 90, '丁': 115},
    '英语': {'甲': 99, '乙': 115, '丙': 130, '丁': 140},
}

df = DataFrame(data)
print(df)
# 删除数学中包含88的行
data = df[df['数学'].isin([88])].index.tolist()

df.drop(index=df[df['数学'].isin([88])].index.tolist(), axis=0, inplace=True)



