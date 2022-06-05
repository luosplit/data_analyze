"""练习如何在csv文件中批量更改时间格式"""

import pandas as pd
import datetime
from pandas import DataFrame



def switch_csv_function():
    xlsx_file = pd.read_excel('./data.xlsx')
    xlsx_file.to_csv('data_1.csv', index=None)


def time_parse_function():
    """对时间格式的处理"""
    # csv_file = pd.read_csv('./data_1.csv')
    # csv_file.日期 = pd.to_datetime(csv_file['日期'])
    # csv_file['日期'] = csv_file['日期'].dt.strftime('%Y/%m/%d %H:%M:%S.000')

    # csv_file.to_csv('result.csv')

    data = pd.read_csv('./data_1.csv',header=0)
    data.loc[:,'日期'] = pd.to_datetime(data.loc[:,'日期'],format='%Y-%m-%d %H:%M:%S.000')

    data.to_csv('result.csv')

    



if __name__ == "__main__":
    # switch_csv_function()
    time_parse_function()
