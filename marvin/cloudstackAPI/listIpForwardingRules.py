"""List the IP forwarding rules"""
from baseCmd import *
from baseResponse import *


class listIpForwardingRulesCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """list resources by account. Must be used with the domainId parameter."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """list only resources belonging to the domain specified"""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """Lists rule with the specified ID."""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """list the rule belonging to this public IP address"""
        self.ipaddressid = None
        self.typeInfo['ipaddressid'] = 'uuid'
        """defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves."""
        self.isrecursive = None
        self.typeInfo['isrecursive'] = 'boolean'
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see. Default value is false"""
        self.listall = None
        self.typeInfo['listall'] = 'boolean'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        """list objects by project"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        """Lists all rules applied to the specified VM."""
        self.virtualmachineid = None
        self.typeInfo['virtualmachineid'] = 'uuid'
        self.required = []


class listIpForwardingRulesResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the ID of the port forwarding rule"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the cidr list to forward traffic from"""
        self.cidrlist = None
        self.typeInfo['cidrlist'] = 'string'
        """is firewall for display to the regular user"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        """the public ip address for the port forwarding rule"""
        self.ipaddress = None
        self.typeInfo['ipaddress'] = 'string'
        """the public ip address id for the port forwarding rule"""
        self.ipaddressid = None
        self.typeInfo['ipaddressid'] = 'string'
        """the id of the guest network the port forwarding rule belongs to"""
        self.networkid = None
        self.typeInfo['networkid'] = 'string'
        """the ending port of port forwarding rule's private port range"""
        self.privateendport = None
        self.typeInfo['privateendport'] = 'string'
        """the starting port of port forwarding rule's private port range"""
        self.privateport = None
        self.typeInfo['privateport'] = 'string'
        """the protocol of the port forwarding rule"""
        self.protocol = None
        self.typeInfo['protocol'] = 'string'
        """the ending port of port forwarding rule's private port range"""
        self.publicendport = None
        self.typeInfo['publicendport'] = 'string'
        """the starting port of port forwarding rule's public port range"""
        self.publicport = None
        self.typeInfo['publicport'] = 'string'
        """the state of the rule"""
        self.state = None
        self.typeInfo['state'] = 'string'
        """the VM display name for the port forwarding rule"""
        self.virtualmachinedisplayname = None
        self.typeInfo['virtualmachinedisplayname'] = 'string'
        """the VM ID for the port forwarding rule"""
        self.virtualmachineid = None
        self.typeInfo['virtualmachineid'] = 'string'
        """the VM name for the port forwarding rule"""
        self.virtualmachinename = None
        self.typeInfo['virtualmachinename'] = 'string'
        """the vm ip address for the port forwarding rule"""
        self.vmguestip = None
        self.typeInfo['vmguestip'] = 'string'
        """the list of resource tags associated with the rule"""
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

