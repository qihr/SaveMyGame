import winreg
from steamfiles import acf
import os
from GameSaveClass import GameSave
import csv
import codecs

SteamHKey = r'SOFTWARE\WOW6432Node\Valve\Steam'
GamesPath = ''


# find steam and acf file path
def FindGamesLocation():
    # find Steam install path
    handle = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, SteamHKey)
    location, _type = winreg.QueryValueEx(handle, "InstallPath")

    # set games info location path
    global GamesPath
    GamesPath = location + '\steamapps'
    print(GamesPath)


# create game save class from acf file
def CreateGameSaveClass(path):
    # some game's info have spacial word like 'Sekiro™','古剑奇谭三(Gujian3)'
    with open(path, encoding="utf-8") as f:
        line = f.read()
    data = acf.loads(line)
    return GameSave(data['AppState']['appid'], data['AppState']['name'], path)


def InitCsv():
    path = "GameLocationInfo.csv"

    with open(path, 'w', newline='', encoding='utf_8_sig') as csvfile:
        csv_write = csv.writer(csvfile)
        csv_write.writerow(['SteamID', 'Name','Path'])


def WriteGameInfoToCsv(gamesave):
    path = "GameLocationInfo.csv"
    with open(path, 'a',newline ='',encoding="utf_8_sig") as f:
        csv_write = csv.writer(f)
        data_row = [gamesave.SteamId, gamesave.GameName,gamesave.GamePath]
        csv_write.writerow(data_row)


# init local game config,when first launch app
def InitGamesInfoCsv():
    allfiles = os.listdir(GamesPath)
    acf_file_paths = []

    for f in allfiles:
        # Get all acf file
        if os.path.splitext(f)[1] == '.acf':
            acf_file_paths.append(f)

    InitCsv()
    for file in acf_file_paths:
        gamesave = CreateGameSaveClass(GamesPath + '\\' + file)
        WriteGameInfoToCsv(gamesave)

FindGamesLocation()
InitGamesInfoCsv()
