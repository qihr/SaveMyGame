import csv
from GameSaveClass import GameSave


def LoadGameCFG():
    print("Load Local csv....")

    csvFile = open("GameLocationInfo.csv", "r")
    reader = csv.reader(csvFile)

    gamesters = []
    for item in reader:
        gamesters.append(GameSave(item[0], item[1], item[2]))
    csvFile.close()

    return gamesters


