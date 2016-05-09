"""List the counters"""
from baseCmd import *
from baseResponse import *


class listCountersCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """ID of the Counter."""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """Name of the counter."""
        self.name = None
        self.typeInfo['name'] = 'string'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        """Source of the counter."""
        self.source = None
        self.typeInfo['source'] = 'string'
        self.required = []


class listCountersResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """the id of the Counter"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """Name of the counter."""
        self.name = None
        self.typeInfo['name'] = 'string'
        """Source of the counter."""
        self.source = None
        self.typeInfo['source'] = 'string'
        """Value in case of snmp or other specific counters."""
        self.value = None
        self.typeInfo['value'] = 'string'
        """zone id of counter"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'string'
