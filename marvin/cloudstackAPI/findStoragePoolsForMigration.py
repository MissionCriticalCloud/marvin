"""Lists storage pools available for migration of a volume."""
from baseCmd import *
from baseResponse import *
class findStoragePoolsForMigrationCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """the ID of the volume"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        self.required = ["id",]

class findStoragePoolsForMigrationResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the ID of the storage pool"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """IOPS CloudStack can provision from this storage pool"""
        self.capacityiops = None
        self.typeInfo['capacityiops'] = 'long'
        """the ID of the cluster for the storage pool"""
        self.clusterid = None
        self.typeInfo['clusterid'] = 'string'
        """the name of the cluster for the storage pool"""
        self.clustername = None
        self.typeInfo['clustername'] = 'string'
        """the date and time the storage pool was created"""
        self.created = None
        self.typeInfo['created'] = 'date'
        """the host's currently allocated disk size"""
        self.disksizeallocated = None
        self.typeInfo['disksizeallocated'] = 'long'
        """the total disk size of the storage pool"""
        self.disksizetotal = None
        self.typeInfo['disksizetotal'] = 'long'
        """the host's currently used disk size"""
        self.disksizeused = None
        self.typeInfo['disksizeused'] = 'long'
        """the hypervisor type of the storage pool"""
        self.hypervisor = None
        self.typeInfo['hypervisor'] = 'string'
        """the IP address of the storage pool"""
        self.ipaddress = None
        self.typeInfo['ipaddress'] = 'string'
        """the name of the storage pool"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the overprovisionfactor for the storage pool"""
        self.overprovisionfactor = None
        self.typeInfo['overprovisionfactor'] = 'string'
        """the storage pool path"""
        self.path = None
        self.typeInfo['path'] = 'string'
        """the Pod ID of the storage pool"""
        self.podid = None
        self.typeInfo['podid'] = 'string'
        """the Pod name of the storage pool"""
        self.podname = None
        self.typeInfo['podname'] = 'string'
        """the scope of the storage pool"""
        self.scope = None
        self.typeInfo['scope'] = 'string'
        """the state of the storage pool"""
        self.state = None
        self.typeInfo['state'] = 'storagepoolstatus'
        """the storage pool capabilities"""
        self.storagecapabilities = None
        self.typeInfo['storagecapabilities'] = 'map'
        """true if this pool is suitable to migrate a volume, false otherwise"""
        self.suitableformigration = None
        self.typeInfo['suitableformigration'] = 'boolean'
        """the tags for the storage pool"""
        self.tags = None
        self.typeInfo['tags'] = 'string'
        """the storage pool type"""
        self.type = None
        self.typeInfo['type'] = 'string'
        """the Zone ID of the storage pool"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'string'
        """the Zone name of the storage pool"""
        self.zonename = None
        self.typeInfo['zonename'] = 'string'
        """the ID of the latest async job acting on this object"""
        self.jobid = None
        self.typeInfo['jobid'] = ''
        """the current status of the latest async job acting on this object"""
        self.jobstatus = None
        self.typeInfo['jobstatus'] = ''

