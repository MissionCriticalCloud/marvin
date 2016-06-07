"""delete a nicira nvp device"""
from baseCmd import *
from baseResponse import *


class deleteNiciraNvpDeviceCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """Nicira device ID"""
        """Required"""
        self.nvpdeviceid = None
        self.typeInfo['nvpdeviceid'] = 'uuid'
        self.required = ["nvpdeviceid", ]


class deleteNiciraNvpDeviceResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

