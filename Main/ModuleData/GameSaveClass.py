class GameInfo:
    SteamId = 0
    GameName = ""
    SavePath = ""
    InstallName = ""
    GamePath = ""
    ExecuteName = ''

    def __init__(self, id, name, installname, path='None', gamepath='None', exe=''):
        self.SteamId = id
        self.GameName = name
        self.SavePath = path
        self.InstallName = installname
        self.GamePath = gamepath
        self.ExecuteName = exe
