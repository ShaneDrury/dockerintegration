from compose.cli.command import get_project


class DockerClientStub(object):
    STATES = {
        'STOPPED': 'STOPPED',
        'UP': 'UP',
    }
    CREATED_STATES = {
        'NOT_CREATED': 'NOT_CREATED',
        'CREATED': 'CREATED'
    }

    def __init__(self):
        self.created_state = self.CREATED_STATES['NOT_CREATED']
        self.state = self.STATES['STOPPED']

    def up(self):
        self.created_state = self.CREATED_STATES['CREATED']
        self.state = self.STATES['UP']

    def stop(self):
        self.created_state = self.CREATED_STATES['CREATED']
        self.state = self.STATES['STOPPED']

    def remove(self):
        self.created_state = self.CREATED_STATES['NOT_CREATED']
        self.state = self.STATES['STOPPED']


class DockerClient(object):
    def __init__(self, project_name, base_dir, config_path):
        self.project = get_project(
            base_dir,
            project_name=project_name,
            config_path=[config_path]
        )

    def up(self):
        self.project.up()

    def stop(self):
        self.project.stop()

    def remove(self):
        self.project.remove_stopped()
