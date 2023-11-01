FROM ubuntu:18.04
RUN apt-get update
RUN apt-get -y install apache2
ADD . /var/www/html
ENTRYPOINT apachectl -D FOREGROUND
EXPOSE 80
Env name Devops IIT Roorkee
