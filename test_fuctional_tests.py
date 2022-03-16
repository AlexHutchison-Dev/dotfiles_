import unittest
from shell_command import ShellCommand


class TestApplicationInterface(unittest.TestCase):
    def setUp(self, executable="./dotfiles.py"):
        self.executable = executable + " "

    # Eli runs the dotfiles application from his command line with no arguments to see what happens
    def test_application_responds_when_called_from_the_command_line(self):
        result = ShellCommand(self.executable)
        self.assertTrue("Hello World!" in result.get_output())


if __name__ == "__main__":
    unittest.main()
