import pytest

from dockerintegration.containers import Container, Address, Service
from dockerintegration.docker import DockerClientStub
from dockerintegration.stack import Stack


@pytest.fixture()
def services():
    return {
        'foo': Service(
            name='foo',
            containers=[
                Container(
                    'foo_1',
                    addresses={6789: [Address('0.0.0.0', 1234)]}
                )
            ]
        ),
        'bar': Service(
            name='bar',
            containers=[
                Container('bar_1', addresses={7000: [Address('1.2.3.4', 5678)]})
            ]
        )
    }


def test_post_setup_state():
    docker_client = DockerClientStub()
    with Stack(docker_client):
        assert docker_client.state == docker_client.STATES['UP']
        assert docker_client.created_state == docker_client.CREATED_STATES['CREATED']


def test_post_teardown_state():
    docker_client = DockerClientStub()
    with Stack(docker_client):
        pass
    assert docker_client.state == docker_client.STATES['STOPPED']
    assert docker_client.created_state == docker_client.CREATED_STATES['NOT_CREATED']


def test_get_first_container_address(services):
    docker_client = DockerClientStub(services=services)
    with Stack(docker_client) as stack:
        service = stack.services['foo']
        container = service.get_containers_by_port(6789)[0]
        address = container.addresses[6789][0]
    assert address == services['foo'].containers[0].addresses[6789][0]


def test_get_non_existent_service(services):
    docker_client = DockerClientStub(services=services)
    with Stack(docker_client) as stack:
        assert stack.services.get('baz') is None


def test_get_non_existent_internal_port(services):
    docker_client = DockerClientStub(services=services)
    with Stack(docker_client) as stack:
        service = stack.services['foo']
        containers = service.get_containers_by_port(4000)
        assert containers == []


def test_get_services(services):
    docker_client = DockerClientStub(services=services)
    stack = Stack(docker_client)
    assert stack.services == docker_client.services
