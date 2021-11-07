import os


class Path:
    def __init__(self, path, root_dir=None):
        if root_dir is None:
            root_dir = Path.project_path()
        self.path = os.path.abspath(os.path.join(root_dir, path))

    @staticmethod
    def project_path():
        curr_path = os.path.abspath(os.curdir)
        while True:
            if 'lib' in os.listdir(curr_path):
                return curr_path
            curr_path = os.path.abspath(os.path.join(curr_path, '..'))

    @classmethod
    def combine(cls, root_path, path):
        return cls(root_dir=root_path.path, path=path)
