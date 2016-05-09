"""Updates the snapshot policy."""
from baseCmd import *
from baseResponse import *
class updateSnapshotPolicyCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "true"
        """an optional field, in case you want to set a custom id to the resource. Allowed to Root Admins only"""
        self.customid = None
        self.typeInfo['customid'] = 'string'
        """an optional field, whether to the display the snapshot policy to the end user or not."""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        """the ID of the snapshot policy"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        self.required = []

class updateSnapshotPolicyResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the ID of the snapshot policy"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """is this policy for display to the regular user"""
        self.fordisplay = None
        self.typeInfo['fordisplay'] = 'boolean'
        """the interval type of the snapshot policy"""
        self.intervaltype = None
        self.typeInfo['intervaltype'] = 'short'
        """maximum number of snapshots retained"""
        self.maxsnaps = None
        self.typeInfo['maxsnaps'] = 'int'
        """time the snapshot is scheduled to be taken."""
        self.schedule = None
        self.typeInfo['schedule'] = 'string'
        """the time zone of the snapshot policy"""
        self.timezone = None
        self.typeInfo['timezone'] = 'string'
        """the ID of the disk volume"""
        self.volumeid = None
        self.typeInfo['volumeid'] = 'string'

