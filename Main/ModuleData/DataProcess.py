import SteamDataProcess
import DBHelper

GameInfoList = []


def ProcessFromDB():
    global GameInfoList
    GameInfoList = SteamDataProcess.GetSteamGames()
    for Info in GameInfoList:
        res = DBHelper.CheckSteamInfo(Info.SteamId)
        if res is not None:
            Info.GamePath = res[2]
        print(Info.SteamId, Info.GamePath)




