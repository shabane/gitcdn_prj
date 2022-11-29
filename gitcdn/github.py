"""the github actual class"""
from .cdninterface import CdnInterface
import requests
import base64
import json


class Github(CdnInterface):
    """this is the class of github"""
    #TODO: let the repo to be a list of str, this will let us to use the multiple repo for saving one content
    def __init__(self, owner, repo, token):
        CdnInterface.__init__(self, owner, repo)
        self.token = token
        self._apiUrl = f'https://api.github.com/repos/{self.owner}/{self.repo}/contents'
        self.headers= {
            'Authorization': f'Bearer {token}',
            'Accept': 'application/vnd.github+json',
        }

    def insert(self, path, file, message, b64: bool = False):
        data = {
            'content': file if b64 else base64.b64encode(file).decode(),
            'message': message
        }

        data = json.dumps(data)

        res = requests.put(f'{self._apiUrl}/{path}', headers=self.headers, data=data)
        return res

    @property
    def apiUrl(self):
        """getter and setter for apiUrl"""
        return self._apiUrl
