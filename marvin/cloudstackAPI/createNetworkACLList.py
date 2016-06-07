"""Creates a network ACL for the given VPC"""
from baseCmd import *
from baseResponse import *


class createNetworkACLListCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """Name of the network ACL list"""
        """Required"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """ID of the VPC associated with this network ACL list"""
        """Required"""
        self.vpcid = None
        self.typeInfo['vpcid'] = 'uuid'
        """Description of the network ACL list"""
        self.description = None
        self.typeInfo['description'] = 'string'
        """an optional field, whether to the display the list to the end user or not"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        self.required = ["name", "vpcid", ]


class createNetworkACLListResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the ID of the ACL"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """Description of the ACL"""
        self.description = None
        self.typeInfo['description'] = 'string'
        """is ACL for display to the regular user"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        """the Name of the ACL"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """Id of the VPC this ACL is associated with"""
        self.vpcid = None
        self.typeInfo['vpcid'] = 'string'

