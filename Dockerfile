FROM python:3.5

# Install sbt
RUN apt-get update && \
  apt-get install -yqq apt-transport-https && \
  echo "deb https://dl.bintray.com/sbt/debian /" | tee -a /etc/apt/sources.list.d/sbt.list && \
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823 && \
  apt-get update && \
  apt-get -yqq install default-jre sbt

WORKDIR /py4jdbc/
COPY . ./
RUN pip install -r requirements-dev.txt

ENV CLASSPATH /py4jdbc/scala/target/scala-2.10/py4jdbc-assembly-0.1.2.jar
