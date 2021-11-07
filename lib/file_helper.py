from path_helper import Path


class File:
    def __init__(self, path: Path):
        self.path = path.path

    def name(self):
        return self.path.split('/')[-1].split('\\')[-1].split('.')[0]

    def extension(self):
        return self.path.split('.')[-1]
