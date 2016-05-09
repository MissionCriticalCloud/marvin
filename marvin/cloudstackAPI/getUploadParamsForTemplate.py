"""upload an existing template into the CloudStack cloud."""
from baseCmd import *
from baseResponse import *
class getUploadParamsForTemplateCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """the display text of the template. This is usually used for display purposes."""
        """Required"""
        self.displaytext = None
        self.typeInfo['displaytext'] = 'string'
        """the format for the volume/template. Possible values include QCOW2, OVA, and VHD."""
        """Required"""
        self.format = None
        self.typeInfo['format'] = 'string'
        """the target hypervisor for the template"""
        """Required"""
        self.hypervisor = None
        self.typeInfo['hypervisor'] = 'string'
        """the name of the volume/template"""
        """Required"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the ID of the OS Type that best represents the OS of this template."""
        """Required"""
        self.ostypeid = None
        self.typeInfo['ostypeid'] = 'uuid'
        """the ID of the zone the volume/template is to be hosted on"""
        """Required"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'uuid'
        """an optional accountName. Must be used with domainId."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """32 or 64 bits support. 64 by default"""
        self.bits = None
        self.typeInfo['bits'] = 'integer'
        """the MD5 checksum value of this volume/template"""
        self.checksum = None
        self.typeInfo['checksum'] = 'string'
        """Template details in key/value pairs."""
        self.details = []
        self.typeInfo['details'] = 'map'
        """an optional domainId. If the account parameter is used, domainId must also be used."""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """true if template contains XS tools inorder to support dynamic scaling of VM cpu/memory"""
        self.isdynamicallyscalable = None
        self.typeInfo['isdynamicallyscalable'] = 'boolean'
        """true if the template or its derivatives are extractable; default is false"""
        self.isextractable = None
        self.typeInfo['isextractable'] = 'boolean'
        """true if this template is a featured template, false otherwise"""
        self.isfeatured = None
        self.typeInfo['isfeatured'] = 'boolean'
        """true if the template is available to all accounts; default is true"""
        self.ispublic = None
        self.typeInfo['ispublic'] = 'boolean'
        """true if the template type is routing i.e., if template is used to deploy router"""
        self.isrouting = None
        self.typeInfo['isrouting'] = 'boolean'
        """true if the template supports the password reset feature; default is false"""
        self.passwordenabled = None
        self.typeInfo['passwordenabled'] = 'boolean'
        """Upload volume/template for the project"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        """true if this template requires HVM"""
        self.requireshvm = None
        self.typeInfo['requireshvm'] = 'boolean'
        """true if the template supports the sshkey upload feature; default is false"""
        self.sshkeyenabled = None
        self.typeInfo['sshkeyenabled'] = 'boolean'
        """the tag for this template."""
        self.templatetag = None
        self.typeInfo['templatetag'] = 'string'
        self.required = ["displaytext","format","hypervisor","name","ostypeid","zoneid",]

class getUploadParamsForTemplateResponse (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the template/volume ID"""
        self.id = None
        self.typeInfo['id'] = 'uuid'
        """the timestamp after which the signature expires"""
        self.expires = None
        self.typeInfo['expires'] = 'string'
        """encrypted data to be sent in the POST request."""
        self.metadata = None
        self.typeInfo['metadata'] = 'string'
        """POST url to upload the file to"""
        self.postURL = None
        self.typeInfo['postURL'] = 'url'
        """signature to be sent in the POST request."""
        self.signature = None
        self.typeInfo['signature'] = 'string'

