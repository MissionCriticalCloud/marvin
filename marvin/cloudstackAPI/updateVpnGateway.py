"""Updates site to site vpn local gateway"""
from baseCmd import *
from baseResponse import *
class updateVpnGatewayCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "true"
        """id of customer gateway"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """an optional field, in case you want to set a custom id to the resource. Allowed to Root Admins only"""
        self.customid = None
        self.typeInfo['customid'] = 'string'
        """an optional field, whether to the display the vpn to the end user or not"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        self.required = ["id",]

class updateVpnGatewayResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the vpn gateway ID"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the owner"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the domain name of the owner"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain id of the owner"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """is vpn gateway for display to the regular user"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        """the project name"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the project id"""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'
        """the public IP address"""
        self.publicip = None
        self.typeInfo['publicip'] = 'string'
        """the date and time the host was removed"""
        self.removed = None
        self.typeInfo['removed'] = 'date'
        """the vpc id of this gateway"""
        self.vpcid = None
        self.typeInfo['vpcid'] = 'string'

