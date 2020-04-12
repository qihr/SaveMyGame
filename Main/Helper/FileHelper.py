import os
import Config

def IsHaveLocalCSV():
    print('本地是否存在文件：', os.path.exists(Config.UserInfoPath))
    return os.path.exists(Config.UserInfoPath)