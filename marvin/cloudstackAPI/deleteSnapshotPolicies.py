"""Deletes snapshot policies for the account."""
from baseCmd import *
from baseResponse import *


class deleteSnapshotPoliciesCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """the Id of the snapshot policy"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """list of snapshots policy IDs separated by comma"""
        self.ids = []
        self.typeInfo['ids'] = 'list'
        self.required = []


class deleteSnapshotPoliciesResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'
