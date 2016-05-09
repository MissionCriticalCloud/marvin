"""Adds S3 Image Store"""
from baseCmd import *
from baseResponse import *
class addImageStoreS3Cmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """S3 access key"""
        """Required"""
        self.accesskey = None
        self.typeInfo['accesskey'] = 'string'
        """Name of the storage bucket"""
        """Required"""
        self.bucket = None
        self.typeInfo['bucket'] = 'string'
        """S3 endpoint"""
        """Required"""
        self.endpoint = None
        self.typeInfo['endpoint'] = 'string'
        """S3 secret key"""
        """Required"""
        self.secretkey = None
        self.typeInfo['secretkey'] = 'string'
        """Connection timeout (milliseconds)"""
        self.connectiontimeout = None
        self.typeInfo['connectiontimeout'] = 'integer'
        """Connection TTL (milliseconds)"""
        self.connectionttl = None
        self.typeInfo['connectionttl'] = 'integer'
        """Maximum number of times to retry on error"""
        self.maxerrorretry = None
        self.typeInfo['maxerrorretry'] = 'integer'
        """Signer Algorithm to use, either S3SignerType or AWSS3V4SignerType"""
        self.s3signer = None
        self.typeInfo['s3signer'] = 'string'
        """Socket timeout (milliseconds)"""
        self.sockettimeout = None
        self.typeInfo['sockettimeout'] = 'integer'
        """Use HTTPS instead of HTTP"""
        self.usehttps = None
        self.typeInfo['usehttps'] = 'boolean'
        """Whether TCP keep-alive is used"""
        self.usetcpkeepalive = None
        self.typeInfo['usetcpkeepalive'] = 'boolean'
        self.required = ["accesskey","bucket","endpoint","secretkey",]

class addImageStoreS3Response (baseResponse):
    typeInfo = {}
    def __init__(self):
        """the ID of the image store"""
        self.id = None
        self.typeInfo['id'] = 'string'
        """the details of the image store"""
        self.details = None
        self.typeInfo['details'] = 'set'
        """the name of the image store"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the protocol of the image store"""
        self.protocol = None
        self.typeInfo['protocol'] = 'string'
        """the provider name of the image store"""
        self.providername = None
        self.typeInfo['providername'] = 'string'
        """the scope of the image store"""
        self.scope = None
        self.typeInfo['scope'] = 'scopetype'
        """the url of the image store"""
        self.url = None
        self.typeInfo['url'] = 'string'
        """the Zone ID of the image store"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'string'
        """the Zone name of the image store"""
        self.zonename = None
        self.typeInfo['zonename'] = 'string'

