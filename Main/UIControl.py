import platform
import DataProcess
import FileHelper
import DataProcess


def ShortSave():
    print('快捷备份正在运行的游戏！')

    FileHelper.Init()
    DataProcess.Init()
    print('游戏目录！', len(DataProcess.GameInfoList))
    list=[]
    for info in DataProcess.GameInfoList:
        if info.SteamId == 814380:
            print(info.SteamId)
            list.append(info)
    print(len(list))
    FileHelper.CopyFile(list)

