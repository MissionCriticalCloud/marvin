"""Adds secondary storage."""
from baseCmd import *
from baseResponse import *


class addSecondaryStorageCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """the URL for the secondary storage"""
        """Required"""
        self.url = None
        self.typeInfo['url'] = 'string'
        """the Zone ID for the secondary storage"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'uuid'
        self.required = ["url", ]


class addSecondaryStorageResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """the ID of the image store"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the details of the image store"""
        self.details = None
        self.typeInfo['details'] = 'set'
        """the name of the image store"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the protocol of the image store"""
        self.protocol = None
        self.typeInfo['protocol'] = 'string'
        """the provider name of the image store"""
        self.providername = None
        self.typeInfo['providername'] = 'string'
        """the scope of the image store"""
        self.scope = None
        self.typeInfo['scope'] = 'scopetype'
        """the url of the image store"""
        self.url = None
        self.typeInfo['url'] = 'string'
        """the Zone ID of the image store"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'string'
        """the Zone name of the image store"""
        self.zonename = None
        self.typeInfo['zonename'] = 'string'
