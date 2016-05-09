"""Adds metric counter"""
from baseCmd import *
from baseResponse import *


class createCounterCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """Name of the counter."""
        """Required"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """Source of the counter."""
        """Required"""
        self.source = None
        self.typeInfo['source'] = 'string'
        """Value of the counter e.g. oid in case of snmp."""
        """Required"""
        self.value = None
        self.typeInfo['value'] = 'string'
        self.required = ["name", "source", "value", ]


class createCounterResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """the id of the Counter"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """Name of the counter."""
        self.name = None
        self.typeInfo['name'] = 'string'
        """Source of the counter."""
        self.source = None
        self.typeInfo['source'] = 'string'
        """Value in case of snmp or other specific counters."""
        self.value = None
        self.typeInfo['value'] = 'string'
        """zone id of counter"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'string'
