import winreg
import platform
from steamfiles import acf
import pytest

testpath = 'F:/Game/Steam/steamapps/appmanifest_12120.acf'

@pytest.fixture(name='acf_data')
def _acf_data():
    with open(testpath, 'rt') as f:
        yield f.read()

def FindSteamLocation():
    string = r'SOFTWARE\WOW6432Node\Valve\Steam'
    handle = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, string)
    location, _type = winreg.QueryValueEx(handle, "InstallPath")
    print('bit' + str(platform.architecture()))
    print(location)


    with open(testpath, 'rt') as f:
        line = f.read()
    data = acf.loads(line)
    print(data['AppState']['name'])


FindSteamLocation()