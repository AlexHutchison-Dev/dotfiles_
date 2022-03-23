import subprocess


class ShellCommand:
    out = ""
    err = ""

    def __init__(self, command):
        self.command = command
        self.run_command(command)

    def run_command(self, command):
        response = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = response.communicate()
        response.kill()
        self.out = out.decode("utf8")
        self.err = err.decode("utf8")
        # print(f"***\nShellCommand command: {self.command}\n")
        # print(f"ShellCommand out: {self.out}\n")
        # print(f"ShellCommand err: {self.err}\n***\n")

    def get_output(self):
        return self.out

    def get_err(self):
        return self.err
