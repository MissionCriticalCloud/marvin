"""Updates a region"""
from baseCmd import *
from baseResponse import *


class updateRegionCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """Id of region to update"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'integer'
        """updates region with this end point"""
        self.endpoint = None
        self.typeInfo['endpoint'] = 'string'
        """updates region with this name"""
        self.name = None
        self.typeInfo['name'] = 'string'
        self.required = ["id", ]


class updateRegionResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the ID of the region"""
        self.id = None
        self.typeInfo['id'] = 'integer'
        """the end point of the region"""
        self.endpoint = None
        self.typeInfo['endpoint'] = 'string'
        """true if GSLB service is enabled in the region, false otherwise"""
        self.gslbserviceenabled = None
        self.typeInfo['gslbserviceenabled'] = 'boolean'
        """the name of the region"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """true if security groups support is enabled, false otherwise"""
        self.portableipserviceenabled = None
        self.typeInfo['portableipserviceenabled'] = 'boolean'

