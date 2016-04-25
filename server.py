from threading import *
import socket
import time
import pickle
from datetime import *
from tkinter import *

class socky(object):
    def __init__(self,port):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.HOST = "reemer9997.duckdns.org"
        self.PORT = port
        self.s.bind((self.HOST,self.PORT))
        
connslist = []
c1 = socky(8900)
nameslist = []
print("Server Initiated. Searching for clients...")

def Main1():
    
    def sendtoall(info):
        data = info
        if not isinstance(data,list):
            data = data.encode("utf-8")
        for conn in connslist:
            try:
                conn.send(data)
            except:
                pass
        
    def recv(connected):
        namey = ""
        while True:
            data = connected.recv(1024)
            if not data:
                break
            data = data.decode("utf-8")
            if len(data) > 0:
                d = str(datetime.now().strftime('%H:%M'))
                if "warn" in data:
                    sendtoall(data)
                elif "kick" in data:
                    sendtoall(data)
                elif ((":" not in data) or ("¦" not in data) or (d not in data)) and ("blocked" not in data) and ("warn" not in data):
                    nameslist.append(data)
                    namey = data
                    print("Current clients:")
                    for nm in nameslist:
                        print(nm)
                    sendtoall(("SZKCHNG "+data))
                    crowwy = pickle.dumps(nameslist)
                    connected.send(crowwy)
                else:
                    sendtoall(data)
                    
        try:
            connslist.remove(connected)
        except:
            pass
        print("Client Disconnected: "+namey)
        try:
            nameslist.remove(namey)
        except:
            print("Client not found. Retrying...")
        noti = ("GNHCKZS "+namey)
        sendtoall(noti)
        Main1()
        

    c1.s.listen(20)
    conn1, addr = c1.s.accept()
    connslist.append(conn1)
    print("""Client Connected: """+str(addr[0])+" on port "+str(addr[1])+"""
Forwarded to Client Handler.""")
    print("Searching for new clients...")
    recv(conn1)
    

for x in range(10):
    Thread(target=Main1).start()


