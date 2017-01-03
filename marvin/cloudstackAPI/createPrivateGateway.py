"""Creates a private gateway"""
from baseCmd import *
from baseResponse import *


class createPrivateGatewayCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """the IP address of the Private gateaway"""
        """Required"""
        self.ipaddress = None
        self.typeInfo['ipaddress'] = 'string'
        """the uuid of the private network to use for the private gateway"""
        """Required"""
        self.networkid = None
        self.typeInfo['networkid'] = 'uuid'
        """the VPC network belongs to"""
        """Required"""
        self.vpcid = None
        self.typeInfo['vpcid'] = 'uuid'
        """the ID of the network ACL"""
        self.aclid = None
        self.typeInfo['aclid'] = 'uuid'
        """the gateway of the Private gateway (DEPRECATED!)."""
        self.gateway = None
        self.typeInfo['gateway'] = 'string'
        """the netmask of the Private gateway (DEPRECATED!)."""
        self.netmask = None
        self.typeInfo['netmask'] = 'string'
        """source NAT supported value. Default value false. If 'true' source NAT is enabled on the private gateway 'false': sourcenat is not supported"""
        self.sourcenatsupported = None
        self.typeInfo['sourcenatsupported'] = 'boolean'
        self.required = ["ipaddress", "networkid", "vpcid", ]


class createPrivateGatewayResponse (baseResponse):
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

