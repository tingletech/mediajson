
https://github.com/ucldc/ucldc-docs/wiki/media.json

https://github.com/ucldc/ucldc-docs/wiki/structMap-meeting

```python
from mediajson import MediaJson
MediaJson(s3url).check_media()
```

the argument to MediaJson can be json, a dict, a file object, a local file path,
an s3:// url or an URL that can be opened by urlopen
