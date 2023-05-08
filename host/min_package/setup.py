from setuptools import setup

setup(
    name='min',
    version='2.1.1',
    description='The MIN protocol specification and reference implementation',
    author='min-protocol',
    packages=['min'],
    py_modules=['min', 'minmon', 'PayloadBuilder'],
    url='https://github.com/min-protocol/min',
    install_requires = [
        'pyserial>=2.7',
    ]
)
