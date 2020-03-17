import csv
import LoadLocalFile
import CopyFile

GameList = LoadLocalFile.LoadGameCFG()
CopyFile.CopyFile(GameList);
