"""Removes specified region"""
from baseCmd import *
from baseResponse import *


class removeRegionCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """ID of the region to delete"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'integer'
        self.required = ["id", ]


class removeRegionResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

