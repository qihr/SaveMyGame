import os
import threading

import Config
from shutil import copyfile
from sys import exit
import os
import shutil
import time

EnvironmentVar = {}
copyfilelock = threading.Lock()

def IsSamePath(pidpath,installname):
   replacepath = (pidpath.replace(os.path.join(Config.SteamInstallPath, 'common\\'), '', 1))
   dirlist = replacepath.split("\\")
   pidpath = dirlist[0]
   return (pidpath == installname)




def IsHaveLocalCSV():
    return os.path.exists(Config.UserInfoPath)


def CopyFileWithLock(gamelist):
    for info in gamelist:
        source = info.GamePath
        timestr = time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))
        target = os.path.join(Config.BackUpPath, info.InstallName, timestr)
        if os.path.exists(target):
            i = 1;
            while os.path.exists((target + '({0})').format(i)):
                i += 1
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
    str = ''
    for info in gamelist:
        str += info.GameName + ','
    print("备份完成：" + str)


def CopyFile(gamelist):
    copyfilelock.acquire()
    try:
        CopyFileWithLock (gamelist)
    finally:
        copyfilelock.release()



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
                pathstr = pathstr.replace(key, info.InstallName, 1);
            else:
                pathstr = pathstr.replace(key, EnvironmentVar[key], 1);
    return pathstr


def InitDir():
    if not os.path.exists(Config.BackUpPath):
        os.makedirs(Config.BackUpPath)

def Init():
    InitEnvironmentVar()
    InitDir()
