FROM docker/whalesay
MAINTAINER Steve Young (smyoung@gmail.com)
#LABEL version="1.0" description="This is a simple description"
RUN apt-get -y update && apt-get install -y fortunes
CMD /usr/games/fortune -a | cowsay
