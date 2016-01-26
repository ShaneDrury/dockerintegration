import random

import pytest
import string

from dockerintegration.docker import DockerClient
from .stack import Stack


def get_config():
    # TODO: Get this e.g. from env variables
    return {
        'base_dir': '.',
        'config_path': 'docker-compose.yml'
    }


def get_pytest_config(request):
    # TODO: Define and get options
    # e.g. request.config.getoption("--device")
    return {}


def random_name():
    return ''.join(random.choice(string.ascii_letters)
                               for _ in range(25))


def get_testing_stack(config):
    project_name = random_name()
    client = DockerClient(project_name, **config)
    return Stack(client)


@pytest.fixture
def docker_fixture(request):
    config = get_config()
    config.update(get_pytest_config(request))
    stack = get_testing_stack(config)
    stack.setup()
    request.addfinalizer(lambda: stack.teardown(remove=True))
    return stack.containers
