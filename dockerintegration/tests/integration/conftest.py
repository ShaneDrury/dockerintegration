import pytest


@pytest.fixture(scope='function')
def docker_stack_func(docker_stack):
    return docker_stack
