from typing import List
from pathlib import Path
import shutil

class Parser:

    extensions = List[str]

    def valid_extension(self, extension):
        if extension in self.extensions:
            return(extension)

    def parse(self, path, source, dest):
        self.path = Path(path)
        self.source = Path(source)
        self.dest = Path(dest)
        raise NotImplementedError

    def read(self, path):
        with open(path, "r") as file:
            return read(file)

    def write(self, path, dest, content, ext=".html"):
        full_path = dest / path.with_suffix(ext).name
        with open(full_path, "w") as file:
            file.write(content)

    def copy(self, path, source, dest):
        shutil.copy2(path, dest / path.source)

    class ResourceParser:
        def __init__(self, extensions):
            self.extensions = [".jpg", "png", ".gif", ".css", ".html"]

        def parse(self, path, source, dest):
            self.path = Path(path)
            self.source = Path(source)
            self.dest = Path(dest)
            raise NotImplementedError
            shutil.copy2(path, source, dest)



