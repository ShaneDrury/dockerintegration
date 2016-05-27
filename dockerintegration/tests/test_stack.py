import pytest

from dockerintegration.containers import Container, Address
from dockerintegration.docker import DockerClientStub
from dockerintegration.exceptions import NoSuchServiceException, NoSuchContainerPortException
from dockerintegration.stack import Stack


@pytest.fixture()
def services():
    return {
        'foo': [Container('foo_1', addresses={6789: [Address('0.0.0.0', 1234)]})],
        'bar': [Container('bar_1', addresses={7000: [Address('1.2.3.4', 5678)]})]
    }


def test_post_setup_state():
    docker_client = DockerClientStub()
    stack = Stack(docker_client)
    stack.setup()
    assert docker_client.state == docker_client.STATES['UP']
    assert docker_client.created_state == docker_client.CREATED_STATES['CREATED']


def test_post_teardown_state():
    docker_client = DockerClientStub()
    stack = Stack(docker_client)
    stack.teardown()
    assert docker_client.state == docker_client.STATES['STOPPED']
    assert docker_client.created_state == docker_client.CREATED_STATES['NOT_CREATED']


def test_post_teardown_state_no_remove():
    docker_client = DockerClientStub()
    stack = Stack(docker_client)
    stack.teardown(remove=False)
    assert docker_client.state == docker_client.STATES['STOPPED']
    assert docker_client.created_state == docker_client.CREATED_STATES['CREATED']


def test_get_first_container_address(services):
    docker_client = DockerClientStub(services=services)
    stack = Stack(docker_client)
    address = stack.get_first_address_by_service('foo', 6789)
    assert address == services['foo'][0].addresses[6789][0]


def test_get_non_existent_service(services):
    docker_client = DockerClientStub(services=services)
    stack = Stack(docker_client)
    with pytest.raises(NoSuchServiceException):
        stack.get_first_address_by_service('baz', 6789)


def test_get_non_existent_internal_port(services):
    docker_client = DockerClientStub(services=services)
    stack = Stack(docker_client)
    with pytest.raises(NoSuchContainerPortException):
        stack.get_first_address_by_service('foo', 4000)


def test_get_services(services):
    docker_client = DockerClientStub(services=services)
    stack = Stack(docker_client)
    assert stack.services == docker_client.services
