import unittest
from shell_command import ShellCommand


class TestSellCommand(unittest.TestCase):
    def setUp(self):
        self.command = ShellCommand("echo 'Hello World!'")

    def test_returns_output_string_provided_to_echo(self):
        self.assertTrue("Hello World!" in self.command.get_output())

    def test_returns_error_when_incorrect_comand_passed(self):
        result = ShellCommand("ehco Hello World!")
        self.assertTrue("not found" in result.get_error())


if __name__ == "__main__":
    unittest.main()
