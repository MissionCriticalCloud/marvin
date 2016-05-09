"""Lists affinity group types available"""
from baseCmd import *
from baseResponse import *
class listAffinityGroupTypesCmd (baseCmd):
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

class listAffinityGroupTypesResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the type of the affinity group"""
        self.type = None
        self.typeInfo['type'] = 'string'

