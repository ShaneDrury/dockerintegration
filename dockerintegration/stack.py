import six


class Stack(object):
    def __init__(self, docker_client):
        self._docker = docker_client

    def _stop(self):
        self._docker.stop()

    def _up(self):
        self._docker.up()

    def _remove(self):
        self._docker.remove()

    @property
    def services(self):
        return self._docker.services

    @property
    def ports(self):
        return {
            name: {
                internal: [address.port for address in external]
                for container in containers
                for internal, external in six.iteritems(container.addresses)
            }
            for name, containers in six.iteritems(self.services)
        }

    def setup(self):
        self._up()

    def teardown(self, remove=True):
        self._stop()
        if remove:
            self._remove()
