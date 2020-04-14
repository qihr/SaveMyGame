import platform
import DataProcess


def main():
    print("Start Work")
    print('操作系统信息：' + str(platform.architecture()))
    DataProcess.Init();


if __name__ == "__main__":
    main()