"""Updates a VPC"""
from baseCmd import *
from baseResponse import *


class updateVPCCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """the id of the VPC"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """an optional field, in case you want to set a custom id to the resource. Allowed to Root Admins only"""
        self.customid = None
        self.typeInfo['customid'] = 'string'
        """the display text of the VPC"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """an optional field, whether to the display the vpc to the end user or not"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        """the name of the VPC"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """The new VPC offering ID to switch to. This will result in a restart+cleanup of the VPC"""
        self.vpcofferingid = None
        self.typeInfo['vpcofferingid'] = 'uuid'
        self.required = ["id", ]


class updateVPCResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the id of the VPC"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the owner of the VPC"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the cidr the VPC"""
        self.cidr = None
        self.typeInfo['cidr'] = 'string'
        """the date this VPC was created"""
        self.created = None
        self.typeInfo['created'] = 'date'
        """an alternate display text of the VPC."""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """is VPC uses distributed router for one hop forwarding and host based network ACL's"""
        self.distributedvpcrouter = None
        self.typeInfo['distributedvpcrouter'] = 'boolean'
        """the domain name of the owner"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain id of the VPC owner"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """is vpc for display to the regular user"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        """the name of the VPC"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the network domain of the VPC"""
        self.networkdomain = None
        self.typeInfo['networkdomain'] = 'string'
        """the project name of the VPC"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the project id of the VPC"""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'
        """if this VPC has redundant router"""
        self.redundantvpcrouter = None
        self.typeInfo['redundantvpcrouter'] = 'boolean'
        """true if VPC is region level"""
        self.regionlevelvpc = None
        self.typeInfo['regionlevelvpc'] = 'boolean'
        """true VPC requires restart"""
        self.restartrequired = None
        self.typeInfo['restartrequired'] = 'boolean'
        """state of the VPC. Can be Inactive/Enabled"""
        self.state = None
        self.typeInfo['state'] = 'string'
        """display text of the vpc offering the vpc is created from"""
        self.vpcofferingdisplaytext = None
        self.typeInfo['vpcofferingdisplaytext'] = 'string'
        """vpc offering id the VPC is created from"""
        self.vpcofferingid = None
        self.typeInfo['vpcofferingid'] = 'string'
        """name of the vpc offering the vpc is created from"""
        self.vpcofferingname = None
        self.typeInfo['vpcofferingname'] = 'string'
        """zone id of the vpc"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'string'
        """the name of the zone the VPC belongs to"""
        self.zonename = None
        self.typeInfo['zonename'] = 'string'
        """the list of networks belongign to the VPC"""
        self.network = []
        """the list of supported services"""
        self.service = []
        """the list of resource tags associated with the project"""
        self.tags = []

class capability:
    def __init__(self):
        """"can this service capability value can be choosable while creatine network offerings"""
        self.canchooseservicecapability = None
        """"the capability name"""
        self.name = None
        """"the capability value"""
        self.value = None

class provider:
    def __init__(self):
        """"uuid of the network provider"""
        self.id = None
        """"true if individual services can be enabled/disabled"""
        self.canenableindividualservice = None
        """"the destination physical network"""
        self.destinationphysicalnetworkid = None
        """"the provider name"""
        self.name = None
        """"the physical network this belongs to"""
        self.physicalnetworkid = None
        """"services for this provider"""
        self.servicelist = None
        """"state of the network provider"""
        self.state = None

class service:
    def __init__(self):
        """"the service name"""
        self.name = None
        """"the list of capabilities"""
        self.capability = []
        """"can this service capability value can be choosable while creatine network offerings"""
        self.canchooseservicecapability = None
        """"the capability name"""
        self.name = None
        """"the capability value"""
        self.value = None
        """"the service provider name"""
        self.provider = []
        """"uuid of the network provider"""
        self.id = None
        """"true if individual services can be enabled/disabled"""
        self.canenableindividualservice = None
        """"the destination physical network"""
        self.destinationphysicalnetworkid = None
        """"the provider name"""
        self.name = None
        """"the physical network this belongs to"""
        self.physicalnetworkid = None
        """"services for this provider"""
        self.servicelist = None
        """"state of the network provider"""
        self.state = None

class capability:
    def __init__(self):
        """"can this service capability value can be choosable while creatine network offerings"""
        self.canchooseservicecapability = None
        """"the capability name"""
        self.name = None
        """"the capability value"""
        self.value = None

class provider:
    def __init__(self):
        """"uuid of the network provider"""
        self.id = None
        """"true if individual services can be enabled/disabled"""
        self.canenableindividualservice = None
        """"the destination physical network"""
        self.destinationphysicalnetworkid = None
        """"the provider name"""
        self.name = None
        """"the physical network this belongs to"""
        self.physicalnetworkid = None
        """"services for this provider"""
        self.servicelist = None
        """"state of the network provider"""
        self.state = None

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

