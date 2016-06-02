import six


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
    for service in client.project.services:
        if service.name == 'oneport':
            service.scale(2)
            break
    else:
        raise ValueError("No service 'oneport'")
    assert len(docker_fixture.services['oneport'].containers) == 2
    service.scale(1)
    assert len(docker_fixture.services['oneport'].containers) == 1
