import os
import winreg

IconName = 'logo.ico'
ResPath = 'Res'
DBName = 'GameSaveInfo.db'
InfoPath = 'GameLocationInfo.csv'
FilePath = os.getcwd()

DBPath = os.path.abspath(os.path.join(FilePath, '..', ResPath, DBName))
UserInfoPath = os.path.abspath(os.path.join(FilePath, '..', ResPath, InfoPath))
IconPath = os.path.abspath(os.path.join(FilePath, '..', ResPath, IconName))

SteamHKey = r'SOFTWARE\WOW6432Node\Valve\Steam'
SteamInstallPath = ''


# find Steam install and acf file path
handle = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, SteamHKey)
location, _type = winreg.QueryValueEx(handle, "InstallPath")
SteamInstallPath = location + '\steamapps'
print('Steam安装位置:', SteamInstallPath)

