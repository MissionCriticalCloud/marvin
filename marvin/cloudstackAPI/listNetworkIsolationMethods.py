"""Lists supported methods of network isolation"""
from baseCmd import *
from baseResponse import *


class listNetworkIsolationMethodsCmd (baseCmd):
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


class listNetworkIsolationMethodsResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """Network isolation method name"""
        self.name = None
        self.typeInfo['name'] = 'string'

