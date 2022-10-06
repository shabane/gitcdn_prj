"""the intrerface for all of the source controls like github and gitlab"""

class CdnInterface():

    def __init__(self, owner, repo, filename):
        self.owner = owner
        self.repo = repo
        self.filename = filename

    def insert(self):
        ...

    def get(self):
        ...

    def update(self):
        ...

    def delete(self):
        ...
