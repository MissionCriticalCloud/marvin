"""Updates a network serviceProvider of a physical network"""
from baseCmd import *
from baseResponse import *


class updateNetworkServiceProviderCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """network service provider id"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """the list of services to be enabled for this physical network service provider"""
        self.servicelist = []
        self.typeInfo['servicelist'] = 'list'
        """Enabled/Disabled/Shutdown the physical network service provider"""
        self.state = None
        self.typeInfo['state'] = 'string'
        self.required = ["id", ]


class updateNetworkServiceProviderResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """uuid of the network provider"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """true if individual services can be enabled/disabled"""
        self.canenableindividualservice = None
        self.typeInfo['canenableindividualservice'] = 'boolean'
        """the destination physical network"""
        self.destinationphysicalnetworkid = None
        self.typeInfo['destinationphysicalnetworkid'] = 'string'
        """the provider name"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the physical network this belongs to"""
        self.physicalnetworkid = None
        self.typeInfo['physicalnetworkid'] = 'string'
        """services for this provider"""
        self.servicelist = None
        self.typeInfo['servicelist'] = 'list'
        """state of the network provider"""
        self.state = None
        self.typeInfo['state'] = 'string'

