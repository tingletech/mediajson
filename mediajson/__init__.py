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
                if not url.scheme:
                    with open(mediainput) as json_data:
                        self.media = json.load(json_data)
                else:
                    print('{} not supported yet'.format(url.scheme))
        # if a file type has been pased
        elif isinstance(mediainput, file_types):
            self.media = json.load(mediainput)


    def __iter__(self):
        yield self.media
        for child in self.media.get('structMap'):
            yield child
