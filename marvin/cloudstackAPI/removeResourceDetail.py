"""Removes detail for the Resource."""
from baseCmd import *
from baseResponse import *


class removeResourceDetailCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """Delete details for resource id"""
        """Required"""
        self.resourceid = None
        self.typeInfo['resourceid'] = 'string'
        """Delete detail by resource type"""
        """Required"""
        self.resourcetype = None
        self.typeInfo['resourcetype'] = 'string'
        """Delete details matching key/value pairs"""
        self.key = None
        self.typeInfo['key'] = 'string'
        self.required = ["resourceid", "resourcetype", ]


class removeResourceDetailResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'
