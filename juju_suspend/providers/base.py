import subprocess


class Provider(object):

    def __init__(self, environment):
        self.environment = environment

    def run(self, command):
        return subprocess.call("sudo " + command, shell=True)

    def do_suspend(self):
        for machine in self.filter_machines():
            if callable(self.suspend_cmd):
                self.suspend_cmd(machine)
            else:
                self.run(self.suspend_cmd.format(machine))

    def do_resume(self):
        for machine in self.filter_machines():
            if callable(self.resume_cmd):
                self.resume_cmd(machine)
            else:
                self.run(self.resume_cmd.format(machine))
