class GameSave:
    SteamId = 0
    GameName = ""
    GamePath = ""

    def __init__(self, id, name, path):
        self.SteamId = id
        self.GameName = name
        self.GamePath = path
