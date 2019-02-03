FROM centos:6
LABEL maintaner="rzz1995@live.com"
RUN yum install -y wget
WORKDIR /app
RUN wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" https://download.oracle.com/otn-pub/java/jdk/8u201-b09/42970487e3af4f5aa5bca3f542482c60/jdk-8u201-linux-x64.tar.gz
RUN tar xzf jdk-8u201-linux-x64.tar.gz && rm -rf jdk-8u201-linux-x64.tar.gz
#configure JAVA_HOME
ENV JAVA_HOME /app/jdk1.8.0_201
ENV PATH $JAVA_HOME/bin:$PATH
ENTRYPOINT [ "java", "-version" ]
CMD ["/bin/sh"]