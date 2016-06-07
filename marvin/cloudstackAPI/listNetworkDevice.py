"""List network devices"""
from baseCmd import *
from baseResponse import *


class listNetworkDeviceCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """parameters for network device"""
        self.networkdeviceparameterlist = []
        self.typeInfo['networkdeviceparameterlist'] = 'map'
        """Network device type, now supports ExternalDhcp, PxeServer, JuniperSRXFirewall, PaloAltoFirewall"""
        self.networkdevicetype = None
        self.typeInfo['networkdevicetype'] = 'string'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        self.required = []


class listNetworkDeviceResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the ID of the network device"""
        self.id = None
        self.typeInfo['id'] = 'string'

