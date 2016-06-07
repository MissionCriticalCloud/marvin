"""Lists Nicira NVP devices"""
from baseCmd import *
from baseResponse import *


class listNiciraNvpDevicesCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """nicira nvp device ID"""
        self.nvpdeviceid = None
        self.typeInfo['nvpdeviceid'] = 'uuid'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        """the Physical Network ID"""
        self.physicalnetworkid = None
        self.typeInfo['physicalnetworkid'] = 'uuid'
        self.required = []


class listNiciraNvpDevicesResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the controller Ip address"""
        self.hostname = None
        self.typeInfo['hostname'] = 'string'
        """this L3 gateway service Uuid"""
        self.l3gatewayserviceuuid = None
        self.typeInfo['l3gatewayserviceuuid'] = 'string'
        """device name"""
        self.niciradevicename = None
        self.typeInfo['niciradevicename'] = 'string'
        """device id of the Nicire Nvp"""
        self.nvpdeviceid = None
        self.typeInfo['nvpdeviceid'] = 'string'
        """the physical network to which this Nirica Nvp belongs to"""
        self.physicalnetworkid = None
        self.typeInfo['physicalnetworkid'] = 'string'
        """name of the provider"""
        self.provider = None
        self.typeInfo['provider'] = 'string'
        """the transport zone Uuid"""
        self.transportzoneuuid = None
        self.typeInfo['transportzoneuuid'] = 'string'

