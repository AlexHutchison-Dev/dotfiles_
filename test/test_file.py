import unittest
import os

from file import File
from shell_command import ShellCommand


class TestFileClass(unittest.TestCase):
    def setUp(self):
        self.test_file_path = os.path.join(os.environ["HOME"], "dotfiles_test_file.txt")
        ShellCommand("touch" + self.test_file_path)
        self.f = File(self.test_file_path)

    def test_can_create_file_Object(self):
        assert isinstance(self.f, File)
