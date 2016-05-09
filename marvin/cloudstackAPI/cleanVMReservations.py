"""Cleanups VM reservations in the database."""
from baseCmd import *
from baseResponse import *


class cleanVMReservationsCmd(baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        self.required = []


class cleanVMReservationsResponse(baseResponse):
    typeInfo = {}

    def __init__(self):
        """any text associated with the success or failure"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """true if operation is executed successfully"""
        self.success = None
        self.typeInfo['success'] = 'boolean'
