import pytest

from dockerintegration.testing import get_config, get_testing_stack


@pytest.fixture(scope='session')
def docker_stack(request):
    config = get_config()
    stack = get_testing_stack(config)
    stack.__enter__()
    request.addfinalizer(lambda: stack.__exit__())
    return stack
