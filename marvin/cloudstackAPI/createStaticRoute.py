"""Creates a static route"""
from baseCmd import *
from baseResponse import *


class createStaticRouteCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """The CIDR to create the static route for"""
        """Required"""
        self.cidr = None
        self.typeInfo['cidr'] = 'string'
        """IP address of the nexthop to route the CIDR to"""
        """Required"""
        self.nexthop = None
        self.typeInfo['nexthop'] = 'string'
        """The VPC id we are creating static route for."""
        """Required"""
        self.vpcid = None
        self.typeInfo['vpcid'] = 'uuid'
        """The private gateway id to get the ipaddress from (DEPRECATED!)."""
        self.gatewayid = None
        self.typeInfo['gatewayid'] = 'uuid'
        self.required = ["cidr", "nexthop", "vpcid", ]


class createStaticRouteResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the ID of static route"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the account associated with the static route"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """The CIDR to route"""
        self.cidr = None
        self.typeInfo['cidr'] = 'string'
        """the domain associated with the static route"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the ID of the domain associated with the static route"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """Gateway ip address the CIDR is routed to"""
        self.nexthop = None
        self.typeInfo['nexthop'] = 'string'
        """the project name of the static route"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the project id of the static route"""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'
        """the state of the static route"""
        self.state = None
        self.typeInfo['state'] = 'string'
        """VPC the static route belongs to"""
        self.vpcid = None
        self.typeInfo['vpcid'] = 'string'
        """the list of resource tags associated with static route"""
        self.tags = []

class tags:
    def __init__(self):
        """"the account associated with the tag"""
        self.account = None
        """"customer associated with the tag"""
        self.customer = None
        """"the domain associated with the tag"""
        self.domain = None
        """"the ID of the domain associated with the tag"""
        self.domainid = None
        """"tag key name"""
        self.key = None
        """"the project name where tag belongs to"""
        self.project = None
        """"the project id the tag belongs to"""
        self.projectid = None
        """"id of the resource"""
        self.resourceid = None
        """"resource type"""
        self.resourcetype = None
        """"tag value"""
        self.value = None

