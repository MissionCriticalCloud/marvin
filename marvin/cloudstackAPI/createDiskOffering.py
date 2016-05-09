"""Creates a disk offering."""
from baseCmd import *
from baseResponse import *
class createDiskOfferingCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """alternate display text of the disk offering"""
        """Required"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """name of the disk offering"""
        """Required"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """bytes read rate of the disk offering"""
        self.bytesreadrate = None
        self.typeInfo['bytesreadrate'] = 'long'
        """bytes write rate of the disk offering"""
        self.byteswriterate = None
        self.typeInfo['byteswriterate'] = 'long'
        """whether disk offering size is custom or not"""
        self.customized = None
        self.typeInfo['customized'] = 'boolean'
        """whether disk offering iops is custom or not"""
        self.customizediops = None
        self.typeInfo['customizediops'] = 'boolean'
        """size of the disk offering in GB (1GB = 1,073,741,824 bytes)"""
        self.disksize = None
        self.typeInfo['disksize'] = 'long'
        """an optional field, whether to display the offering to the end user or not."""
        self.displayoffering = None
        self.typeInfo['displayoffering'] = 'boolean'
        """the ID of the containing domain, null for public offerings"""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """Hypervisor snapshot reserve space as a percent of a volume (for managed storage using Xen)"""
        self.hypervisorsnapshotreserve = None
        self.typeInfo['hypervisorsnapshotreserve'] = 'integer'
        """io requests read rate of the disk offering"""
        self.iopsreadrate = None
        self.typeInfo['iopsreadrate'] = 'long'
        """io requests write rate of the disk offering"""
        self.iopswriterate = None
        self.typeInfo['iopswriterate'] = 'long'
        """max iops of the disk offering"""
        self.maxiops = None
        self.typeInfo['maxiops'] = 'long'
        """min iops of the disk offering"""
        self.miniops = None
        self.typeInfo['miniops'] = 'long'
        """provisioning type used to create volumes. Valid values are thin, sparse, fat."""
        self.provisioningtype = None
        self.typeInfo['provisioningtype'] = 'string'
        """the storage type of the disk offering. Values are local and shared."""
        self.storagetype = None
        self.typeInfo['storagetype'] = 'string'
        """tags for the disk offering"""
        self.tags = None
        self.typeInfo['tags'] = 'string'
        self.required = ["displaytext","name",]

class createDiskOfferingResponse (baseResponse):
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

