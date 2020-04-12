import csv
from ModuleData.GameSaveClass import GameSave

UserInfoPath = "GameLocationInfo.csv"


def InitCsv():
    with open(UserInfoPath, 'w', newline='', encoding='utf_8_sig') as csvfile:
        csv_write = csv.writer(csvfile)
        csv_write.writerow(['SteamID', 'Name','Path','GamePathName'])


def WriteInfoToCsv(gamesave):
    with open(UserInfoPath, 'a',newline ='',encoding="utf_8_sig") as f:
        csv_write = csv.writer(f)
        data_row = [gamesave.SteamId, gamesave.GameName,gamesave.GamePath]
        csv_write.writerow(data_row)


def WriteInfosToCSV(list):
    for info in list:
        WriteInfoToCsv(info)



def LoadGameCSV():
    print("Load Local csv....")
    with open(UserInfoPath, 'r', newline='', encoding='utf_8_sig') as csvfile:
        reader = csv.reader(csvfile)
        gamesters = []
        for item in reader:
            gamesters.append(GameSave(item[0], item[1], item[2]))
    return gamesters
