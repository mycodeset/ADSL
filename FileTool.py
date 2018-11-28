class FileTool(object):

    #从文件中读取时间
    def get_time(self):
        f = open('time.config', mode='r', encoding='utf-8')
        Time = f.read()
        f.close()
        return int(Time)
    #将时间覆盖进文件中
    def set_time(self,Time):
        f = open('time.config', mode='w', encoding='utf-8')
        f.write(str(Time))
        f.close()
    #将IP追加到文件中
    def __write_IP(self,IP):
        f = open('IP.txt', mode='a', encoding='utf-8')
        f.write(IP+'\n')
        f.close()
    #从文件中读取IP
    def __get_IP(self):
        f = open('IP.txt', mode='r', encoding='utf-8')
        IP = f.read()
        f.close()
        return IP
    #判断IP，如果IP已经在文件中已经存在，则返回False，若IP为全新IP则返回Ture
    def judge_IP(self,IP):
        old_IP = self.__get_IP()
        #找到返回字符串位置，未找到则返回-1
        if old_IP.find(IP) == -1:
            self.__write_IP(IP)
            return True
        else:
            return False
    #将日志追加到文件中
    def write_log(self,boolean,IP):
        Time = str(self.get_time())
        f = open('log.txt', mode='a', encoding='utf-8')
        if boolean:
            f.write('设置时间为:'+Time+'暂未发现重复IP, 当前IP为:' + IP + '\n')
        else:
            f.write('设置时间为:'+Time+'发现重复IP, 当前IP为:' + IP + '\n')
        f.close()



