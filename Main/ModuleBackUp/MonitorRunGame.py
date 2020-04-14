import os
import time
import psutil


# 游戏是否运行
def IsGameRunning(gamename):
    try:
        print('tasklist | findstr ' + gamename)
        process = len(os.popen('tasklist | findstr ' + gamename).readlines())
        print(process)
        if process >= 1:
            return True
        else:
            return False
    except:
        print("程序错误")
        return False


# 游戏是否运行第二种实现方法
def IsGameRunning2(gamename):
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        if p.name() == gamename:
            return True
    return False


if __name__=="__main__":
    flag=True
    while flag:
        flag = IsGameRunning2("Battle.net.exe")
        print(flag)
        if flag == False:
            print("关闭了！")
        time.sleep(10)##每隔60s进行检查