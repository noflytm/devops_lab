#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="snapshot",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'snapshot = snapshot.snapshot:logging', ],
    },
    install_requires=[
        "psutil"
    ],
    version="1.0",
    author="Anton Antanovich",
    author_email="Anton_Antanovich@epam.com",
    description="Simple monitoring for you instance",
    license="MIT"
)
