# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.


"""Upload a data disk to the cloudstack cloud."""
from baseCmd import *
from baseResponse import *
class getUploadParamsForVolumeCmd (baseCmd):
    typeInfo = {}
    def __init__(self):
        self.isAsync = "false"
        """the format for the volume/template. Possible values include QCOW2, OVA, and VHD."""
        """Required"""
        self.format = None
        self.typeInfo['format'] = 'string'
        """the name of the volume/template"""
        """Required"""
        self.name = None
        self.typeInfo['name'] = 'string'
        """the ID of the zone the volume/template is to be hosted on"""
        """Required"""
        self.zoneid = None
        self.typeInfo['zoneid'] = 'uuid'
        """an optional accountName. Must be used with domainId."""
        self.account = None
        self.typeInfo['account'] = 'string'
        """the MD5 checksum value of this volume/template"""
        self.checksum = None
        self.typeInfo['checksum'] = 'string'
        """the ID of the disk offering. This must be a custom sized offering since during upload of volume/template size is unknown."""
        self.diskofferingid = None
        self.typeInfo['diskofferingid'] = 'uuid'
        """an optional domainId. If the account parameter is used, domainId must also be used."""
        self.domainid = None
        self.typeInfo['domainid'] = 'uuid'
        """Image store uuid"""
        self.imagestoreuuid = None
        self.typeInfo['imagestoreuuid'] = 'string'
        """Upload volume/template for the project"""
        self.projectid = None
        self.typeInfo['projectid'] = 'uuid'
        self.required = ["format","name","zoneid",]

class getUploadParamsForVolumeResponse (baseResponse):
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

