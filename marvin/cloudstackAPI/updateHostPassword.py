"""Update password of a host/pool on management server."""
from baseCmd import *
from baseResponse import *
class updateHostPasswordCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """the new password for the host/cluster"""
        """Required"""
        self.password = None
        self.typeInfo['password'] = 'string'
        """the username for the host/cluster"""
        """Required"""
        self.username = None
        self.typeInfo['username'] = 'string'
        """the cluster ID"""
        self.clusterid = None
        self.typeInfo['clusterid'] = 'uuid'
        """the host ID"""
        self.hostid = None
        self.typeInfo['hostid'] = 'uuid'
        """if the password should also be updated on the hosts"""
        self.update_passwd_on_host = None
        self.typeInfo['update_passwd_on_host'] = 'boolean'
        self.required = ["password","username",]

class updateHostPasswordResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'

