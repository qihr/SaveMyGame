import platform
import DataProcess
import FileHelper
import UIView
import MonitorRunGame
import getpass
import time
import socket
import threading

def main():
    print("Start Work")
    print('操作系统信息：' + str(platform.architecture()))
    FileHelper.Init()
    DataProcess.Init()
    t = threading.Thread(target=MonitorRunGame.Monitor)
    t.start()

    UIView.Init()


if __name__ == "__main__":
    main()




