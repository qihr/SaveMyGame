class GameInfo:
    SteamId = 0
    GameName = ""
    SavePath = ""
    InstallName = ""
    GamePath = ""

    def __init__(self, id, name, installname, path='None',gamepath='None'):
        self.SteamId = id
        self.GameName = name
        self.SavePath = path
        self.InstallName = installname
        self.GamePath = gamepath
