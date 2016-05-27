import six

from dockerintegration.exceptions import NoSuchContainerPortException, NoSuchServiceException


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

    def get_first_address_by_service(self, service_name, container_port):
        try:
            first_container = self.services[service_name][0]
        except KeyError:
            raise NoSuchServiceException(service_name)
        try:
            addresses = first_container.addresses[container_port]
        except KeyError:
            raise NoSuchContainerPortException(container_port)
        return addresses[0]

    def setup(self):
        self.docker_client.up()

    def teardown(self, remove=True):
        self.docker_client.stop()
        if remove:
            self.docker_client.remove()
