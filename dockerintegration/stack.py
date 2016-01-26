from dockerintegration.containers import Container


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
    def containers(self):
        # TODO: Fill this in properly
        return [Container('name', 'host', 123), ]

    def setup(self):
        self._stop()
        self._up()

    def teardown(self, remove=True):
        self._stop()
        if remove:
            self._remove()
