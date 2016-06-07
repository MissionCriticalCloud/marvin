"""Lists all supported OS categories for this cloud."""
from baseCmd import *
from baseResponse import *


class listOsCategoriesCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """list Os category by id"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """list os category by name"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        self.required = []


class listOsCategoriesResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the ID of the OS category"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the name of the OS category"""
        self.name = None
        self.typeInfo['name'] = 'string'

