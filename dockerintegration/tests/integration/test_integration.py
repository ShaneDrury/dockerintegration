import six

from dockerintegration.containers import HostAddress

SERVICES = {
    'oneport': [59001, ],
    'twoports': [59002, 59003]
}


def test_docker_fixture_services(docker_fixture):
    for service_name, ports in six.iteritems(SERVICES):
        service = docker_fixture.services[service_name]
        for container in service.containers:
            docker_ports = container.port_mappings.keys()
            assert sorted(ports) == sorted(docker_ports)


def test_docker_scale(docker_fixture):
    client = docker_fixture.docker_client
    assert len(docker_fixture.services['oneport'].containers) == 1
    client.scale('oneport', 2)
    assert len(docker_fixture.services['oneport'].containers) == 2
    client.scale('oneport', 1)
    assert len(docker_fixture.services['oneport'].containers) == 1


def test_get_addresses_by_port(docker_fixture):
    addresses = docker_fixture.services['oneport'].get_addresses_by_port(59001)
    assert len(addresses) == 1


def test_get_addresses_by_port_scale(docker_fixture):
    client = docker_fixture.docker_client
    client.scale('oneport', 2)
    addresses = docker_fixture.services['oneport'].get_addresses_by_port(59001)
    assert len(addresses) == 2
    client.scale('oneport', 1)


def test_get_one_address_by_port(docker_fixture):
    address = docker_fixture.services['oneport'].get_one_address_by_port(59001)
    assert type(address) == HostAddress
