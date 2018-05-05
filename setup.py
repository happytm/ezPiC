from setuptools import setup

setup(
    name='ezPiC',
    packages=['ezPiC'],
    include_package_data=True,
    install_requires=[
        
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)