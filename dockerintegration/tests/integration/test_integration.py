import six


SERVICES = {
    'oneport': [59001, ],
    'twoports': [59002, 59003]
}


def test_docker_fixture_services(docker_fixture):
    for service_name, ports in six.iteritems(SERVICES):
        service = docker_fixture.services[service_name]
        for container in service:
            docker_ports = container.addresses.keys()
            assert sorted(ports) == sorted(docker_ports)


def test_docker_fixture_ports(docker_fixture):
    for service_name, port_mapping in six.iteritems(docker_fixture.ports):
        internal_ports = port_mapping.keys()
        assert sorted(SERVICES[service_name]) == sorted(internal_ports)


def test_docker_get_first_container(docker_fixture):
    for name, ports in six.iteritems(SERVICES):
        for port in ports:
            address = docker_fixture.get_first_address_by_service(name, port)
            assert docker_fixture.ports[name][port][0] == address.port


def test_docker_scale(docker_fixture):
    client = docker_fixture.docker_client
    assert len(docker_fixture.services['oneport']) == 1
    for service in client.project.services:
        if service.name == 'oneport':
            service.scale(2)
            break
    else:
        raise ValueError("No service 'oneport'")
    assert len(docker_fixture.services['oneport']) == 2
    service.scale(1)
    assert len(docker_fixture.services['oneport']) == 1
