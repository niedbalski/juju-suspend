from juju_suspend.providers.base import Provider


class LocalProvider(Provider):

    suspend_cmd = "lxc-freeze -n {0}"
    resume_cmd = "lxc-unfreeze -n {0}"
    use_sudo = True

    def __init__(self, environment):
        Provider.__init__(self, environment)

    def filter_machines(self):
        for i, v in self.environment.machines:
            instance_id = v['InstanceId']
            if instance_id not in ('pending', 'localhost', ):
                yield instance_id

    def suspend(self):
        self.do_suspend()

    def resume(self):
        self.do_resume()
