import os
from shell_command import ShellCommand


class SetUp:
    def __init__(self, path):
        self.path = path
        # if not self.dotfiles_directory_exists():
        #     self.create_dotfiles_directory()

    def dotfiles_directory_exists(self):
        if os.path.exists(self.path) and os.path.isdir(self.path):
            return True
        return False

    def create_dotfiles_directory(self):
        ShellCommand("mkdir " + self.path)
        return os.path.exists(self.path)
