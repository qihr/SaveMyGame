from ModuleData.GameSaveClass import GameSave
import SteamDataProcess
import DBHelper
import CSVHelper
import FileHelper

GameInfoList = []
LocalInfoList = []
CSVInfoList = []


# 格式化Gameinfo为正规数据
def ProcessFromDB():
    for Info in GameInfoList:
        AddSavePathData(Info)


# 从数据库添加信息
def AddSavePathData(info):
    res = DBHelper.CheckSteamInfo(info.SteamId)
    if res is not None:
        info.GamePath = res[2]


# 对比本地和CSV数据
def CompareCSVAndLocal():
    newinfolist = []
    deleteinfolist = []
    for info in LocalInfoList:
        if all(x.SteamId != info.SteamId for x in CSVInfoList):
            print(info.GameName)
            newinfolist.append(info)
    for info in CSVInfoList:
        if info not in LocalInfoList:
            deleteinfolist.append(info)
            CSVInfoList.remove(info)

    SaveDeletedInfo(deleteinfolist)
    # GameInfoList.extend(CSVInfoList)
    GameInfoList.extend(newinfolist)


# 将删除的数据写入数据库
def SaveDeletedInfo(deletelist):
    print("a")


# 本地是否与csv不同
def IsDataDifferent():
    for info in LocalInfoList:
        if all(x.SteamId != info.SteamId for x in CSVInfoList):
            return True
    return False


def Init():
    global LocalInfoList, CSVInfoList
    LocalInfoList = SteamDataProcess.GetSteamGames()
    if FileHelper.IsHaveLocalCSV():
        CSVInfoList = CSVHelper.LoadGameCSV()
        print('CSVInfoList的数据数量', len(CSVInfoList))
        if IsDataDifferent():
            print("游戏信息不一致，进入比较处理流程")
            CompareCSVAndLocal()
        else:
            print("游戏信息一致，退出")
            return;
    else:
        print('LocalInfoList的数据数量', len(LocalInfoList))
        GameInfoList.extend(LocalInfoList)
        CSVHelper.InitCsv()
    ProcessFromDB()
    print('GameInfoList的数据数量',len(GameInfoList))
    CSVHelper.WriteInfosToCSV(GameInfoList)
Init()










