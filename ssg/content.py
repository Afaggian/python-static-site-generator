from yaml import re, load, FullLoader
from _collections_abc import Mapping

class Content(Mapping):
    __delimeter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)

    @classmethod
    def load(cls, string):
        _, fm, content = cls.__regex.split(string, 2)
        metadata = cls.load(fm, Loader=FullLoader)
        return cls(metadata, content)

    def __init__(self, metadata, content):
        self.data = metadata
        self.data["content"] = content

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        if "type" in self.data:
            return self.data["type"]
        else:
            return "None"

    @type.setter
    def type(self,type):
        self.data["type"] = type


    def __getitem__(self, key):
        return self.data[key]

    def __inter__(self):
        self.data.__inter__()

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        data = {}
        for key, value in self.data.items()
            if key != "content":
                data[key] = value
        return str(data)