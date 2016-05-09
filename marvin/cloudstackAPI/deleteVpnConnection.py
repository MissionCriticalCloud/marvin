"""Delete site to site vpn connection"""
from baseCmd import *
from baseResponse import *


class deleteVpnConnectionCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """id of vpn connection"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        self.required = ["id", ]


class deleteVpnConnectionResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'
