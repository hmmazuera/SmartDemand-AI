FROM ubuntu:latest
LABEL authors="mauriciomazuera"

ENTRYPOINT ["top", "-b"]