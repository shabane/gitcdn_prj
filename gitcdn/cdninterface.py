"""the intrerface for all of the source controls like github and gitlab"""


class CdnInterface():

    def __init__(self, owner, repo):
        self.owner = owner
        self.repo = repo

    def insert(self):
        ...

    def get(self):
        ...

    def update(self):
        ...

    def delete(self):
        ...
