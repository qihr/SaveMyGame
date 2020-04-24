import platform
import DataProcess
import FileHelper

def main():
    print("Start Work")
    print('操作系统信息：' + str(platform.architecture()))
    FileHelper.Init()
    DataProcess.Init()


if __name__ == "__main__":
    main()



