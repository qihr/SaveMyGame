import os
import winreg

IconName = 'logo.ico'
ResPath = 'Res'
BackUpDir = 'BackUp'
DBName = 'GameSaveInfo.db'
TableName = 'GameLocationInfo.csv'
FilePath = os.getcwd()

BackUpPath = os.path.abspath(os.path.join(FilePath,'..', BackUpDir))
print('备份文件夹位置:' ,BackUpPath)
DBPath = os.path.abspath(os.path.join(FilePath, '..', ResPath, DBName))
UserInfoPath = os.path.abspath(os.path.join(FilePath, '..', ResPath, TableName))
IconPath = os.path.abspath(os.path.join(FilePath, '..', ResPath, IconName))

SteamHKey = r'SOFTWARE\WOW6432Node\Valve\Steam'
SteamInstallPath = ''


# find Steam install and acf file path
handle = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, SteamHKey)
location, _type = winreg.QueryValueEx(handle, "InstallPath")
SteamInstallPath = location + '\steamapps'
print('Steam安装位置:', SteamInstallPath)

