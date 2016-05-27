import six


class Stack(object):
    def __init__(self, docker_client):
        self.docker_client = docker_client

    @property
    def services(self):
        return self.docker_client.services

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

    def get_first_container_address(self, name, internal_port):
        first_container = self.services[name][0]
        addresses = first_container.addresses[internal_port]
        return addresses[0]

    def setup(self):
        self.docker_client.up()

    def teardown(self, remove=True):
        self.docker_client.stop()
        if remove:
            self.docker_client.remove()
