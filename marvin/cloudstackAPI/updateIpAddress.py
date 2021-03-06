"""Updates an IP address"""
from baseCmd import *
from baseResponse import *


class updateIpAddressCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """the ID of the public IP address to update"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """an optional field, in case you want to set a custom id to the resource. Allowed to Root Admins only"""
        self.customid = None
        self.typeInfo['customid'] = 'string'
        """an optional field, whether to the display the IP to the end user or not"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        self.required = ["id", ]


class updateIpAddressResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """public IP address id"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the account the public IP address is associated with"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the ID of the ACL applied to this IP"""
        self.aclid = None
        self.typeInfo['aclid'] = 'string'
        """date the public IP address was acquired"""
        self.allocated = None
        self.typeInfo['allocated'] = 'date'
        """the ID of the Network associated with the IP address"""
        self.associatednetworkid = None
        self.typeInfo['associatednetworkid'] = 'string'
        """the name of the Network associated with the IP address"""
        self.associatednetworkname = None
        self.typeInfo['associatednetworkname'] = 'string'
        """the domain the public IP address is associated with"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain ID the public IP address is associated with"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """is public ip for display to the regular user"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        """the virtual network for the IP address"""
        self.forvirtualnetwork = None
        self.typeInfo['forvirtualnetwork'] = 'boolean'
        """public IP address"""
        self.ipaddress = None
        self.typeInfo['ipaddress'] = 'string'
        """is public IP portable across the zones"""
        self.isportable = None
        self.typeInfo['isportable'] = 'boolean'
        """true if the IP address is a source nat address, false otherwise"""
        self.issourcenat = None
        self.typeInfo['issourcenat'] = 'boolean'
        """true if this ip is for static nat, false otherwise"""
        self.isstaticnat = None
        self.typeInfo['isstaticnat'] = 'boolean'
        """true if this ip is system ip (was allocated as a part of deployVm or createLbRule)"""
        self.issystem = None
        self.typeInfo['issystem'] = 'boolean'
        """the ID of the Network where ip belongs to"""
        self.networkid = None
        self.typeInfo['networkid'] = 'string'
        """the physical network this belongs to"""
        self.physicalnetworkid = None
        self.typeInfo['physicalnetworkid'] = 'string'
        """the project name of the address"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the project id of the ipaddress"""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'
        """purpose of the IP address. In Acton this value is not null for Ips with isSystem=true, and can have either StaticNat or LB value"""
        self.purpose = None
        self.typeInfo['purpose'] = 'string'
        """State of the ip address. Can be: Allocatin, Allocated and Releasing"""
        self.state = None
        self.typeInfo['state'] = 'string'
        """virutal machine display name the ip address is assigned to (not null only for static nat Ip)"""
        self.virtualmachinedisplayname = None
        self.typeInfo['virtualmachinedisplayname'] = 'string'
        """virutal machine id the ip address is assigned to (not null only for static nat Ip)"""
        self.virtualmachineid = None
        self.typeInfo['virtualmachineid'] = 'string'
        """virutal machine name the ip address is assigned to (not null only for static nat Ip)"""
        self.virtualmachinename = None
        self.typeInfo['virtualmachinename'] = 'string'
        """the ID of the VLAN associated with the IP address. This parameter is visible to ROOT admins only"""
        self.vlanid = None
        self.typeInfo['vlanid'] = 'string'
        """the VLAN associated with the IP address"""
        self.vlanname = None
        self.typeInfo['vlanname'] = 'string'
        """virutal machine (dnat) ip address (not null only for static nat Ip)"""
        self.vmipaddress = None
        self.typeInfo['vmipaddress'] = 'string'
        """VPC the ip belongs to"""
        self.vpcid = None
        self.typeInfo['vpcid'] = 'string'
        """the ID of the zone the public IP address belongs to"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'string'
        """the name of the zone the public IP address belongs to"""
        self.zonename = None
        self.typeInfo['zonename'] = 'string'
        """the list of resource tags associated with ip address"""
        self.tags = []
        """the ID of the latest async job acting on this object"""
        self.jobid = None
        self.typeInfo['jobid'] = ''
        """the current status of the latest async job acting on this object"""
        self.jobstatus = None
        self.typeInfo['jobstatus'] = ''

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

