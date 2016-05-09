"""Lists host tags"""
from baseCmd import *
from baseResponse import *
class listHostTagsCmd (baseCmd):
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

class listHostTagsResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the ID of the host tag"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the host ID of the host tag"""
        self.hostid = None
        self.typeInfo['hostid'] = 'long'
        """the name of the host tag"""
        self.name = None
        self.typeInfo['name'] = 'string'

