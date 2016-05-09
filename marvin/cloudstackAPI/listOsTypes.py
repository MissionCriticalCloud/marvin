"""Lists all supported OS types for this cloud."""
from baseCmd import *
from baseResponse import *
class listOsTypesCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """list os by description"""
        self.description = None
        self.typeInfo['description'] = 'string'
        """list by Os type Id"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """list by Os Category id"""
        self.oscategoryid = None
        self.typeInfo['oscategoryid'] = 'uuid'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        self.required = []

class listOsTypesResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the ID of the OS type"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the name/description of the OS type"""
        self.description = None
        self.typeInfo['description'] = 'string'
        """is the guest OS user defined"""
        self.isuserdefined = None
        self.typeInfo['isuserdefined'] = 'string'
        """the ID of the OS category"""
        self.oscategoryid = None
        self.typeInfo['oscategoryid'] = 'string'

