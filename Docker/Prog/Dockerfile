FROM ubuntu:18.04

RUN apt-get update && apt install build-essential -y && apt install gcc -y

COPY hello.c hello.c

RUN gcc hello.c -o hello

CMD ./hello

