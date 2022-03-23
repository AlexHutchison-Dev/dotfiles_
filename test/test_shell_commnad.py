import unittest
from shell_command import ShellCommand


class TestSellCommand(unittest.TestCase):
    def setUp(self):
        self.command = ShellCommand("echo 'Hello World!'")

    def test_should_return_string_string_provided_to_echo(self):
        self.assertTrue("Hello World!" in self.command.get_output())


if __name__ == "__main__":
    unittest.main()
