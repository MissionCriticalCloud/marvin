"""Lists physical networks"""
from baseCmd import *
from baseResponse import *


class listPhysicalNetworksCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """list physical network by id"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """search by name"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        """the Zone ID for the physical network"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'uuid'
        self.required = []


class listPhysicalNetworksResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the uuid of the physical network"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """Broadcast domain range of the physical network"""
        self.broadcastdomainrange = None
        self.typeInfo['broadcastdomainrange'] = 'string'
        """the domain id of the physical network owner"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """isolation methods"""
        self.isolationmethods = None
        self.typeInfo['isolationmethods'] = 'string'
        """name of the physical network"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the speed of the physical network"""
        self.networkspeed = None
        self.typeInfo['networkspeed'] = 'string'
        """state of the physical network"""
        self.state = None
        self.typeInfo['state'] = 'string'
        """comma separated tag"""
        self.tags = None
        self.typeInfo['tags'] = 'string'
        """the vlan of the physical network"""
        self.vlan = None
        self.typeInfo['vlan'] = 'string'
        """zone id of the physical network"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'string'

