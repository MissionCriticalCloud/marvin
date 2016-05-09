"""Deleting resource tag(s)"""
from baseCmd import *
from baseResponse import *


class deleteTagsCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """Delete tags for resource id(s)"""
        """Required"""
        self.resourceids = []
        self.typeInfo['resourceids'] = 'list'
        """Delete tag by resource type"""
        """Required"""
        self.resourcetype = None
        self.typeInfo['resourcetype'] = 'string'
        """Delete tags matching key/value pairs"""
        self.tags = []
        self.typeInfo['tags'] = 'map'
        self.required = ["resourceids", "resourcetype", ]


class deleteTagsResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'
