from distutils.core import setup

setup(
        name='dockerintegration',
        version='0.0.1',
        packages=['dockerintegration', 'dockerintegration.tests'],
        entry_points={
            'pytest11': [
                'name_of_plugin = dockerintegration.plugin',
            ]
        },
        classifiers=[
            "Framework :: Pytest",
        ],
        url='',
        license='',
        author='Shane Drury',
        author_email='shane.r.drury@gmail.com',
        description='Use docker with integration tests',
        install_requires=['docker-compose', ],
)
