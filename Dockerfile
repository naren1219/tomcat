FROM openjdk:8-jre

# Define working directory.
WORKDIR /data

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr

# Define default command.
CMD ["bash"]

ENV TOMCAT_VERSION 7.0.70

## Set locales
#RUN locale-gen en_GB.UTF-8
#ENV LANG en_GB.UTF-8
#ENV LC_CTYPE en_GB.UTF-8

# Fix sh
RUN rm /bin/sh && ln -s /bin/bash /bin/sh


# Get Tomcat
RUN wget --quiet --no-cookies https://archive.apache.org/dist/tomcat/tomcat-7/v7.0.70/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz -O /tmp/tomcat.tgz && \
tar xzvf /tmp/tomcat.tgz -C /opt && \
mv /opt/apache-tomcat-${TOMCAT_VERSION} /opt/tomcat && \
 rm /tmp/tomcat.tgz 
RUN rm -rf /opt/tomcat/webapps/*

# Add admin/admin user

ENV CATALINA_HOME /opt/tomcat
ENV PATH $PATH:$CATALINA_HOME/bin

EXPOSE 8080
EXPOSE 8009
WORKDIR /opt/tomcat

COPY VN_sample_war/ROOT.war /opt/tomcat/webapps/ROOT.war
RUN mkdir -p /opt/tomcat/resources
COPY admin-config.groovy  /opt/tomcat/resources/admin-config.groovy
# Launch Tomcat
CMD ["/opt/tomcat/bin/catalina.sh", "run"]
