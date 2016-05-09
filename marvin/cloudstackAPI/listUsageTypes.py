"""List Usage Types"""
from baseCmd import *
from baseResponse import *
class listUsageTypesCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        self.required = []

class listUsageTypesResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """description of usage type"""
        self.description = None
        self.typeInfo['description'] = 'string'
        """usage type"""
        self.usagetypeid = None
        self.typeInfo['usagetypeid'] = 'integer'

