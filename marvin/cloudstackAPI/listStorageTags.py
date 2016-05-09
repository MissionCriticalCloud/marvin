"""Lists storage tags"""
from baseCmd import *
from baseResponse import *


class listStorageTagsCmd(baseCmd):
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
        self.required = []


class listStorageTagsResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """the ID of the storage tag"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the name of the storage tag"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the pool ID of the storage tag"""
        self.poolid = None
        self.typeInfo['poolid'] = 'long'
