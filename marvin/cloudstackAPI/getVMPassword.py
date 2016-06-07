"""Returns an encrypted password for the VM"""
from baseCmd import *
from baseResponse import *


class getVMPasswordCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """The ID of the virtual machine"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        self.required = ["id", ]


class getVMPasswordResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """The base64 encoded encrypted password of the VM"""
        self.encryptedpassword = None
        self.typeInfo['encryptedpassword'] = 'string'

