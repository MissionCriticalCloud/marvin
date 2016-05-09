"""Disables static rule for given IP address"""
from baseCmd import *
from baseResponse import *
class disableStaticNatCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "true"
        """the public IP address ID for which static NAT feature is being disabled"""
        """Required"""
        self.ipaddressid = None
        self.typeInfo['ipaddressid'] = 'uuid'
        self.required = ["ipaddressid",]

class disableStaticNatResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

