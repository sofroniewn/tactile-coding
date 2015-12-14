FROM andrewosh/binder-base

MAINTAINER Jeremy Freeman <freeman.jeremy@gmail.com>

USER root

# Add dependency
RUN apt-get update
RUN apt-get install -y default-jre

# Install Spark
RUN wget http://d3kbcqa49mib13.cloudfront.net/spark-1.4.1-bin-hadoop1.tgz 
RUN tar -xzf spark-1.4.1-bin-hadoop1.tgz
ENV SPARK_HOME $HOME/spark-1.4.1-bin-hadoop1
ENV PATH $PATH:$SPARK_HOME/bin
ENV PYTHONPATH $PYTHONPATH:$SPARK_HOME/python
ENV PYTHONPATH $PYTHONPATH:$SPARK_HOME/python/lib/py4j-0.8.2.1-src.zip
RUN sed 's/log4j.rootCategory=INFO/log4j.rootCategory=ERROR/g' $SPARK_HOME/conf/log4j.properties.template > $SPARK_HOME/conf/log4j.properties
ENV _JAVA_OPTIONS "-Xms512m -Xmx4g" 

# Install Python requirements
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Do boto configuration
RUN printf '[s3]\ncalling_format = boto.s3.connection.OrdinaryCallingFormat' >> ~/.boto