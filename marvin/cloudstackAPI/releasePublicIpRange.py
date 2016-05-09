"""Releases a Public IP range back to the system pool"""
from baseCmd import *
from baseResponse import *


class releasePublicIpRangeCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """the id of the Public IP range"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        self.required = ["id", ]


class releasePublicIpRangeResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'
