from dockerintegration.docker import DockerClientStub, DockerClient
from dockerintegration.stack import Stack


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
