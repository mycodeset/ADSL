import os
import time
#拨号换IP
class ADSL(object):
    #name:ADSL连接名称 username:用户名 password:密码
    def __init__(self,name,username,password):
        self.name = name
        self.username = username
        self.password = password
    #连接
    def connect(self):
        cmd_str = "rasdial %s %s %s" % (self.name, self.username, self.password)
        os.system(cmd_str)
        time.sleep(1)
    #断开连接
    def disconnect(self):
        cmd_str = "rasdial %s /disconnect" % self.name
        os.system(cmd_str)
        time.sleep(1)
    #重新连接
    def reconnect(self):
        self.disconnect()
        self.connect()
