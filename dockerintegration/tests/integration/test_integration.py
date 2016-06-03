import six

from dockerintegration.containers import HostAddress

SERVICES = {
    'oneport': [59001, ],
    'twoports': [59002, 59003]
}


def test_docker_stack_services(docker_stack):
    for service_name, ports in six.iteritems(SERVICES):
        service = docker_stack.services[service_name]
        for container in service.containers:
            docker_ports = container.port_mappings.keys()
            assert sorted(ports) == sorted(docker_ports)


def test_docker_scale(docker_stack):
    client = docker_stack.docker_client
    assert len(docker_stack.services['oneport'].containers) == 1
    client.scale('oneport', 2)
    assert len(docker_stack.services['oneport'].containers) == 2
    client.scale('oneport', 1)
    assert len(docker_stack.services['oneport'].containers) == 1


def test_get_addresses_by_port(docker_stack):
    addresses = docker_stack.services['oneport'].get_addresses_by_port(59001)
    assert len(addresses) == 1


def test_get_addresses_by_port_scale(docker_stack):
    client = docker_stack.docker_client
    client.scale('oneport', 2)
    addresses = docker_stack.services['oneport'].get_addresses_by_port(59001)
    assert len(addresses) == 2
    client.scale('oneport', 1)


def test_get_one_address_by_port(docker_stack):
    address = docker_stack.services['oneport'].get_one_address_by_port(59001)
    assert type(address) == HostAddress


def test_scoping(docker_stack_func):
    # Just testing that the fixture exists
    addresses = docker_stack_func.services['oneport'].get_addresses_by_port(59001)
    assert len(addresses) == 1
