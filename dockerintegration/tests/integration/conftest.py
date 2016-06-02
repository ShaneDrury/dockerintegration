import pytest

from dockerintegration import docker_stack as _docker_stack


@pytest.fixture(scope='module')
def docker_stack(request):
    return _docker_stack(request)
