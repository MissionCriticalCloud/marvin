"""Destroys a l2tp/ipsec remote access vpn"""
from baseCmd import *
from baseResponse import *


class deleteRemoteAccessVpnCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """public ip address id of the vpn server"""
        """Required"""
        self.publicipid = None
        self.typeInfo['publicipid'] = 'uuid'
        self.required = ["publicipid", ]


class deleteRemoteAccessVpnResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'
