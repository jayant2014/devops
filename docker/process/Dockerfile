ARG VERSION=latest
FROM ubuntu:${VERSION}
LABEL AUTHOR="jayant"
ENV USER=duser
RUN echo $USER && \
    mkdir /data
WORKDIR /data
COPY ./testme.sh /data
RUN echo "hello world" > test && \
    chmod u+x /data/testme.sh
ENTRYPOINT ["sleep", "1000"]
