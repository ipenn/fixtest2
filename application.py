import quickfix as fix
import quickfix44 as fixMsg
import datetime
import random

class Application (fix.Application):
    
    def onCreate(self, sessionID):
        self.sessionID = sessionID
        print("Application created - session: " + sessionID.toString())

    def onLogon(self, sessionID):
        self.sessionID = sessionID
        print("onLogon - sessionID: " + sessionID.toString())

    def onLogout(self, sessionID):
        self.sessionID = sessionID
        print("onLogout - sessionID: " + sessionID.toString())
    
    def toAdmin(self, message, sessionID):
        self.sessionID = sessionID
        self.message = message
        print("toAdmin - message: " + message.toString() + " sessionID:" + sessionID.toString())
        
        beginString = fix.BeginString()
        msgType = fix.MsgType()
        message.getHeader().getField(beginString)
        message.getHeader().getField(msgType)
        if msgType.getValue() == 'A':
            message.setField(fix.Username('sgmmDEMOSOMFXTRADESTR1'))
            message.setField(fix.Password('Stater123'))
            pass
            
    def toApp(self, message, sessionID): 
        self.sessionID = sessionID
        self.message = message
        print("toApp - message: " + message.toString() + " sessionID:" + sessionID.toString())
    
    def fromAdmin(self, message, sessionID):
        self.sessionID = sessionID
        self.message = message
        print("fromAdmin - message: " + message.toString() + " sessionID:" + sessionID.toString())
    
    def fromApp(self, message, sessionID):
        self.sessionID = sessionID
        self.message = message
        print("fromApp - message: " + message.toString() + " sessionID:" + sessionID.toString())
