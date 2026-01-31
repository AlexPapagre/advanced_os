FROM eclipse-temurin:11-jdk

ENV SPARK_VERSION=3.4.2
ENV HADOOP_VERSION=3
ENV SPARK_HOME=/opt/spark
ENV PATH="$SPARK_HOME/bin:$PATH"

RUN apt-get update && apt-get install -y curl python3 python3-pip python3-venv procps && \
    rm -rf /var/lib/apt/lists/*

RUN curl -L https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz \
    -o spark.tgz && \
    tar xzf spark.tgz -C /opt && \
    mv /opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} ${SPARK_HOME} && \
    rm spark.tgz

COPY config/spark-defaults.conf $SPARK_HOME/conf/spark-defaults.conf
COPY config/spark-env.sh $SPARK_HOME/conf/spark-env.sh

COPY config/start-spark.sh /opt/start-spark.sh
RUN chmod +x /opt/start-spark.sh

COPY data/ /opt/data/

COPY main.py /opt/main.py

EXPOSE 8080 8081 6066 7077

WORKDIR /opt
CMD ["/opt/start-spark.sh"]
