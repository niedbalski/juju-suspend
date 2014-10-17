from juju_suspend.providers.base import Provider


class OpenstackProvider(Provider):

    suspend_cmd = "nova suspend {0}"
    resume_cmd = "nova resume {0}"

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
