"""create secondary staging store."""
from baseCmd import *
from baseResponse import *


class createSecondaryStagingStoreCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """the URL for the staging store"""
        """Required"""
        self.url = None
        self.typeInfo['url'] = 'string'
        """the details for the staging store"""
        self.details = []
        self.typeInfo['details'] = 'map'
        """the staging store provider name"""
        self.provider = None
        self.typeInfo['provider'] = 'string'
        """the scope of the staging store: zone only for now"""
        self.scope = None
        self.typeInfo['scope'] = 'string'
        """the Zone ID for the staging store"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'uuid'
        self.required = ["url", ]


class createSecondaryStagingStoreResponse (baseResponse):
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

