FROM python:2.7.14

LABEL maintainer="nielsonnas@gmail.com"

RUN apt-get update && apt-get install -y gettext

RUN pip install -U virtualenv && \
  pip install -U virtualenv zappa pip>=9.0.3

ADD ./python-2.7/bashrc.sh /root/bashrc_extras
RUN sed -i 's/\r//' /root/bashrc_extras
RUN chmod +x /root/bashrc_extras

RUN echo "\nsource ~/bashrc_extras" >> /root/.bashrc

WORKDIR /var/task

CMD ["zappa"]