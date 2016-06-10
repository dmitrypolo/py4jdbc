FROM python:3.4

# Install python deps
ADD requirements.txt /app/requirements.txt
ADD requirements-test.txt /app/requirements-test.txt
RUN pip3 install -r /app/requirements.txt

# Install sbt
RUN apt-get update && apt-get install -yqq apt-transport-https \
  && echo "deb https://dl.bintray.com/sbt/debian /" | tee -a /etc/apt/sources.list.d/sbt.list \
  && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823 \
  && apt-get update && apt-get -yqq install default-jre sbt

# Build the assembly jar
ADD scala scala
RUN cd scala && sbt assembly
ENV CLASSPATH /py4jdbc/scala/target/scala-2.10/py4jdbc-assembly-0.0.jar

WORKDIR /py4jdbc/

