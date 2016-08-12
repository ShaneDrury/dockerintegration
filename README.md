# Docker Integration

[![Build Status](https://travis-ci.org/ShaneDrury/dockerintegration.svg?branch=master)](https://travis-ci.org/ShaneDrury/dockerintegration)

Control Docker from within Python scripts.
Set-up and tear-down for integration tests.

## Requirements
* Python (Tested on 2.7.10, 2.7.11, 3.5.1)
* [Docker](https://docs.docker.com/engine/installation/) (Tested on 1.8.2, 1.9.1, 1.11.1)
* [docker-compose](https://docs.docker.com/compose/) (Tested on 1.4.2, 1.5.2, 1.7.1)

## Installation

```python
pip install docker-integration
```

## Example Usage
To find the [Docker Compose YAML files](https://docs.docker.com/compose/compose-file/) Docker Integration needs the enviroment variable `COMPOSE_FILE` set.
This defaults to `./docker-compose.yml`.
e.g.

```bash
$ export COMPOSE_FILE=dockerintegration/tests/integration/files/test-compose.yml 
$ py.test
```

# py.test

```python
# test_redis.py
from redis import StrictRedis

def test_push_to_redis(docker_stack):
    address = docker_stack.services['redis'].get_addresses_by_port(6379)[0]
    redis = StrictRedis(host=address.ip, port=address.port)
    redis.rpush('key', ['value'])
    ...

# or if you're only running one container for a service

def test_push_to_redis_better(docker_stack):
    address = docker_stack.services['redis'].get_one_address_by_port(6379)
    redis = StrictRedis(host=address.ip, port=address.port)
    redis.rpush('key', ['value'])
    ...
```

Lower level usage:

```python

def test_scaling_web_app():
    client = DockerClient(
        project_name='testing_web_app',
        base_dir='.',
        config_path='docker-compose.yml'
    )
    with Stack(client) as docker_stack:
        docker_stack.scale('app', 4)
        nginx_address = docker_stack.services['nginx'].get_one_address_by_port(80)
        requests.get("http://{ip}:{port}".format(ip=nginx_address.ip, port=nginx_address.port))
        ...
        # Test the scaled app handles requests correctly
```

# Scoping

By default the docker_fixture has the scope 'session'. If you need a temporary stack e.g. when running isolated tests
you can define your own fixture with a more limited scope:

```python
# conftest.py
import pytest
@pytest.fixture(scope='function')
def docker_fixture_func(docker_fixture):
    return docker_fixture
```

## Running Tests

```bash
make test       # Runs integration and unit tests
make quicktest  # Only runs unit tests
```

## TODO

- Test set-up for unittest
