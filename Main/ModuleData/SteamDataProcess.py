import winreg
from steamfiles import acf
import os
from ModuleData.GameSaveClass import GameSave

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
    return GameSave(data['AppState']['appid'], data['AppState']['name'], data['AppState']['installdir'])


# init local game config,when first launch app
def GetSteamGames():
    FindGamesLocation()
    allfiles = os.listdir(GamesPath)
    acf_file_paths = []

    for f in allfiles:
        # Get all acf file
        if os.path.splitext(f)[1] == '.acf':
            acf_file_paths.append(f)

    # InitCsv()
    gamelist = []
    for file in acf_file_paths:
        gamesave = CreateGameSaveClass(GamesPath + '\\' + file)
        gamelist.append(gamesave)
    print("steam库中游戏数量:",len(gamelist));
    return gamelist



