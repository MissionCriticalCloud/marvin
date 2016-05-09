"""Releases a dedicated guest vlan range to the system"""
from baseCmd import *
from baseResponse import *


class releaseDedicatedGuestVlanRangeCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """the ID of the dedicated guest vlan range"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        self.required = ["id", ]


class releaseDedicatedGuestVlanRangeResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'
