"""List hypervisors"""
from baseCmd import *
from baseResponse import *
class listHypervisorsCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """the zone id for listing hypervisors."""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'uuid'
        self.required = []

class listHypervisorsResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """Hypervisor name"""
        self.name = None
        self.typeInfo['name'] = 'string'

