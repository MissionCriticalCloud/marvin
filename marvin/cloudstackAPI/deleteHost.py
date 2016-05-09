"""Deletes a host."""
from baseCmd import *
from baseResponse import *
class deleteHostCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """the host ID"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """Force delete the host. All HA enabled vms running on the host will be put to HA; HA disabled ones will be stopped"""
        self.forced = None
        self.typeInfo['forced'] = 'boolean'
        """Force destroy local storage on this host. All VMs created on this local storage will be destroyed"""
        self.forcedestroylocalstorage = None
        self.typeInfo['forcedestroylocalstorage'] = 'boolean'
        self.required = ["id",]

class deleteHostResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

