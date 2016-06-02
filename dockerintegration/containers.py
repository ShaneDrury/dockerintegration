from collections import namedtuple

Container = namedtuple('Container', 'name, port_mappings')

HostAddress = namedtuple('HostAddress', 'ip, port')


class Service(object):
    def __init__(self, name, containers):
        self.name = name
        self.containers = containers

    def get_addresses_by_port(self, port):
        addresses = set()
        for container in self.containers:
            host_addresses = container.port_mappings.get(port, {})
            addresses.update(host_addresses)
        return list(addresses)

    def get_one_address_by_port(self, port):
        return self.get_addresses_by_port(port)[0]
