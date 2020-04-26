import platform
import DataProcess
import FileHelper
import DataProcess
import MonitorRunGame


def ShortSave():
    print('快捷备份正在运行的游戏！')
    list= MonitorRunGame.GetRunningGame()
    FileHelper.CopyFile(list)

