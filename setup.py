#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess

try:
    from setuptools import setup
    from setuptools.file_util import copy_file
    from setuptools.command.install import install
    from setuptools.command.build import build
    from setuptools.spawn import find_executable
except ImportError:
    from distutils.core import setup
    from distutils.file_util import copy_file
    from distutils.command.install import install
    from distutils.command.build import build
    from distutils.spawn import find_executable

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = ["py4j==0.10.1"]
test_requirements = ["pytest", "coverage", "pytest-cov"]

exec(compile(open("py4jdbc/version.py").read(), "py4jdbc/version.py", 'exec'))
VERSION = __version__  # noqa

class jar_build(build):
    user_options = build.user_options + []
    def run(self):
        """
        Compile the companion jar file.
        """
        if find_executable('sbt') is None:
            raise EnvironmentError("""

The executable "sbt" cannot be found.

Please install the "sbt" tool to build the companion jar file.
""")
        
        build.run(self)

        cwd = os.getcwd()
        os.chdir('py4jdbc/scala')
        subprocess.check_call('sbt clean', shell=True)
        subprocess.check_call('sbt assembly', shell=True)
        os.chdir(cwd)
        
class jar_install(install):
    def run(self):
        """
        Install the companion jar file.
        """
        install.run(self)
        
        dest = os.path.normpath(os.path.join(os.path.realpath(find_executable('java')), '../../lib/ext'))
        
        copy_file("py4jdbc/scala/target/scala-2.10/py4jdbc-assembly-0.1.6.2.jar",
                  "{0}/py4jdbc-assembly-0.1.6.2.jar".format(dest))

setup(
    name='py4jdbc',
    version=VERSION,
    description="py4j JDBC wrapper",
    long_description=readme,
    author="Thom Neale",
    author_email='tneale@massmutual.com',
    url='https://github.com/massmutual/py4jdbc',
    packages=['py4jdbc', 'py4jdbc.exceptions'],
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
    cmdclass={'build': jar_build, 'install': jar_install},
    package_data={
        'py4jdbc': [
            'scala/build.sbt',
            'scala/LICENCE',
            'scala/project/assembly.sbt',
            'scala/src/main/scala/GatewayServer.scala'
        ]
    }
)
