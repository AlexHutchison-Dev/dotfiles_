import unittest
from shell_command import ShellCommand

from file import File


class TestFileClass(unittest.TestCase):
    def test_can_create_file_Object(self):
        f = File("path")
        assert isinstance(f, File)
