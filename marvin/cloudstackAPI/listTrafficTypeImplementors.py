"""Lists implementors of implementor of a network traffic type or implementors of all network traffic types"""
from baseCmd import *
from baseResponse import *


class listTrafficTypeImplementorsCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        """Optional. The network traffic type, if specified, return its implementor. Otherwise, return all traffic types with their implementor"""
        self.traffictype = None
        self.typeInfo['traffictype'] = 'string'
        self.required = []


class listTrafficTypeImplementorsResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """network traffic type"""
        self.traffictype = None
        self.typeInfo['traffictype'] = 'string'
        """implementor of network traffic type"""
        self.traffictypeimplementor = None
        self.typeInfo['traffictypeimplementor'] = 'string'

