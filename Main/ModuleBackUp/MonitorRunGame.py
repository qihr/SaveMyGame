import os
import time
import psutil
import Config
import DataProcess
import FileHelper

def GetRunningGame():
    pids = psutil.pids()
    list = []
    for pid in pids:
        try:
            p = psutil.Process(pid)
            if not Config.UseName == p.username():
                continue
            for info in DataProcess.GameInfoList:
                if FileHelper.IsSamePath(p.exe(), info.InstallName):
                    list.append(info)
        except psutil.NoSuchProcess:
            print("no process found with pid=", pid)
    str = ''
    for info in list:
        str += info.GameName
    print('正在进行的游戏：',str)
    return list
