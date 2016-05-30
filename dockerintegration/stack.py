class Stack(object):
    def __init__(self, docker_client):
        self.docker_client = docker_client

    def __enter__(self):
        self.docker_client.up()
        return self

    def __exit__(self, *args, **kwargs):
        self.docker_client.stop()
        self.docker_client.remove()

    @property
    def services(self):
        return self.docker_client.services
