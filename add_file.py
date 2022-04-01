from file import File


class AddFile:
    def __init__(self, path):
        self.path = path
        self.target_file = File(path)

    def add(self):
        self.target_file._copy_file()
