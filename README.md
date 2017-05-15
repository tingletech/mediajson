
https://github.com/ucldc/ucldc-docs/wiki/media.json

https://github.com/ucldc/ucldc-docs/wiki/structMap-meeting

```python
from mediajson import MediaJson

s3url = 's3://bucket/key-media.json'

# the handy check_media method will check that deep harvest files in S3 exist
MediaJson(s3url).check_media()

# MediaJson is an iterator 
for node in MediaJson('path/to/file-media.json'):
    print(node.media)
```

the argument to MediaJson can be json, a dict, a file object, a local file path,
an s3:// url or an URL that can be opened by urlopen
