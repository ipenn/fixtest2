import quickfix as fix
import quickfix44 as fix44

import datetime
import random

class Application (fix.Application):
    
    def onCreate(self, sessionID):
        self.sessionID = sessionID
        print("Application created - session: " + sessionID.toString())

    def onLogon(self, sessionID):
        self.sessionID = sessionID
        print("onLogon - sessionID: " + sessionID.toString())

        mdr = fix.Message()
        mdr.getHeader().setField(fix.BeginString(fix.BeginString_FIX44))
        mdr.getHeader().setField(fix.MsgType(fix.MsgType_MarketDataRequest))

        mdr.setField(fix.MDReqID('17499348912123123'))      # a random string
        mdr.setField(fix.SubscriptionRequestType(fix.SubscriptionRequestType_SNAPSHOT_PLUS_UPDATES))        # what stater required
        mdr.setField(fix.MarketDepth(1))        # what stater required

        mdr.setField(fix.AggregatedBook(True))

        mdr.setField(fix.NoMDEntryTypes(1))     # what stater required
        mdr.setField(fix.MDUpdateType(fix.MDUpdateType_INCREMENTAL_REFRESH))        # what stater required

        group = fix44.MarketDataRequest().NoMDEntryTypes()
        group.setField(fix.MDEntryType(fix.MDEntryType_BID))
        mdr.addGroup(group)
        group.setField(fix.MDEntryType(fix.MDEntryType_OFFER))
        mdr.addGroup(group)

        mdr.setField(fix.NoRelatedSym(1))

        symbol = fix44.MarketDataRequest().NoRelatedSym()

        symbol.setField(fix.Symbol('GBP/USD'))
        mdr.addGroup(symbol)

        fix.Session.sendToTarget(mdr, sessionID)



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



