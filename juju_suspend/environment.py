from jujuclient import Environment as GoEnvironment
from juju_suspend import providers

import yaml
import subprocess
import os


class Environment:

    def __init__(self, options):
        env_path = os.path.expanduser(
            "~/.juju/environments/%s.jenv" % self.name)

        if not os.path.exists(env_path):
            raise Exception("Not found specified environment: %s" % self.name)

        with open(env_path) as fd:
            loaded = yaml.load(fd.read())

        for k, v in loaded.items():
            setattr(self, k.replace("-", "_"), v)

        self._env = GoEnvironment("wss://{}".format(self.state_servers[0]))
        self._env.login(self.password)
        self.options = options

        try:
            provider_type = self.bootstrap_config.get('type')
            klass = "{0}Provider".format(provider_type.capitalize())
            self.provider = getattr(providers, klass)(self)
        except AttributeError:
            raise Exception("Provider type: %s , not supported yet"
                            % provider_type)
        except:
            raise

    @property
    def name(self):
        if hasattr(self, '_name'):
            return self._name
        name = os.environ.get("JUJU_ENV", None)
        if name:
            self._name = name
        else:
            self._name = yaml.load(
                subprocess.check_output(["juju", "get-environment"]))['name']
        return self._name

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
