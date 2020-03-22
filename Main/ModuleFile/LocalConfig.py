import winreg
import platform

def FindSteamLocation():
    string = r'SOFTWARE\WOW6432Node\Valve\Steam'
    handle = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, string)
    location, _type = winreg.QueryValueEx(handle, "InstallPath")
    print('bit' + str(platform.architecture()))
    print(location)

