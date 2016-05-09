"""Lists all available disk offerings."""
from baseCmd import *
from baseResponse import *


class listDiskOfferingsCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """list only resources belonging to the domain specified"""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """ID of the disk offering"""
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
        """name of the disk offering"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        self.required = []


class listDiskOfferingsResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """unique ID of the disk offering"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the cache mode to use for this disk offering. none, writeback or writethrough"""
        self.cacheMode = None
        self.typeInfo['cacheMode'] = 'string'
        """the date this disk offering was created"""
        self.created = None
        self.typeInfo['created'] = 'date'
        """bytes read rate of the disk offering"""
        self.diskBytesReadRate = None
        self.typeInfo['diskBytesReadRate'] = 'long'
        """bytes write rate of the disk offering"""
        self.diskBytesWriteRate = None
        self.typeInfo['diskBytesWriteRate'] = 'long'
        """io requests read rate of the disk offering"""
        self.diskIopsReadRate = None
        self.typeInfo['diskIopsReadRate'] = 'long'
        """io requests write rate of the disk offering"""
        self.diskIopsWriteRate = None
        self.typeInfo['diskIopsWriteRate'] = 'long'
        """the size of the disk offering in GB"""
        self.disksize = None
        self.typeInfo['disksize'] = 'long'
        """whether to display the offering to the end user or not."""
        self.displayoffering = None
        self.typeInfo['displayoffering'] = 'boolean'
        """an alternate display text of the disk offering."""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """the domain name this disk offering belongs to. Ignore this information as it is not currently applicable."""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain ID this disk offering belongs to. Ignore this information as it is not currently applicable."""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """Hypervisor snapshot reserve space as a percent of a volume (for managed storage using Xen)"""
        self.hypervisorsnapshotreserve = None
        self.typeInfo['hypervisorsnapshotreserve'] = 'integer'
        """true if disk offering uses custom size, false otherwise"""
        self.iscustomized = None
        self.typeInfo['iscustomized'] = 'boolean'
        """true if disk offering uses custom iops, false otherwise"""
        self.iscustomizediops = None
        self.typeInfo['iscustomizediops'] = 'boolean'
        """the max iops of the disk offering"""
        self.maxiops = None
        self.typeInfo['maxiops'] = 'long'
        """the min iops of the disk offering"""
        self.miniops = None
        self.typeInfo['miniops'] = 'long'
        """the name of the disk offering"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """provisioning type used to create volumes. Valid values are thin, sparse, fat."""
        self.provisioningtype = None
        self.typeInfo['provisioningtype'] = 'string'
        """the storage type for this disk offering"""
        self.storagetype = None
        self.typeInfo['storagetype'] = 'string'
        """the tags for the disk offering"""
        self.tags = None
        self.typeInfo['tags'] = 'string'
