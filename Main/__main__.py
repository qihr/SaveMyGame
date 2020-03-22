import getopt
import sys
import LoadLocalFile
import CopyFile

def main():
    print("Start Work")
    GameList = LoadLocalFile.LoadGameCFG()
    CopyFile.CopyFile(GameList);


if __name__ == "__main__":
    main()