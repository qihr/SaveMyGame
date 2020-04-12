class GameInfo:
    SteamId = 0
    GameName = ""
    GamePath = ""
    GameSaveName = ""

    def __init__(self, id, name, installname, path='None',):
        self.SteamId = id
        self.GameName = name
        self.GamePath = path
        self.GameSaveName = installname
