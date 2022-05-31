from unittest import TestCase
from set_up import SetUp

import os


class TestSetUp(TestCase):
    def test_checks_if_dotfiles_directory_exists(self):
        dotfiles_dir = os.path.join(os.environ["HOME"], "dotfiles")
        exists = os.path.exists(dotfiles_dir)

        self.assertTrue(exists, SetUp(dotfiles_dir).dotfiles_directory_exists())
        self.assertTrue(os.path.isdir(dotfiles_dir))

    def test_creates_dotfiles_directory(self):
        self.assertTrue(os.path.exists(os.path.join(os.environ["HOME"], "dotfiles")))
