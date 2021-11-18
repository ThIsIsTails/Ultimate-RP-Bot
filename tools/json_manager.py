import os


class json:
    def __init__(self, file: str):
        self.file = file

    def read(self):
        import json
        
        data = None
        with open(os.path.join(self.file), "r") as r:
            data = r.read()
        data = json.load(data)

        return data

    def write(self, data):
        with open(os.path.join(self.file), "w") as w:
            w.write(data)