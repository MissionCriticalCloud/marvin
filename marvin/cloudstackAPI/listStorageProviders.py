"""Lists storage providers."""
from baseCmd import *
from baseResponse import *


class listStorageProvidersCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """the type of storage provider: either primary or image"""
        """Required"""
        self.type = None
        self.typeInfo['type'] = 'string'
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        self.required = ["type", ]


class listStorageProvidersResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the name of the storage provider"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the type of the storage provider: primary or image provider"""
        self.type = None
        self.typeInfo['type'] = 'string'

