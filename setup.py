from distutils.core import setup

setup(
        name='docker-integration',
        version='0.0.1',
        packages=['dockerintegration', 'dockerintegration.tests'],
        entry_points={
            'pytest11': [
                'name_of_plugin = dockerintegration.plugin',
            ]
        },
        classifiers=[
            'Framework :: Pytest',
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.5',
            'Topic :: Utilities',
            'Intended Audience :: Developers',
            'Operating System :: Unix',
            'Operating System :: POSIX',
            'Operating System :: Microsoft :: Windows',
        ],
        url='https://github.com/ShaneDrury/dockerintegration',
        license='MIT',
        author='Shane Drury',
        author_email='shane.r.drury@gmail.com',
        description='A pytest fixture to provide Docker integration.',
        keywords=['docker', 'integration'],
        install_requires=['docker-compose', ],
)
