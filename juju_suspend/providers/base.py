import subprocess


class Provider(object):

    use_sudo = False

    def __init__(self, environment):
        self.environment = environment

    def run(self, command):
        if self.use_sudo:
            command = "sudo " + command
        return subprocess.call(command, shell=True)

    def do_suspend(self, *args, **kwargs):
        for machine in self.filter_machines():
            if callable(self.suspend_cmd):
                self.suspend_cmd(machine, *args, **kwargs)
            else:
                self.run(self.suspend_cmd.format(machine, *args))

    def do_resume(self, *args, **kwargs):
        for machine in self.filter_machines():
            if callable(self.resume_cmd):
                self.resume_cmd(machine, *args, **kwargs)
            else:
                self.run(self.resume_cmd.format(machine, *args))
