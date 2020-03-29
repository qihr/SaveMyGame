import winreg
from steamfiles import acf
import os
import pytest

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


# load game info from acf file
def LoadAppInfo(path):
    print(path)
    with open(path, errors='ignore') as f:
        line = f.read()
    data = acf.loads(line)
    print(data['AppState']['name'])


# init local game config,when first launch app
def InitGamesInfoCsv():
    allfiles = os.listdir(GamesPath)
    acf_file_paths = []

    for f in allfiles:
        # Get all acf file
        if os.path.splitext(f)[1] == '.acf':
            acf_file_paths.append(f)

    for file in acf_file_paths:
        LoadAppInfo(GamesPath + '\\' + file)


FindGamesLocation()
InitGamesInfoCsv()
