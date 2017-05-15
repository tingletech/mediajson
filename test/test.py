from unittest import TestCase

from mediajson import MediaJson

import json

MEDIA_JSON = """
{
    "label": "2002_0221_UCI_Dance_Visions",
    "href": "https://nuxeo.cdlib.org/nuxeo/nxbigfile/default/cdf1ceeb-37bc-4c83-8563-baaf1f7859a4/file:content/2002_0221_UCI_Dance_Visions.mp3",
    "id": "cdf1ceeb-37bc-4c83-8563-baaf1f7859a4",
    "format": "audio"
}
"""

class TestMediaJson(TestCase):
    def test_init_json(self):
        # init with json
        x = MediaJson(MEDIA_JSON)
        self.assertTrue(len(x.media) > 1)

    def test_init_dict(self):
        # init with dict
        x = MediaJson(json.loads(MEDIA_JSON))
        self.assertTrue(len(x.media) > 1)

    def test_init_path(self):
        # init with path to file
        x = MediaJson('test/cdf1ceeb-37bc-4c83-8563-baaf1f7859a4-media.json')
        self.assertTrue(len(x.media) > 1)

    def test_init_file(self):
        # init with open file
        with open('test/26c4ece6-7e0d-4b5b-9950-91c48a2d4140-media.json') as json_data:
            x = MediaJson(json_data)
            self.assertTrue(len(x.media) > 1)

    def test_init_http(self):
        x = MediaJson('https://s3.amazonaws.com/static.ucldc.cdlib.org/media_json/26c4ece6-7e0d-4b5b-9950-91c48a2d4140-media.json')
        self.assertTrue(len(x.media) > 1)

    def test_init_s3(self):
        x = MediaJson('s3://static.ucldc.cdlib.org/media_json/26c4ece6-7e0d-4b5b-9950-91c48a2d4140-media.json')
        self.assertTrue(len(x.media) > 1)

