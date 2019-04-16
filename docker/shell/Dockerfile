FROM ubuntu:latest
COPY ./testme.sh /
ENV USER=duser
RUN chmod u+x /testme.sh
ENTRYPOINT ["/testme.sh"]
