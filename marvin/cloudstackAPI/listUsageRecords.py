"""Lists usage records for accounts"""
from baseCmd import *
from baseResponse import *


class listUsageRecordsCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "false"
        """End date range for usage record query (use format "yyyy-MM-dd" or the new format "yyyy-MM-dd HH:mm:ss", e.g. startDate=2015-01-01 or startdate=2015-01-01 10:30:00)."""
        """Required"""
        self.enddate = None
        self.typeInfo['enddate'] = 'date'
        """Start date range for usage record query (use format "yyyy-MM-dd" or the new format "yyyy-MM-dd HH:mm:ss", e.g. startDate=2015-01-01 or startdate=2015-01-01 11:00:00)."""
        """Required"""
        self.startdate = None
        self.typeInfo['startdate'] = 'date'
        """List usage records for the specified user."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """List usage records for the specified account"""
        self.accountid = None
        self.typeInfo['accountid'] = 'uuid'
        """List usage records for the specified domain."""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """List by keyword"""
        self.keyword = None
        self.typeInfo['keyword'] = 'string'
        """"""
        self.page = None
        self.typeInfo['page'] = 'integer'
        """"""
        self.pagesize = None
        self.typeInfo['pagesize'] = 'integer'
        """List usage records for specified project"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        """List usage records for the specified usage type"""
        self.type = None
        self.typeInfo['type'] = 'long'
        """List usage records for the specified usage UUID. Can be used only together with TYPE parameter."""
        self.usageid = None
        self.typeInfo['usageid'] = 'string'
        self.required = ["enddate", "startdate", ]


class listUsageRecordsResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the user account name"""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the user account Id"""
        self.accountid = None
        self.typeInfo['accountid'] = 'string'
        """number of cpu of resource"""
        self.cpunumber = None
        self.typeInfo['cpunumber'] = 'long'
        """speed of each cpu of resource"""
        self.cpuspeed = None
        self.typeInfo['cpuspeed'] = 'long'
        """description of the usage record"""
        self.description = None
        self.typeInfo['description'] = 'string'
        """the domain the resource is associated with"""
        self.domain = None
        self.typeInfo['domain'] = 'string'
        """the domain ID"""
        self.domainid = None
        self.typeInfo['domainid'] = 'string'
        """end date of the usage record"""
        self.enddate = None
        self.typeInfo['enddate'] = 'string'
        """True if the resource is default"""
        self.isdefault = None
        self.typeInfo['isdefault'] = 'boolean'
        """True if the IPAddress is source NAT"""
        self.issourcenat = None
        self.typeInfo['issourcenat'] = 'boolean'
        """True if the IPAddress is system IP - allocated during vm deploy or lb rule create"""
        self.issystem = None
        self.typeInfo['issystem'] = 'boolean'
        """memory allocated for the resource"""
        self.memory = None
        self.typeInfo['memory'] = 'long'
        """virtual machine name"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """id of the network"""
        self.networkid = None
        self.typeInfo['networkid'] = 'string'
        """offering ID"""
        self.offeringid = None
        self.typeInfo['offeringid'] = 'string'
        """the project name of the resource"""
        self.project = None
        self.typeInfo['project'] = 'string'
        """the project id of the resource"""
        self.projectid = None
        self.typeInfo['projectid'] = 'string'
        """raw usage in hours"""
        self.rawusage = None
        self.typeInfo['rawusage'] = 'string'
        """resource size"""
        self.size = None
        self.typeInfo['size'] = 'long'
        """start date of the usage record"""
        self.startdate = None
        self.typeInfo['startdate'] = 'string'
        """template ID"""
        self.templateid = None
        self.typeInfo['templateid'] = 'string'
        """resource type"""
        self.type = None
        self.typeInfo['type'] = 'string'
        """usage in hours"""
        self.usage = None
        self.typeInfo['usage'] = 'string'
        """id of the resource"""
        self.usageid = None
        self.typeInfo['usageid'] = 'string'
        """usage type ID"""
        self.usagetype = None
        self.typeInfo['usagetype'] = 'integer'
        """virtual machine ID"""
        self.virtualmachineid = None
        self.typeInfo['virtualmachineid'] = 'string'
        """virtual size of resource"""
        self.virtualsize = None
        self.typeInfo['virtualsize'] = 'long'
        """the zone ID"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'string'

