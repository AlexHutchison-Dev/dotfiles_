import os
import shutil


class AddFile:
    def __init__(self, path):
        self.path = path
        self.dotfiles_dir = os.path.join(os.environ["HOME"], "dotfiles")
        self.path_relative_to_home = self._extract_relative_path()

    def add(self):
        self._copy_file()

    def _copy_file(self):
        shutil.copy(
            self.path, os.path.join(self.dotfiles_dir, self.path_relative_to_home)
        )

    def _extract_relative_path(self):
        destructured_path = self.path.split("/")
        return destructured_path[-1]
