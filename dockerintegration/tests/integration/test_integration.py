import pytest
import six


@pytest.fixture
def service_internal_ports():
    return {
        'foo': [59001, ],
        'bar': [59002, 59003]
    }


def test_docker_fixture(docker_fixture, service_internal_ports):
    for service_name, ports in six.iteritems(service_internal_ports):
        service = docker_fixture[service_name]
        for container in service:
            docker_ports = [internal.port
                            for internal, _ in six.iteritems(container.addresses)]
            assert sorted(ports) == sorted(docker_ports)
