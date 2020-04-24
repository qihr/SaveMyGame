import os
import Config
from shutil import copyfile
from sys import exit
import os
import shutil
import time

EnvironmentVar = {}

def IsHaveLocalCSV():
    print('本地是否存在文件：', os.path.exists(Config.UserInfoPath))
    return os.path.exists(Config.UserInfoPath)


def CopyFile(gamelist):
    for info in gamelist:
        source = info.GamePath
        timestr = time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))
        target = os.path.join(Config.BackUpPath, info.InstallName, timestr)
        print('路径', target)
        if os.path.exists(target):
            i = 1;
            while os.path.exists((target + '({0})').format(i)):
                print('路径', target)
                i+=1
            target = (target + '({0})').format(i)

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


def InitDir():
    if not os.path.exists(Config.BackUpPath):
        os.makedirs(Config.BackUpPath)



def Init():
    InitEnvironmentVar()
    InitDir()

# print(os.environ['appdata'])
# print(os.environ['SteamAppPath'])









