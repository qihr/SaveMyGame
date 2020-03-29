import getopt
import sys
import LoadLocalFile
import CopyFile
import platform

def main():
    print("Start Work")
    print('System Bit' + str(platform.architecture()))
    GameList = LoadLocalFile.LoadGameCFG()
    CopyFile.CopyFile(GameList);


if __name__ == "__main__":
    main()