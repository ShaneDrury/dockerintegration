import pytest
import six


@pytest.fixture
def service_internal_ports():
    return {
        'foo': [59001, ],
        'bar': [59002, 59003]
    }


def test_docker_fixture_services(docker_fixture, service_internal_ports):
    for service_name, ports in six.iteritems(service_internal_ports):
        service = docker_fixture.services[service_name]
        for container in service:
            docker_ports = container.addresses.keys()
            assert sorted(ports) == sorted(docker_ports)


def test_docker_fixture_ports(docker_fixture, service_internal_ports):
    for service_name, port_mapping in six.iteritems(docker_fixture.ports):
        internal_ports = port_mapping.keys()
        assert sorted(service_internal_ports[service_name]) == sorted(internal_ports)
