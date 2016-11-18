# -*- coding: utf-8 -*-
import quickfix as fix
from application import Application
import os
import time

fixIni = os.getcwd() + "/FIX.ini"

try:
    settings = fix.SessionSettings(fixIni)
    application = Application()
    print(application)
    store = fix.FileStoreFactory("store")
    log = fix.FileLogFactory("log")
    
    initiator = fix.SocketInitiator(application, store, settings, log)
    
except fix.ConfigError, e:
    print(e)
    raise RuntimeError('FIXCLIENT failure')

initiator.start()
print ("FIXCLIENT initiator start complete")
while True:
    time.sleep(1)
