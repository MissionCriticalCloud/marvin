"""Extracts a template"""
from baseCmd import *
from baseResponse import *


class extractTemplateCmd (baseCmd):
    typeInfo = {}

    def __init__(self):
        self.isAsync = "true"
        """the ID of the template"""
        """Required"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """the mode of extraction - HTTP_DOWNLOAD or FTP_UPLOAD"""
        """Required"""
        self.mode = None
        self.typeInfo['mode'] = 'string'
        """the url to which the ISO would be extracted"""
        self.url = None
        self.typeInfo['url'] = 'string'
        """the ID of the zone where the ISO is originally located"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'uuid'
        self.required = ["id", "mode", ]


class extractTemplateResponse (baseResponse):
    typeInfo = {}

    def __init__(self):
        """the id of extracted object"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the account id to which the extracted object belongs"""
        self.accountid = None
        self.typeInfo['accountid'] = 'string'
        """the time and date the object was created"""
        self.created = None
        self.typeInfo['created'] = 'date'
        """the upload id of extracted object"""
        self.extractId = None
        self.typeInfo['extractId'] = 'string'
        """the mode of extraction - upload or download"""
        self.extractMode = None
        self.typeInfo['extractMode'] = 'string'
        """the name of the extracted object"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the state of the extracted object"""
        self.state = None
        self.typeInfo['state'] = 'string'
        """the status of the extraction"""
        self.status = None
        self.typeInfo['status'] = 'string'
        """type of the storage"""
        self.storagetype = None
        self.typeInfo['storagetype'] = 'string'
        """the percentage of the entity uploaded to the specified location"""
        self.uploadpercentage = None
        self.typeInfo['uploadpercentage'] = 'integer'
        """if mode = upload then url of the uploaded entity. if mode = download the url from which the entity can be downloaded"""
        self.url = None
        self.typeInfo['url'] = 'string'
        """zone ID the object was extracted from"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'string'
        """zone name the object was extracted from"""
        self.zonename = None
        self.typeInfo['zonename'] = 'string'

