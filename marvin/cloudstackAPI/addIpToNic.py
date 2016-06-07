"""Assigns secondary IP to NIC"""
from baseCmd import *
from baseResponse import *


class addIpToNicCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """the ID of the nic to which you want to assign private IP"""
        """Required"""
        self.nicid = None
        self.typeInfo['nicid'] = 'uuid'
        """Secondary IP Address"""
        self.ipaddress = None
        self.typeInfo['ipaddress'] = 'string'
        self.required = ["nicid", ]


class addIpToNicResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the ID of the secondary private IP addr"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """Secondary IP address"""
        self.ipaddress = None
        self.typeInfo['ipaddress'] = 'string'
        """the ID of the network"""
        self.networkid = None
        self.typeInfo['networkid'] = 'string'
        """the ID of the nic"""
        self.nicid = None
        self.typeInfo['nicid'] = 'string'
        """the ID of the vm"""
        self.virtualmachineid = None
        self.typeInfo['virtualmachineid'] = 'string'

