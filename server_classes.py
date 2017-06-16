#bin/bash/env python
import socket
from hashlib import *
import time
import os



class server():
    def __init__(self):
        self.log_path="/etc/Botmessage_Server/log"
        self.time=time.asctime()



    def loger(self, error):
        if not os.path.exists(self.log_path):
            os.chdir("/etc")
            os.mkdirs("Botmessage_Server/log")
            os.chdir(self.log_path)
            server_log=open("log.log", "w")
            server_log.write(self.time+" "+str(error))
            server_log.close()
        else:
            os.chdir(self.log_path)
            server_log=open("log.log","a")
            server_log.write("\n"+self.time+" "+str(error))
            server_log.close()

    def setup(self, username ,mac):
        try:
            data_bank=open("data.txt","a")
            data_bank.write("Name: "+str(username)+" mac_address: "+str(mac))
            data.close()
        except Exception as e:
            self.loger(e)


    def login():
        pass
