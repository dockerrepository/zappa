FROM python:3.6.5

LABEL maintainer="nielsonnas@gmail.com"

RUN apt-get -y update && apt-get -y install gettext

RUN pip install -U zappa

ADD ./bashrc.sh /root/bashrc_extras
RUN sed -i 's/\r//' /root/bashrc_extras
RUN chmod +x /root/bashrc_extras

RUN echo "\nsource ~/bashrc_extras" >> /root/.bashrc

WORKDIR /var/task

CMD ["zappa"]