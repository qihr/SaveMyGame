import platform
import DataProcess
import FileHelper
import UIView
import MonitorRunGame
import getpass
import time
import socket


def main():
    print("Start Work")
    print('操作系统信息：' + str(platform.architecture()))
    FileHelper.Init()
    DataProcess.Init()
    UIView.Init()
    while True:
        for info in DataProcess.GameInfoList:
            # print("检查的游戏:",info.GameName)
            if MonitorRunGame.IsGameRunning3(info):
                print(info.GameName)
    time.sleep(10)


if __name__ == "__main__":
    main()




