import os

ResPath = 'Res'
DBName = 'GameSaveInfo.db'
InfoPath = 'GameLocationInfo.csv'
FilePath = os.getcwd()

DBPath = os.path.abspath(os.path.join(FilePath,'..',ResPath, DBName))
UserInfoPath = os.path.abspath(os.path.join(FilePath,'..',ResPath, InfoPath))
