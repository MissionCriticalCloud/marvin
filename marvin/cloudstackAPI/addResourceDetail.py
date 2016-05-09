"""Adds detail for the Resource."""
from baseCmd import *
from baseResponse import *


class addResourceDetailCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """Map of (key/value pairs)"""
        """Required"""
        self.details = []
        self.typeInfo['details'] = 'map'
        """resource id to create the details for"""
        """Required"""
        self.resourceid = None
        self.typeInfo['resourceid'] = 'string'
        """type of the resource"""
        """Required"""
        self.resourcetype = None
        self.typeInfo['resourcetype'] = 'string'
        """pass false if you want this detail to be disabled for the regular user. True by default"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        self.required = ["details", "resourceid", "resourcetype", ]


class addResourceDetailResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'
