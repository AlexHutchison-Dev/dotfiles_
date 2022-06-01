import os

import click

from file import File


class AddFile:
    def __init__(self, path):
        self.path = path
        self.target_file = File(path)
        self.add()

    def add(self):
        if not self._file_already_added():
            self.target_file._copy_file()

    def _file_already_added(self):
        exists = os.path.exists(self.target_file.get_dotfiles_path())
        if exists:
            click.echo("file already added")
        return exists
