import os
import threading
import time
import psutil
import Config
import DataProcess
import FileHelper

RunningGame = []


def CheackGame():
    global RunningGame
    list = GetRunningGame()
    needsaveinfo = []
    for info in RunningGame:
        if all(x.SteamId != info.SteamId for x in list):
            needsaveinfo.append(info)
    RunningGame = list
    print('自动检测到的停止运行的游戏：' ,len(needsaveinfo))
    FileHelper.CopyFile(needsaveinfo)





def Monitor():
    print('监控线程开启!')
    while True:
        time.sleep(2)
        CheackGame()


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
