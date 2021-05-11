# -*- coding: iso-8859-1 -*-

from setuptools import setup

# Paquetes de Python necesarios
requirements = ['flask', 'flask-restx']


setup(
    name='PROJECT-NAME',  # TODO: Change
    version='1.0',
    packages=[''],
    url='',
    license='',
    author='Héctor',
    author_email='',
    description='',
    entry_points={
        'console_scripts': [
            'PROJECT-NAME=run:run'  # TODO: Change
        ],
        'gui_scripts': []
    },
    install_requires=requirements
)
