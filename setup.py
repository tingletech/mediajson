from setuptools import setup

setup(
    name='MediaJson',
    version='0.1.0',
    packages=['mediajson',],
    install_requires=['boto3','future',],
    test_suite='nose.collector',
    tests_require=['nose',],
)
