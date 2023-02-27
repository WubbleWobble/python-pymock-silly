class Thing:
    def __init__(self, api):
        self.api = api

    def total(self):
        return sum(self.api.stats())