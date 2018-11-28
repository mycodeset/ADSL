import time
from ADSL import *
from FileTool import *
from urllib.request import urlopen

#用于调整时间间隔

#增加时间间隔参数
Time_Plus = 20
#减少时间间隔参数
Time_minus = 5

#从拨号成功到断开连接的时间间隔
connecting_time = 10

adlsTool = ADSL('宽带连接','username','password')

fileTool = FileTool()

while True:
    #获取当前IP
    IP = urlopen('http://ip.42.pl/raw').read().decode('utf-8')
    #判断IP是否已存在,存在返回false，不存在返回Ture
    flag = fileTool.judge_IP(IP)
    #将日志写入文件中
    fileTool.write_log(flag,IP)
    #断开宽带连接
    print('正在断开连接...')
    adlsTool.disconnect()
    #获取休眠时间
    Time = fileTool.get_time()
    #休眠
    print('休眠'+ str(Time) + '秒后继续...')
    time.sleep(Time)
    #开始拨号
    print('正在拨号...')
    adlsTool.connect()
    if flag:
        print('当前IP未与之前的IP匹配，将减小时间间隔')
        fileTool.set_time(Time-Time_minus)
    else:
        print('当前IP与之前IP重复，将增加时间间隔')
        fileTool.set_time(Time+Time_Plus)

    time.sleep(connecting_time)
    


    




