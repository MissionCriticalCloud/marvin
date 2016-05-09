"""Creates resource tag(s)"""
from baseCmd import *
from baseResponse import *


class createTagsCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """list of resources to create the tags for"""
        """Required"""
        self.resourceids = []
        self.typeInfo['resourceids'] = 'list'
        """type of the resource"""
        """Required"""
        self.resourcetype = None
        self.typeInfo['resourcetype'] = 'string'
        """Map of tags (key/value pairs)"""
        """Required"""
        self.tags = []
        self.typeInfo['tags'] = 'map'
        """identifies client specific tag. When the value is not null, the tag can't be used by cloudStack code internally"""
        self.customer = None
        self.typeInfo['customer'] = 'string'
        self.required = ["resourceids", "resourcetype", "tags", ]


class createTagsResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'
