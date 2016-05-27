import pytest

from dockerintegration import docker_fixture as _docker_fixture


@pytest.fixture(scope='module')
def docker_fixture(request):
    return _docker_fixture(request)
