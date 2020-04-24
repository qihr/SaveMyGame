import os
import Config
from shutil import copyfile
from sys import exit
import os
import shutil

EnvironmentVar = {}

def IsHaveLocalCSV():
    print('本地是否存在文件：', os.path.exists(Config.UserInfoPath))
    return os.path.exists(Config.UserInfoPath)


def CopyFile(gamelist):
    for gameinfo in gamelist:
        source = gameinfo.GamePath
        target = "E:/CodeProject/SaveMyGame/GameBackUp"

        #assert not os.path.isabs(source)
        #target = os.path.join(target, os.path.dirname(source))

        #os.makedirs(target)

        try:
            shutil.copytree(source, target)
        except IOError as e:
            print("Unable to copy file. %s" % e)
        except:
            print("Unexpected error:")


def InitEnvironmentVar():
    EnvironmentVar['%InstallName%'] = ""
    EnvironmentVar['%SteamAppPath%'] =os.path.join(Config.SteamInstallPath, 'common');
    EnvironmentVar['%appdata%'] = os.environ['appdata'];
    os.environ['SteamAppPath'] = Config.SteamInstallPath


def ReplaceEnvironment(info):
    pathstr = info.GamePath
    for key in EnvironmentVar:
        if key in pathstr:
            if key == '%InstallName%':
                print("游戏安装目录：" + info.InstallName + "" + key)
                pathstr = pathstr.replace(key, info.InstallName, 1);
            else:
                pathstr = pathstr.replace(key, EnvironmentVar[key], 1);
            print("匹配成功：" + pathstr)
    return pathstr


def Init():
    InitEnvironmentVar()

# print(os.environ['appdata'])
# print(os.environ['SteamAppPath'])









