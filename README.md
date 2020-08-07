# nopy.to-client
Client written in Python for nopy.to.

## Usage
Import and instantiate it.
```python
from nopy.client import Client
# Optionally import exceptions, too.
from nopy.exceptions import *


client = Client()
```

Get a file's metadata.
```python
url = "https://nopy.to/20eMxZbq/test_file.zip"
data = client.get_file_meta(url)
```

Response:
```json
{
   "filename": "test_file.zip",
   "fid": "ad7b11bc2f53567115d2e1275e92fb1406f15e0c1b0a112e1510d384847173d7",
   "size": "7.3GB",
   "raw_size": "7833606696",
   "hash": "9a1f6c009034431c90ae1ab1a226f3fcea210aa3",
   "date": "2019-11-11",
   "uploader": {
      "img": "f95zone",
      "url": "https://f95zone.to"
   },
   "request": "5f2t14a1994a2961737856",
   "session": "dw923f2cb4d1c5bd3915bd296e0b0b60cb923a066963af9db0a28f68a18715e3",
   "error_fatal": false,
   "errors": [

   ],
   "file_url": "https://server12.files.nopy.to/1596814729/YCq6jeuEWmKDsxIC9gbsZQ/ae7b41bc8f51567115e2e1275e92fb1406f15g0c1b0a112e1570d384847173d7/test_file.zip?s=6bf6e2df1ax46c84f6d8f9f1e385c3bb2a4bde6e"
}
```

## Exceptions
|Class|Info|
| --- | --- |
|BadResponseError|The API didn't return a 200.
|InvalidURLError|URL failed the regex check.
|NotAuthenticatedError|An attempt to upload a file was made without being logged in.
