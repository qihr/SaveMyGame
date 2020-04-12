import csv

UserInfoPath = "GameLocationInfo.csv"


def InitCsv():
    with open(UserInfoPath, 'w', newline='', encoding='utf_8_sig') as csvfile:
        csv_write = csv.writer(csvfile)
        csv_write.writerow(['SteamID', 'Name','Path','GamePathName'])


def WriteGameInfoToCsv(gamesave):
    with open(UserInfoPath, 'a',newline ='',encoding="utf_8_sig") as f:
        csv_write = csv.writer(f)
        data_row = [gamesave.SteamId, gamesave.GameName,gamesave.GamePath]
        csv_write.writerow(data_row)