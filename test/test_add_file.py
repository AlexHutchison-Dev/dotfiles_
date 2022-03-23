import os
from unittest import TestCase
from shell_command import ShellCommand
from click.testing import CliRunner
from dotfiles import cli


class TestAddFile(TestCase):
    def setUp(self):
        self.executable = "dotfiles add "
        self.test_file_path = os.path.join(os.environ["HOME"], "dotfiles_test_file.txt")
        self.runner = CliRunner()
        ShellCommand("touch " + self.test_file_path)

    def tearDown(self):
        ShellCommand("rm " + self.test_file_path)

    def test_should_respond_with_error_when_path_provided_doesnt_exist(self):
        result = self.runner.invoke(cli, ["add", "~/nonexistant.txt"])
        assert result.exit_code == 2
        assert "Error: Invalid value for 'FILENAME'" in result.output

    def test_should_echo_path_to_screen_if_provided(self):
        result = self.runner.invoke(cli, ["add", self.test_file_path])
        assert result.exit_code == 0
        assert self.test_file_path in result.output
