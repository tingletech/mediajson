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

class TestJoke(TestCase):
    def test_init_json(self):
        x = MediaJson(MEDIA_JSON)
        self.assertTrue(len(x.media) > 1)

        x = MediaJson(json.loads(MEDIA_JSON))
        self.assertTrue(len(x.media) > 1)

        x = MediaJson('test/cdf1ceeb-37bc-4c83-8563-baaf1f7859a4-media.json')
        self.assertTrue(len(x.media) > 1)

