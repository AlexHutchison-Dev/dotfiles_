from file import File
import click
import os


class AddFile:
    def __init__(self, path):
        self.path = path
        self.target_file = File(path)
        self.add()

    def add(self):
        print(self.target_file.get_dotfiles_path())
        if os.path.exists(self.target_file.get_dotfiles_path()):
            click.echo("file already added")
            # print("file already added")
            return
        self.target_file._copy_file()
