"""Adds backup image store."""
from baseCmd import *
from baseResponse import *


class addImageStoreCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """the image store provider name"""
        """Required"""
        self.provider = None
        self.typeInfo['provider'] = 'string'
        """the details for the image store. Example: details[0].key=accesskey&details[0].value=s389ddssaa&details[1].key=secretkey&details[1].value=8dshfsss"""
        self.details = []
        self.typeInfo['details'] = 'map'
        """the name for the image store"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the URL for the image store"""
        self.url = None
        self.typeInfo['url'] = 'string'
        """the Zone ID for the image store"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'uuid'
        self.required = ["provider", ]


class addImageStoreResponse (baseResponse):
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

