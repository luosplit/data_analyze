import os
import zipfile


#  zip解压
# f = zipfile.ZipFile('package.zip', 'r')
# for file in f.namelist():
#     f.extract(file, r'D:\数据分析练习\解压')
# f.close()

def file_parse_function():
    path = r'D:\数据分析练习\解压\package'
    file_list = os.listdir(path)
    for file in file_list:
        file_path = path + '\\' + file
        if os.path.isdir(file_path):  # 判断是否为文件夹
            second_file_list = os.listdir(file_path)
            # 第二层
            for second_file in second_file_list:
                second_file_path = file_path + '\\' + second_file
                # 第三层
                if os.path.isdir(second_file_path):
                    third_file_list = os.listdir(second_file_path)
                    for item in third_file_list:
                        item_path = second_file_path + '\\' + item
                        after_path = second_file_path + '\\' + file + '.txt'
                        os.rename(item_path, after_path)


if __name__ == '__main__':
    file_parse_function()
