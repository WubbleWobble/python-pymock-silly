import json
from urllib.request import urlopen

class Api:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def stats(self):
        # Data - e.g. '[1,2,3,4,5]'
        return json.loads(urlopen(self.endpoint + "/stats").read())