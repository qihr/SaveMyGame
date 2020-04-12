import DataProcess
import  CSVHelper


DataProcess.ProcessFromDB()
CSVHelper.InitCsv()
for GameInfo in DataProcess.GameInfoList:
    CSVHelper.WriteGameInfoToCsv(GameInfo)