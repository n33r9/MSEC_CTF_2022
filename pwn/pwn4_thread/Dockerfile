FROM i386/ubuntu:20.04

MAINTAINER phanNT
RUN apt-get update

RUN useradd -m thread

COPY ./share/flag /flag
COPY ./share/run.sh /home/thread/run.sh
COPY ./share/thread /home/thread/thread

RUN chmod +x /home/thread/run.sh

RUN chown -R root:thread /home/thread
RUN chmod -R 755 /home/thread
RUN chmod 644 /flag

RUN echo thread > /etc/cron.deny
RUN chmod 644 /etc/cron.deny

RUN chmod -R 774 /var/tmp
RUN chmod -R 774 /tmp
RUN chmod -R 774 /dev
RUN chmod -R 774 /run
RUN chmod 1733 /dev/shm

WORKDIR /home/thread
 
CMD ["./run.sh"]

EXPOSE 1337
