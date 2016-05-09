"""Creates a domain"""
from baseCmd import *
from baseResponse import *


class createDomainCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """creates domain with this name"""
        """Required"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """Domain UUID, required for adding domain from another Region"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """Network domain for networks in the domain"""
        self.networkdomain = None
        self.typeInfo['networkdomain'] = 'string'
        """assigns new domain a parent domain by domain ID of the parent.  If no parent domain is specied, the ROOT domain is assumed."""
        self.parentdomainid = None
        self.typeInfo['parentdomainid'] = 'uuid'
        self.required = ["name", ]


class createDomainResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """the ID of the domain"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the total number of cpu cores available to be created for this domain"""
        self.cpuavailable = None
        self.typeInfo['cpuavailable'] = 'string'
        """the total number of cpu cores the domain can own"""
        self.cpulimit = None
        self.typeInfo['cpulimit'] = 'string'
        """the total number of cpu cores owned by domain"""
        self.cputotal = None
        self.typeInfo['cputotal'] = 'long'
        """whether the domain has one or more sub-domains"""
        self.haschild = None
        self.typeInfo['haschild'] = 'boolean'
        """the total number of public ip addresses available for this domain to acquire"""
        self.ipavailable = None
        self.typeInfo['ipavailable'] = 'string'
        """the total number of public ip addresses this domain can acquire"""
        self.iplimit = None
        self.typeInfo['iplimit'] = 'string'
        """the total number of public ip addresses allocated for this domain"""
        self.iptotal = None
        self.typeInfo['iptotal'] = 'long'
        """the level of the domain"""
        self.level = None
        self.typeInfo['level'] = 'integer'
        """the total memory (in MB) available to be created for this domain"""
        self.memoryavailable = None
        self.typeInfo['memoryavailable'] = 'string'
        """the total memory (in MB) the domain can own"""
        self.memorylimit = None
        self.typeInfo['memorylimit'] = 'string'
        """the total memory (in MB) owned by domain"""
        self.memorytotal = None
        self.typeInfo['memorytotal'] = 'long'
        """the name of the domain"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the total number of networks available to be created for this domain"""
        self.networkavailable = None
        self.typeInfo['networkavailable'] = 'string'
        """the network domain"""
        self.networkdomain = None
        self.typeInfo['networkdomain'] = 'string'
        """the total number of networks the domain can own"""
        self.networklimit = None
        self.typeInfo['networklimit'] = 'string'
        """the total number of networks owned by domain"""
        self.networktotal = None
        self.typeInfo['networktotal'] = 'long'
        """the domain ID of the parent domain"""
        self.parentdomainid = None
        self.typeInfo['parentdomainid'] = 'string'
        """the domain name of the parent domain"""
        self.parentdomainname = None
        self.typeInfo['parentdomainname'] = 'string'
        """the path of the domain"""
        self.path = None
        self.typeInfo['path'] = 'string'
        """the total primary storage space (in GiB) available to be used for this domain"""
        self.primarystorageavailable = None
        self.typeInfo['primarystorageavailable'] = 'string'
        """the total primary storage space (in GiB) the domain can own"""
        self.primarystoragelimit = None
        self.typeInfo['primarystoragelimit'] = 'string'
        """the total primary storage space (in GiB) owned by domain"""
        self.primarystoragetotal = None
        self.typeInfo['primarystoragetotal'] = 'long'
        """the total number of projects available for administration by this domain"""
        self.projectavailable = None
        self.typeInfo['projectavailable'] = 'string'
        """the total number of projects the domain can own"""
        self.projectlimit = None
        self.typeInfo['projectlimit'] = 'string'
        """the total number of projects being administrated by this domain"""
        self.projecttotal = None
        self.typeInfo['projecttotal'] = 'long'
        """the total secondary storage space (in GiB) available to be used for this domain"""
        self.secondarystorageavailable = None
        self.typeInfo['secondarystorageavailable'] = 'string'
        """the total secondary storage space (in GiB) the domain can own"""
        self.secondarystoragelimit = None
        self.typeInfo['secondarystoragelimit'] = 'string'
        """the total secondary storage space (in GiB) owned by domain"""
        self.secondarystoragetotal = None
        self.typeInfo['secondarystoragetotal'] = 'long'
        """the total number of snapshots available for this domain"""
        self.snapshotavailable = None
        self.typeInfo['snapshotavailable'] = 'string'
        """the total number of snapshots which can be stored by this domain"""
        self.snapshotlimit = None
        self.typeInfo['snapshotlimit'] = 'string'
        """the total number of snapshots stored by this domain"""
        self.snapshottotal = None
        self.typeInfo['snapshottotal'] = 'long'
        """the state of the domain"""
        self.state = None
        self.typeInfo['state'] = 'string'
        """the total number of templates available to be created by this domain"""
        self.templateavailable = None
        self.typeInfo['templateavailable'] = 'string'
        """the total number of templates which can be created by this domain"""
        self.templatelimit = None
        self.typeInfo['templatelimit'] = 'string'
        """the total number of templates which have been created by this domain"""
        self.templatetotal = None
        self.typeInfo['templatetotal'] = 'long'
        """the total number of virtual machines available for this domain to acquire"""
        self.vmavailable = None
        self.typeInfo['vmavailable'] = 'string'
        """the total number of virtual machines that can be deployed by this domain"""
        self.vmlimit = None
        self.typeInfo['vmlimit'] = 'string'
        """the total number of virtual machines deployed by this domain"""
        self.vmtotal = None
        self.typeInfo['vmtotal'] = 'long'
        """the total volume available for this domain"""
        self.volumeavailable = None
        self.typeInfo['volumeavailable'] = 'string'
        """the total volume which can be used by this domain"""
        self.volumelimit = None
        self.typeInfo['volumelimit'] = 'string'
        """the total volume being used by this domain"""
        self.volumetotal = None
        self.typeInfo['volumetotal'] = 'long'
        """the total number of vpcs available to be created for this domain"""
        self.vpcavailable = None
        self.typeInfo['vpcavailable'] = 'string'
        """the total number of vpcs the domain can own"""
        self.vpclimit = None
        self.typeInfo['vpclimit'] = 'string'
        """the total number of vpcs owned by domain"""
        self.vpctotal = None
        self.typeInfo['vpctotal'] = 'long'
