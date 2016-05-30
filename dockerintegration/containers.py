from collections import namedtuple

Container = namedtuple('Container', 'name, addresses')

Address = namedtuple('Address', 'ip, port')


class Service(object):
    def __init__(self, name, containers):
        self.name = name
        self.containers = containers

    def get_containers_by_port(self, port):
        containers = []
        for container in self.containers:
            for internal_port in container.addresses.keys():
                if internal_port == port:
                    containers.append(container)
        return containers
