#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial.tools.list_ports
import time
from win10toast import ToastNotifier
import threading
ports = list(serial.tools.list_ports.comports())
com = []



def notify(comport):

    toaster = ToastNotifier()
    toaster.show_toast("COM Port",
                        str(comport),
                        icon_path="custom.ico",
                        duration=10,
                       threaded=False,
                       )
def startNotify():
    for item in com:
        notify(item)


#########################################################################
x = threading.Thread(target=startNotify)





while True:
    ports = list(serial.tools.list_ports.comports())
    print(ports)
    print("ports")
    print(len(ports))
    print("com")
    print( len(com))
    time.sleep(1)
    if len(ports) < len(com):
        com = []
        for p in ports:
            com.append(p)

    if len(ports) > (len(com)):
        com = []
        for p in ports:
            com.append(str(p))
        startNotify()
        #print(com)
    if not ports:
        com =[]