class network:
    def __init__(self):
        """"the id of the network"""
        self.id = None
        """"the owner of the network"""
        self.account = None
        """"ACL Id associated with the VPC network"""
        self.aclid = None
        """"acl type - access type to the network"""
        self.acltype = None
        """"Broadcast domain type of the network"""
        self.broadcastdomaintype = None
        """"broadcast uri of the network. This parameter is visible to ROOT admins only"""
        self.broadcasturi = None
        """"list networks available for vm deployment"""
        self.canusefordeploy = None
        """"Cloudstack managed address space, all CloudStack managed VMs get IP address from CIDR"""
        self.cidr = None
        """"an optional field, whether to the display the network to the end user or not."""
        self.displaynetwork = None
        """"the displaytext of the network"""
        self.displaytext = None
        """"the first DNS for the network"""
        self.dns1 = None
        """"the second DNS for the network"""
        self.dns2 = None
        """"the domain name of the network owner"""
        self.domain = None
        """"the domain id of the network owner"""
        self.domainid = None
        """"the network's gateway"""
        self.gateway = None
        """"the cidr of IPv6 network"""
        self.ip6cidr = None
        """"the gateway of IPv6 network"""
        self.ip6gateway = None
        """"true if network is default, false otherwise"""
        self.isdefault = None
        """"list networks that are persistent"""
        self.ispersistent = None
        """"true if network is system, false otherwise"""
        self.issystem = None
        """"the name of the network"""
        self.name = None
        """"the network's netmask"""
        self.netmask = None
        """"the network CIDR of the guest network configured with IP reservation. It is the summation of CIDR and RESERVED_IP_RANGE"""
        self.networkcidr = None
        """"the network domain"""
        self.networkdomain = None
        """"availability of the network offering the network is created from"""
        self.networkofferingavailability = None
        """"true if network offering is ip conserve mode enabled"""
        self.networkofferingconservemode = None
        """"display text of the network offering the network is created from"""
        self.networkofferingdisplaytext = None
        """"network offering id the network is created from"""
        self.networkofferingid = None
        """"name of the network offering the network is created from"""
        self.networkofferingname = None
        """"the physical network id"""
        self.physicalnetworkid = None
        """"the project name of the address"""
        self.project = None
        """"the project id of the ipaddress"""
        self.projectid = None
        """"related to what other network configuration"""
        self.related = None
        """"the network's IP range not to be used by CloudStack guest VMs and can be used for non CloudStack purposes"""
        self.reservediprange = None
        """"true network requires restart"""
        self.restartrequired = None
        """"true if network supports specifying ip ranges, false otherwise"""
        self.specifyipranges = None
        """"state of the network"""
        self.state = None
        """"true if network can span multiple zones"""
        self.strechedl2subnet = None
        """"true if users from subdomains can access the domain level network"""
        self.subdomainaccess = None
        """"the traffic type of the network"""
        self.traffictype = None
        """"the type of the network"""
        self.type = None
        """"The vlan of the network. This parameter is visible to ROOT admins only"""
        self.vlan = None
        """"VPC the network belongs to"""
        self.vpcid = None
        """"zone id of the network"""
        self.zoneid = None
        """"the name of the zone the network belongs to"""
        self.zonename = None
        """"If a network is enabled for 'streched l2 subnet' then represents zones on which network currently spans"""
        self.zonesnetworkspans = None
        """"the list of services"""
        self.service = []
        """"the service name"""
        self.name = None
        """"the list of capabilities"""
        self.capability = []
        """"can this service capability value can be choosable while creatine network offerings"""
        self.canchooseservicecapability = None
        """"the capability name"""
        self.name = None
        """"the capability value"""
        self.value = None
        """"the service provider name"""
        self.provider = []
        """"uuid of the network provider"""
        self.id = None
        """"true if individual services can be enabled/disabled"""
        self.canenableindividualservice = None
        """"the destination physical network"""
        self.destinationphysicalnetworkid = None
        """"the provider name"""
        self.name = None
        """"the physical network this belongs to"""
        self.physicalnetworkid = None
        """"services for this provider"""
        self.servicelist = None
        """"state of the network provider"""
        self.state = None
        """"the list of resource tags associated with network"""
        self.tags = []
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

class capability:
    def __init__(self):
        """"can this service capability value can be choosable while creatine network offerings"""
        self.canchooseservicecapability = None
        """"the capability name"""
        self.name = None
        """"the capability value"""
        self.value = None

class provider:
    def __init__(self):
        """"uuid of the network provider"""
        self.id = None
        """"true if individual services can be enabled/disabled"""
        self.canenableindividualservice = None
        """"the destination physical network"""
        self.destinationphysicalnetworkid = None
        """"the provider name"""
        self.name = None
        """"the physical network this belongs to"""
        self.physicalnetworkid = None
        """"services for this provider"""
        self.servicelist = None
        """"state of the network provider"""
        self.state = None

class service:
    def __init__(self):
        """"the service name"""
        self.name = None
        """"the list of capabilities"""
        self.capability = []
        """"can this service capability value can be choosable while creatine network offerings"""
        self.canchooseservicecapability = None
        """"the capability name"""
        self.name = None
        """"the capability value"""
        self.value = None
        """"the service provider name"""
        self.provider = []
        """"uuid of the network provider"""
        self.id = None
        """"true if individual services can be enabled/disabled"""
        self.canenableindividualservice = None
        """"the destination physical network"""
        self.destinationphysicalnetworkid = None
        """"the provider name"""
        self.name = None
        """"the physical network this belongs to"""
        self.physicalnetworkid = None
        """"services for this provider"""
        self.servicelist = None
        """"state of the network provider"""
        self.state = None

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

