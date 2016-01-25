from dockerintegration.docker import DockerProject


def test_project_name():
    project_name = 'foo'
    project = DockerProject(project_name=project_name)
    assert project_name == project.project_name
