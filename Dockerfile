FROM python:$PYVERSION

# Install sbt
RUN apt-get update && \
  apt-get install -yqq apt-transport-https && \
  echo "deb https://dl.bintray.com/sbt/debian /" | tee -a /etc/apt/sources.list.d/sbt.list && \
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823 && \
  apt-get update && \
  apt-get -yqq install default-jre sbt

WORKDIR /py4jdbc/
COPY py4jdbc/scala ./py4jdbc/scala
RUN cd /py4jdbc/py4jdbc/scala && sbt clean

COPY . ./
RUN python setup.py install