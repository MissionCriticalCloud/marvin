"""Lists all static routes"""
from baseCmd import *
from baseResponse import *


class listStaticRoutesCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """list static routes by cidr"""
        self.cidr = None
        self.typeInfo['cidr'] = 'string'
        """list only resources belonging to the domain specified"""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """list static routes by gateway id (DEPRECATED!)"""
        self.gatewayid = None
        self.typeInfo['gatewayid'] = 'uuid'
        """list static route by id"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves."""
        self.isrecursive = None
        self.typeInfo['isrecursive'] = 'boolean'
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see. Default value is false"""
        self.listall = None
        self.typeInfo['listall'] = 'boolean'
        """list static routes by nexthop ip address"""
        self.nexthop = None
        self.typeInfo['nexthop'] = 'string'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        """list objects by project"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        """List resources by tags (key/value pairs)"""
        self.tags = []
        self.typeInfo['tags'] = 'map'
        """list static routes by vpc id"""
        self.vpcid = None
        self.typeInfo['vpcid'] = 'uuid'
        self.required = []


class listStaticRoutesResponse (baseResponse):
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

