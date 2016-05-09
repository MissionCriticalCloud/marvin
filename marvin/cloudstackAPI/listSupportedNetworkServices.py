"""Lists all network services provided by CloudStack or for the given Provider."""
from baseCmd import *
from baseResponse import *
class listSupportedNetworkServicesCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        """network service provider name"""
        self.provider = None
        self.typeInfo['provider'] = 'string'
        """network service name to list providers and capabilities of"""
        self.service = None
        self.typeInfo['service'] = 'string'
        self.required = []

class listSupportedNetworkServicesResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the service name"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the list of capabilities"""
        self.capability = []
        """the service provider name"""
        self.provider = []

class capability:
    def __init__(self):
        """"can this service capability value can be choosable while creatine network offerings"""
        self.canchooseservicecapability = None
        """"the capability name"""
        self.name = None
        """"the capability value"""
        self.value = None

class provider:
    def __init__(self):
        """"uuid of the network provider"""
        self.id = None
        """"true if individual services can be enabled/disabled"""
        self.canenableindividualservice = None
        """"the destination physical network"""
        self.destinationphysicalnetworkid = None
        """"the provider name"""
        self.name = None
        """"the physical network this belongs to"""
        self.physicalnetworkid = None
        """"services for this provider"""
        self.servicelist = None
        """"state of the network provider"""
        self.state = None

