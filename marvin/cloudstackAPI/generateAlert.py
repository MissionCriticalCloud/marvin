"""Generates an alert"""
from baseCmd import *
from baseResponse import *
class generateAlertCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "true"
        """Alert description"""
        """Required"""
        self.description = None
        self.typeInfo['description'] = 'string'
        """Name of the alert"""
        """Required"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """Type of the alert"""
        """Required"""
        self.type = None
        self.typeInfo['type'] = 'short'
        """Pod id for which alert is generated"""
        self.podid = None
        self.typeInfo['podid'] = 'uuid'
        """Zone id for which alert is generated"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'uuid'
        self.required = ["description","name","type",]

class generateAlertResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

