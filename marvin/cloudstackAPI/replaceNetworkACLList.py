"""Replaces ACL associated with a network or private gateway"""
from baseCmd import *
from baseResponse import *


class replaceNetworkACLListCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """the ID of the network ACL"""
        """Required"""
        self.aclid = None
        self.typeInfo['aclid'] = 'uuid'
        """the ID of the private gateway"""
        self.gatewayid = None
        self.typeInfo['gatewayid'] = 'uuid'
        """the ID of the network"""
        self.networkid = None
        self.typeInfo['networkid'] = 'uuid'
        self.required = ["aclid", ]


class replaceNetworkACLListResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

