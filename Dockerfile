FROM docker/whalesay
MAINTAINER Steve Young (smyoung@gmail.com)
RUN apt-get -y update && apt-get install -y fortunes
CMD /usr/games/fortune -a | cowsay
