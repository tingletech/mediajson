# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from builtins import open
from future import standard_library
standard_library.install_aliases()
from builtins import object
import json
from urllib.parse import urlparse
from urllib.request import urlopen
import boto3
from botocore.exceptions import ClientError

# get a `file_type` that will work with python 2 or python 3
# http://stackoverflow.com/a/36321030/1763984
import io
try:
    file_types = (file, io.IOBase)
except NameError:
    file_types = (io.IOBase,)

try:
    json_exception = json.JSONDecodeError
except AttributeError:
    json_exception = ValueError

class MediaJson(object):

    def __init__(self, mediainput):
        ## duck typing
        # take a 'dict'
        if type(mediainput) is dict:
            self.media = mediainput
        elif isinstance(mediainput, str):
            # if it is a basestring, check if it is json 
            try:
                self.media = json.loads(mediainput)
            # otherwise, try to parse it as a URI
            except json_exception:
                url = urlparse(mediainput)
                # local file
                if not url.scheme:
                    with open(mediainput) as json_data:
                        self.media = json.load(json_data)
                # s3
                elif url.scheme == 's3':
                    client = boto3.client('s3')
                    boto_object = client.get_object(
                        Bucket=url.netloc, Key=url.path.strip('/'))
                    self.media = json.load(boto_object['Body'])
                # other URLs
                else:
                    with urlopen(mediainput) as json_data:
                        self.media = json.load(json_data)

        # if a file type has been pased
        elif isinstance(mediainput, file_types):
            self.media = json.load(mediainput)

        else:
            raise ValueError('parameter must be json, file path, file object, or url')


    def __iter__(self):
        yield self.media
        for child in self.media.get('structMap'):
            yield child


    def check_media(self,
                    iiif_base='s3://ucldc-private-files/jp2000/',
                    media_base='s3://ucldc-nuxeo-ref-media/'):
        for node in self:
            self.check_node(node, iiif_base, media_base)


    def check_node(self, node, iiif_base, media_base):
        if node.get('format') == 'image':
            self.check_s3_object('{}{}'.format(iiif_base, node.get('id')))
        else:
            self.check_s3_object('{}{}'.format(media_base, node.get('id')))


    def check_s3_object(self, s3path):
        client = boto3.client('s3')
        url = urlparse(s3path)
        try:
            client.head_object(Bucket=url.netloc, Key=url.path.strip('/'))
        except ClientError:
            raise ValueError('{} not found'.format(s3path))

"""
Copyright © 2017, Regents of the University of California
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
- Redistributions of source code must retain the above copyright notice,
  this list of conditions and the following disclaimer.
- Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.
- Neither the name of the University of California nor the names of its
  contributors may be used to endorse or promote products derived from this
  software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
"""
