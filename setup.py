#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess


try:
    from setuptools import setup, find_packages
    from setuptools.command.install import install
except ImportError:
    from distutils.core import setup, find_packages, install


with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    "py4j"
    # TODO: put package requirements here
]

test_requirements = [
    "pytest", "coverage"
    # TODO: put package test requirements here
]



jar_file_path = ('scala', 'target', 'scala-2.10', 'py4jdbc-assembly-0.0.jar')
JAR_FILE_PATH = os.path.join(*jar_file_path)


class InstallPy4jdbc(install):
    """Customized setuptools install command - prints a friendly greeting."""
    def run(self):
        self.sbt_assembly()
        install.run(self)

    def sbt_assembly(self):
        cwd = os.getcwd()
        os.chdir('scala')
        subprocess.check_call('sbt assembly', shell=True)
        os.chdir(cwd)


setup(
    name='py4jdbc',
    version='0.1.0',
    description="py4j JDBC wrapper",
    long_description=readme,
    author="Thom Neale",
    author_email='tneale@massmutual.com',
    url='https://github.com/massmutual/py4jdbc',
    packages=find_packages(),
    data_files=[('share/py4jdbc', [JAR_FILE_PATH])],
    package_dir={'py4jdbc':
                 'py4jdbc'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords=['jdbc', 'dbapi', 'py4j'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    scripts=['scripts/sbtassembly']
)
