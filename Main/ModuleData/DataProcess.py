import SteamDataProcess
import DBHelper
import CSVHelper
import FileHelper

GameInfoList = []
LocalInfoList = []
CSVInfoList = []
RunningList = []


# 格式化Gameinfo为正规数据
def ProcessFromDB(list):
    for info in list:
        AddSavePathData(info)


# 根据环境变量格式化路径
def FormatSavePath(list):
    for info in list:
        info.GamePath = FileHelper.ReplaceEnvironment(info)


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
            newinfolist.append(info)
    for info in CSVInfoList:
        if info not in LocalInfoList:
            deleteinfolist.append(info)
            CSVInfoList.remove(info)

    SaveDeletedInfo(deleteinfolist)
    # GameInfoList.extend(CSVInfoList)
    # GameInfoList.extend(newinfolist)
    return newinfolist


# 将删除的数据写入数据库
def SaveDeletedInfo(deletelist):
    pass


# 本地是否与csv不同
def IsDataDifferent():
    for info in LocalInfoList:
        if all(x.SteamId != info.SteamId for x in CSVInfoList):
            return True
    return False


def Init():
    global LocalInfoList, CSVInfoList, GameInfoList
    LocalInfoList = SteamDataProcess.GetSteamGames()
    if FileHelper.IsHaveLocalCSV():
        CSVInfoList = CSVHelper.LoadGameCSV()
        if IsDataDifferent():
            newlist = CompareCSVAndLocal()
            ProcessFromDB(newlist)
            FormatSavePath(newlist)
            CSVHelper.WriteInfosToCSV(newlist)
        else:
            GameInfoList = CSVInfoList;
            ProcessFromDB(GameInfoList)
            FormatSavePath(GameInfoList)
    else:
        GameInfoList.extend(LocalInfoList)
        CSVHelper.InitCsv()
        ProcessFromDB(GameInfoList)
        FormatSavePath(GameInfoList)
        CSVHelper.WriteInfosToCSV(GameInfoList)
