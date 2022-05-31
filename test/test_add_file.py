import os
from unittest import TestCase
from shell_command import ShellCommand
from click.testing import CliRunner
from dotfiles import cli

# from dotfiles import cli
import filecmp


class TestAddFile(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_file_path = os.path.join(os.environ["HOME"], "dotfiles_test_file.txt")
        cls.runner = CliRunner()
        cls.copied_test_file_path = os.path.join(
            os.environ["HOME"], "dotfiles", "dotfiles_test_file.txt"
        )

        ShellCommand("touch " + cls.test_file_path)

    @classmethod
    def tearDownClass(cls):
        ShellCommand("rm " + cls.test_file_path)
        ShellCommand("rm " + cls.copied_test_file_path)

    def test_responds_with_error_when_path_provided_doesnt_exist(self):
        result = self.runner.invoke(cli, ["add", "~/nonexistant.txt"])

        assert result.exit_code == 2
        assert "Error: Invalid value for 'FILENAME'" in result.output

    def test_copies_file_to_dotfiles_dir(self):
        self.runner.invoke(cli, ["add", self.test_file_path])

        assert os.path.exists(self.copied_test_file_path)
        assert filecmp.cmp(self.test_file_path, self.copied_test_file_path)

    def test_prints_message_if_file_to_copy_already_exists(self):
        result = self.runner.invoke(cli, ["add", self.test_file_path])
        self.assertTrue("file already added" in result.output)
