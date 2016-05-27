import six
from compose.cli.command import get_project

from .containers import Container, Address


class DockerClientStub(object):
    STATES = {
        'STOPPED': 'STOPPED',
        'UP': 'UP',
    }
    CREATED_STATES = {
        'NOT_CREATED': 'NOT_CREATED',
        'CREATED': 'CREATED'
    }

    def __init__(self, services=None):
        self.created_state = self.CREATED_STATES['NOT_CREATED']
        self.state = self.STATES['STOPPED']
        if services is not None:
            self._services = services
        else:
            self._services = {}

    def up(self):
        self.created_state = self.CREATED_STATES['CREATED']
        self.state = self.STATES['UP']

    def stop(self):
        self.created_state = self.CREATED_STATES['CREATED']
        self.state = self.STATES['STOPPED']

    def remove(self):
        self.created_state = self.CREATED_STATES['NOT_CREATED']
        self.state = self.STATES['STOPPED']

    @property
    def services(self):
        return self._services


class DockerClient(object):
    def __init__(self, project_name, base_dir, config_path):
        self.project = get_project(
            base_dir,
            project_name=project_name,
            config_path=[config_path]
        )

    def up(self):
        self.project.up()

    def stop(self):
        self.project.stop()

    def remove(self):
        self.project.remove_stopped()

    @property
    def services(self):
        return {
            service.name: [
                Container(container.name, addresses_from_container(container))
                for container in service.containers()
                ]
            for service in self.project.services
        }


def internal_port_from_docker(docker_port):
    return int(docker_port.split('/')[0])


def addresses_from_container(docker_container):
    return {
        internal_port_from_docker(internal):
            [Address(address['HostIp'], int(address['HostPort']))
             for address in addresses]
        for internal, addresses in six.iteritems(docker_container.ports)
    }
