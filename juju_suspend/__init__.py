from jujuclient import Environment as GoEnvironment
from juju_suspend import providers

import yaml
import os


class Environment:

    def __init__(self, name=None, **options):

        #TODO: move this to the cli
        env_path = os.path.expanduser(
            "~/.juju/environments/%s.jenv" % name)

        #TODO: move this logic to the cli
        if not os.path.exists(env_path):
            raise Exception("Not found specified environment: %s" % name)

        with open(env_path) as fd:
            loaded = yaml.load(fd.read())

        for k, v in loaded.items():
            setattr(self, k.replace("-", "_"), v)

        self._env = GoEnvironment("wss://{}".format(self.state_servers[0]))
        self._env.login(self.password)
        self.options = options

    @property
    def provider(self):
        if not hasattr(self, '_provider'):
            klass = "{0}Provider".format(
                self.bootstrap_config.get('type').capitalize())
            self._provider = getattr(providers, klass)(self)
        return self._provider

    @property
    def status(self):
        return self._env.status()

    @property
    def machines(self):
        return self.status.get('Machines').items()

    def suspend(self):
        return self.provider.suspend()

    def resume(self):
        return self.provider.resume()
