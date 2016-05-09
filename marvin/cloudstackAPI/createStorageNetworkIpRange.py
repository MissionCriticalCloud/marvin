"""Creates a Storage network IP range."""
from baseCmd import *
from baseResponse import *
class createStorageNetworkIpRangeCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "true"
        """the gateway for storage network"""
        """Required"""
        self.gateway = None
        self.typeInfo['gateway'] = 'string'
        """the netmask for storage network"""
        """Required"""
        self.netmask = None
        self.typeInfo['netmask'] = 'string'
        """UUID of pod where the ip range belongs to"""
        """Required"""
        self.podid = None
        self.typeInfo['podid'] = 'uuid'
        """the beginning IP address"""
        """Required"""
        self.startip = None
        self.typeInfo['startip'] = 'string'
        """the ending IP address"""
        self.endip = None
        self.typeInfo['endip'] = 'string'
        """Optional. The vlan the ip range sits on, default to Null when it is not specificed which means you network is not on any Vlan."""
        self.vlan = None
        self.typeInfo['vlan'] = 'integer'
        self.required = ["gateway","netmask","podid","startip",]

class createStorageNetworkIpRangeResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the uuid of storage network IP range."""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the end ip of the storage network IP range"""
        self.endip = None
        self.typeInfo['endip'] = 'string'
        """the gateway of the storage network IP range"""
        self.gateway = None
        self.typeInfo['gateway'] = 'string'
        """the netmask of the storage network IP range"""
        self.netmask = None
        self.typeInfo['netmask'] = 'string'
        """the network uuid of storage network IP range"""
        self.networkid = None
        self.typeInfo['networkid'] = 'string'
        """the Pod uuid for the storage network IP range"""
        self.podid = None
        self.typeInfo['podid'] = 'string'
        """the start ip of the storage network IP range"""
        self.startip = None
        self.typeInfo['startip'] = 'string'
        """the ID or VID of the VLAN."""
        self.vlan = None
        self.typeInfo['vlan'] = 'integer'
        """the Zone uuid of the storage network IP range"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'string'

