import csv
from ModuleData.GameSaveClass import GameInfo
import Config


# 初始化CSV
def InitCsv():
    with open(Config.UserInfoPath, 'w', newline='', encoding='utf_8_sig') as csvfile:
        csv_write = csv.writer(csvfile)
        csv_write.writerow(['SteamID', 'Name','Path','GamePathName'])


# 写入CSV
def WriteInfoToCsv(gamesave):
    with open(Config.UserInfoPath, 'a',newline ='',encoding="utf_8_sig") as f:
        csv_write = csv.writer(f)
        data_row = [gamesave.SteamId, gamesave.GameName,gamesave.GamePath]
        csv_write.writerow(data_row)


# 列表写入CSV
def WriteInfosToCSV(list):
    for info in list:
        WriteInfoToCsv(info)


# 读取CSV
def LoadGameCSV():
    with open(Config.UserInfoPath, 'r', newline='', encoding='utf_8_sig') as csvfile:
        reader = csv.reader(csvfile)
        gamesters = []
        for item in reader:
            gamesters.append(GameInfo(item[0], item[1], item[2]))
    return gamesters
