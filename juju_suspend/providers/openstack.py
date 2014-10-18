from juju_suspend.providers.base import Provider


class OpenstackProvider(Provider):

    suspend_cmd = ". {1}; nova stop {0}"
    resume_cmd = ". {1}; nova start {0}"

    def __init__(self, environment):
        Provider.__init__(self, environment)
        if not self.environment.options.novarc:
            raise Exception("Please specify your novarc file")

    def filter_machines(self):
        for i, v in self.environment.machines:
            instance_id = v['InstanceId']

            if instance_id not in ('localhost',) and v['DNSName'] + ':17070'\
               not in self.environment.state_servers:
                yield instance_id

    def suspend(self):
        self.do_suspend(self.environment.options.novarc)

    def resume(self):
        self.do_resume(self.environment.options.novarc)
