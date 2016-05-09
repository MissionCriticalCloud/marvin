"""Lists Regions"""
from baseCmd import *
from baseResponse import *
class listRegionsCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """List Region by region ID."""
        self.id = None
        self.typeInfo['id'] = 'integer'
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """List Region by region name."""
        self.name = None
        self.typeInfo['name'] = 'string'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        self.required = []

class listRegionsResponse (baseResponse):
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

