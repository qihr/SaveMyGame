from shutil import copyfile
from sys import exit
import os
import shutil


def CopyFile(gamelist):
    for gameinfo in gamelist:
        source = gameinfo.GamePath
        target = "E:/CodeProject/SaveMyGame/GameBackUp"

        #assert not os.path.isabs(source)
        #target = os.path.join(target, os.path.dirname(source))

        #os.makedirs(target)

        try:
            shutil.copytree(source, target)
        except IOError as e:
            print("Unable to copy file. %s" % e)
        except:
            print("Unexpected error:")



