"""Lists all available service offerings."""
from baseCmd import *
from baseResponse import *


class listServiceOfferingsCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """list only resources belonging to the domain specified"""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """ID of the service offering"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """defaults to false, but if true, lists all resources from the parent specified by the domainId till leaves."""
        self.isrecursive = None
        self.typeInfo['isrecursive'] = 'boolean'
        """is this a system vm offering"""
        self.issystem = None
        self.typeInfo['issystem'] = 'boolean'
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """If set to false, list only resources belonging to the command's caller; if set to true - list resources that the caller is authorized to see. Default value is false"""
        self.listall = None
        self.typeInfo['listall'] = 'boolean'
        """name of the service offering"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        """the system VM type. Possible types are "consoleproxy", "secondarystoragevm" or "domainrouter"."""
        self.systemvmtype = None
        self.typeInfo['systemvmtype'] = 'string'
        """the ID of the virtual machine. Pass this in if you want to see the available service offering that a virtual machine can be changed to."""
        self.virtualmachineid = None
        self.typeInfo['virtualmachineid'] = 'uuid'
        self.required = []


class listServiceOfferingsResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the id of the service offering"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the number of CPU"""
        self.cpunumber = None
        self.typeInfo['cpunumber'] = 'integer'
        """the clock rate CPU speed in Mhz"""
        self.cpuspeed = None
        self.typeInfo['cpuspeed'] = 'integer'
        """the date this service offering was created"""
        self.created = None
        self.typeInfo['created'] = 'date'
        """is this a  default system vm offering"""
        self.defaultuse = None
        self.typeInfo['defaultuse'] = 'boolean'
        """deployment strategy used to deploy VM."""
        self.deploymentplanner = None
        self.typeInfo['deploymentplanner'] = 'string'
        """bytes read rate of the service offering"""
        self.diskBytesReadRate = None
        self.typeInfo['diskBytesReadRate'] = 'long'
        """bytes write rate of the service offering"""
        self.diskBytesWriteRate = None
        self.typeInfo['diskBytesWriteRate'] = 'long'
        """io requests read rate of the service offering"""
        self.diskIopsReadRate = None
        self.typeInfo['diskIopsReadRate'] = 'long'
        """io requests write rate of the service offering"""
        self.diskIopsWriteRate = None
        self.typeInfo['diskIopsWriteRate'] = 'long'
        """an alternate display text of the service offering."""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """Domain name for the offering"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain id of the service offering"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """the host tag for the service offering"""
        self.hosttags = None
        self.typeInfo['hosttags'] = 'string'
        """Hypervisor snapshot reserve space as a percent of a volume (for managed storage using Xen)"""
        self.hypervisorsnapshotreserve = None
        self.typeInfo['hypervisorsnapshotreserve'] = 'integer'
        """is true if the offering is customized"""
        self.iscustomized = None
        self.typeInfo['iscustomized'] = 'boolean'
        """true if disk offering uses custom iops, false otherwise"""
        self.iscustomizediops = None
        self.typeInfo['iscustomizediops'] = 'boolean'
        """is this a system vm offering"""
        self.issystem = None
        self.typeInfo['issystem'] = 'boolean'
        """true if the vm needs to be volatile, i.e., on every reboot of vm from API root disk is discarded and creates a new root disk"""
        self.isvolatile = None
        self.typeInfo['isvolatile'] = 'boolean'
        """restrict the CPU usage to committed service offering"""
        self.limitcpuuse = None
        self.typeInfo['limitcpuuse'] = 'boolean'
        """the max iops of the disk offering"""
        self.maxiops = None
        self.typeInfo['maxiops'] = 'long'
        """the memory in MB"""
        self.memory = None
        self.typeInfo['memory'] = 'integer'
        """the min iops of the disk offering"""
        self.miniops = None
        self.typeInfo['miniops'] = 'long'
        """the name of the service offering"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """data transfer rate in megabits per second allowed."""
        self.networkrate = None
        self.typeInfo['networkrate'] = 'integer'
        """the ha support in the service offering"""
        self.offerha = None
        self.typeInfo['offerha'] = 'boolean'
        """provisioning type used to create volumes. Valid values are thin, sparse, fat."""
        self.provisioningtype = None
        self.typeInfo['provisioningtype'] = 'string'
        """additional key/value details tied with this service offering"""
        self.serviceofferingdetails = None
        self.typeInfo['serviceofferingdetails'] = 'map'
        """the storage type for this service offering"""
        self.storagetype = None
        self.typeInfo['storagetype'] = 'string'
        """is this a the systemvm type for system vm offering"""
        self.systemvmtype = None
        self.typeInfo['systemvmtype'] = 'string'
        """the tags for the service offering"""
        self.tags = None
        self.typeInfo['tags'] = 'string'

