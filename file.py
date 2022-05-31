import os
import shutil


class File:
    def __init__(self, path):
        self.path = path
        self.dotfiles_dir = os.path.join(os.environ["HOME"], "dotfiles")
        self.path_relative_to_home = self._extract_relative_path()
        self.dotfiles_path = os.path.join(self.dotfiles_dir, self.path_relative_to_home)

    def get_path(self):
        return self.path

    def get_dotfiles_path(self):
        return self.dotfiles_path

    def _copy_file(self):
        shutil.copy(
            self.path, os.path.join(self.dotfiles_dir, self.path_relative_to_home)
        )
        print(os.listdir(self.dotfiles_dir))

    def _extract_relative_path(self):
        destructured_path = self.path.split("/")
        return destructured_path[-1]
