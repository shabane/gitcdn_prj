# how to use this api in python

first we need *requests* library. installed it with `pip3 install requests`.
then we use the api, in this example we use the local server to test the api.
file should be a tuple, whitch the first index indicate the name of file, and the second index is the binary of the file.
an impotant thing is that we should use the **Http Pos** method.

### Example code

```python
import requests

with open('Screenshot_20221021_005151.png', 'rb') as fli:
    url = 'http://127.0.0.1:8000/api/v1/image/'
    files={'image': ('nsdfsdfame_of_file.png', fli)}
    res = requests.post(url, files=files)
    print(res.json())
```
