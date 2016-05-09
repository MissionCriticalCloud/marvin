"""List Event Types"""
from baseCmd import *
from baseResponse import *


class listEventTypesCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        self.required = []


class listEventTypesResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """Event Type"""
        self.name = None
        self.typeInfo['name'] = 'string'
