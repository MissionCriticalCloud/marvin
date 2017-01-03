"""List private gateways"""
from baseCmd import *
from baseResponse import *


class listPrivateGatewaysCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """list only resources belonging to the domain specified"""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """list private gateway by IP"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """list gateways by IP address"""
        self.ipaddress = None
        self.typeInfo['ipaddress'] = 'string'
        """defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves."""
        self.isrecursive = None
        self.typeInfo['isrecursive'] = 'boolean'
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see. Default value is false"""
        self.listall = None
        self.typeInfo['listall'] = 'boolean'
        """list gateways by network ID"""
        self.networkid = None
        self.typeInfo['networkid'] = 'string'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        """list objects by project"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        """list gateways by state"""
        self.state = None
        self.typeInfo['state'] = 'string'
        """list gateways by VPC"""
        self.vpcid = None
        self.typeInfo['vpcid'] = 'uuid'
        self.required = []


class listPrivateGatewaysResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the id of the private gateway"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the account associated with the private gateway"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """ACL Id set for private gateway"""
        self.aclid = None
        self.typeInfo['aclid'] = 'string'
        """the CIDR of the private network"""
        self.cidr = None
        self.typeInfo['cidr'] = 'string'
        """the domain associated with the private gateway"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the ID of the domain associated with the private gateway"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """the private gateway's ip address"""
        self.ipaddress = None
        self.typeInfo['ipaddress'] = 'string'
        """the network id"""
        self.networkid = None
        self.typeInfo['networkid'] = 'string'
        """the network name"""
        self.networkname = None
        self.typeInfo['networkname'] = 'string'
        """the project name of the private gateway"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the project id of the private gateway"""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'
        """Souce Nat enable status"""
        self.sourcenatsupported = None
        self.typeInfo['sourcenatsupported'] = 'boolean'
        """State of the gateway, can be Creating, Ready, Deleting"""
        self.state = None
        self.typeInfo['state'] = 'string'
        """the network implementation uri for the private gateway"""
        self.vlan = None
        self.typeInfo['vlan'] = 'string'
        """VPC the private gateaway belongs to"""
        self.vpcid = None
        self.typeInfo['vpcid'] = 'string'
        """zone id of the private gateway"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'string'
        """the name of the zone the private gateway belongs to"""
        self.zonename = None
        self.typeInfo['zonename'] = 'string'

