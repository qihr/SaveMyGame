import os


def IsHaveLocalCSV():
    print('本地是否存在文件：', os.path.exists('GameLocationInfo.csv'))
    return os.path.exists('GameLocationInfo.csv')