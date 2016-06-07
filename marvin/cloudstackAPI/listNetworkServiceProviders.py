"""Lists network serviceproviders for a given physical network."""
from baseCmd import *
from baseResponse import *


class listNetworkServiceProvidersCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """list providers by name"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        """the Physical Network ID"""
        self.physicalnetworkid = None
        self.typeInfo['physicalnetworkid'] = 'uuid'
        """list providers by state"""
        self.state = None
        self.typeInfo['state'] = 'string'
        self.required = []


class listNetworkServiceProvidersResponse (baseResponse):
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

