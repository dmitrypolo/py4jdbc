Py4jdbc
===========

This repo aspires to be a (partially) `dbapi 2.0 <https://www.python.org/dev/peps/pep-0249/>`_ compliant interface to JDBC. It's similar to `JayDeBeAPI <https://github.com/baztian/jaydebeapi>`_, but uses a much more efficient JVM backend process implemented with Py4j instead of JPype.

Example
++++++++++++

A simple example that starts a JVM subprocess::

    from py4jdbc.gatway_process import GatewayProcess

    with GatewayProcess() as gateway:
        params = dict(
            user='test',
            password='test',
            host='localhost',
            engine='postgres',
            database='postgres')

        jdbc = JdbcClient.from_py4j(gateway, **params)
        for col in jdbc.get_columns():
            print(col)