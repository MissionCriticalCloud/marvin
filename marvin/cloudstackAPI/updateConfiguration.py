"""Updates a configuration."""
from baseCmd import *
from baseResponse import *
class updateConfigurationCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """the name of the configuration"""
        """Required"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the ID of the Account to update the parameter value for corresponding account"""
        self.accountid = None
        self.typeInfo['accountid'] = 'uuid'
        """the ID of the Cluster to update the parameter value for corresponding cluster"""
        self.clusterid = None
        self.typeInfo['clusterid'] = 'uuid'
        """the ID of the Storage pool to update the parameter value for corresponding storage pool"""
        self.storageid = None
        self.typeInfo['storageid'] = 'uuid'
        """the value of the configuration"""
        self.value = None
        self.typeInfo['value'] = 'string'
        """the ID of the Zone to update the parameter value for corresponding zone"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'uuid'
        self.required = ["name",]

class updateConfigurationResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the value of the configuration"""
        self.id = None
        self.typeInfo['id'] = 'long'
        """the category of the configuration"""
        self.category = None
        self.typeInfo['category'] = 'string'
        """the description of the configuration"""
        self.description = None
        self.typeInfo['description'] = 'string'
        """the name of the configuration"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """scope(zone/cluster/pool/account) of the parameter that needs to be updated"""
        self.scope = None
        self.typeInfo['scope'] = 'string'
        """the value of the configuration"""
        self.value = None
        self.typeInfo['value'] = 'string'

