import unittest
from shell_command import ShellCommand


class TestApplicationInterface(unittest.TestCase):
    def setUp(self, executable="dotfiles"):
        self.executable = executable

    def test_displays_usage_hint_when_no_arguments_passed(self):
        result = ShellCommand(self.executable)
        self.assertTrue("Usage: dotfiles" in result.get_output())


if __name__ == "__main__":
    unittest.main()
