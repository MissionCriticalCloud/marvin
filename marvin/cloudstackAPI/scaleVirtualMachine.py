"""Scales the virtual machine to a new service offering."""
from baseCmd import *
from baseResponse import *
class scaleVirtualMachineCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "true"
        """The ID of the virtual machine"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """the ID of the service offering for the virtual machine"""
        """Required"""
        self.serviceofferingid = None
        self.typeInfo['serviceofferingid'] = 'uuid'
        """name value pairs of custom parameters for cpu,memory and cpunumber. example details[i].name=value"""
        self.details = []
        self.typeInfo['details'] = 'map'
        self.required = ["id","serviceofferingid",]

class scaleVirtualMachineResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

