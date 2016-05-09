"""Creates a physical network"""
from baseCmd import *
from baseResponse import *


class createPhysicalNetworkCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """the name of the physical network"""
        """Required"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the Zone ID for the physical network"""
        """Required"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'uuid'
        """the broadcast domain range for the physical network[Pod or Zone]. In Acton release it can be Zone only in Advance zone, and Pod in Basic"""
        self.broadcastdomainrange = None
        self.typeInfo['broadcastdomainrange'] = 'string'
        """domain ID of the account owning a physical network"""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """the isolation method for the physical network[VLAN/L3/GRE]"""
        self.isolationmethods = []
        self.typeInfo['isolationmethods'] = 'list'
        """the speed for the physical network[1G/10G]"""
        self.networkspeed = None
        self.typeInfo['networkspeed'] = 'string'
        """Tag the physical network"""
        self.tags = []
        self.typeInfo['tags'] = 'list'
        """the VLAN for the physical network"""
        self.vlan = None
        self.typeInfo['vlan'] = 'string'
        self.required = ["name", "zoneid", ]


class createPhysicalNetworkResponse(baseResponse):
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
