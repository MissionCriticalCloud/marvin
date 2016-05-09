"""Logs out the user"""
from baseCmd import *
from baseResponse import *


class logoutCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        self.required = []


class logoutResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """Response description"""
        self.description = None
        self.typeInfo['description'] = 'string'
