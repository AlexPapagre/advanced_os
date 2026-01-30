FROM eclipse-temurin:11-jdk

ENV SPARK_VERSION=3.4.2
ENV HADOOP_VERSION=3
ENV SPARK_HOME=/app/spark
ENV PATH="$SPARK_HOME/bin:$PATH"

RUN apt-get update && apt-get install -y curl python3 python3-pip procps && rm -rf /var/lib/apt/lists/*

RUN curl -L https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz \
    -o spark.tgz && \
    mkdir -p ${SPARK_HOME} && \
    tar xzf spark.tgz --strip-components=1 -C ${SPARK_HOME} && \
    rm spark.tgz

COPY spark-defaults.conf $SPARK_HOME/conf/spark-defaults.conf
COPY spark-env.sh $SPARK_HOME/conf/spark-env.sh

COPY start-spark.sh /app/start-spark.sh
RUN chmod +x /app/start-spark.sh

COPY requirements.txt .
RUN pip3 install --break-system-packages --no-cache-dir -r requirements.txt

COPY main.py /app/main.py

EXPOSE 8080 8081 6066 7077

WORKDIR /app
CMD ["/app/start-spark.sh"]
