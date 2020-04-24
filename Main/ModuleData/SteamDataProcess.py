import Config
from steamfiles import acf
import os
from ModuleData.GameSaveClass import GameInfo


# create game save class from acf file
def CreateGameSaveClass(path):
    # some game's info have spacial word like 'Sekiro™','古剑奇谭三(Gujian3)'
    with open(path, encoding="utf-8") as f:
        line = f.read()
    data = acf.loads(line)
    return GameInfo(data['AppState']['appid'], data['AppState']['name'], data['AppState']['installdir'])


# init local game config,when first launch app
def GetSteamGames():
    allfiles = os.listdir(Config.SteamInstallPath)
    acf_file_paths = []

    for f in allfiles:
        # Get all acf file
        if os.path.splitext(f)[1] == '.acf':
            acf_file_paths.append(f)

    gamelist = []
    for file in acf_file_paths:
        gamesave = CreateGameSaveClass(Config.SteamInstallPath + '\\' + file)
        gamelist.append(gamesave)
    print("steam库中游戏数量:",len(gamelist));
    return gamelist



