FROM python:3.7

LABEL maintainer="nielsonnas@gmail.com"

RUN apt-get -y update && apt-get -y install gettext

ADD ./requirements.txt /root/requirements.txt
RUN pip install -U virtualenv && pip install -r /root/requirements.txt

ADD ./bashrc.sh /root/.bashrc
RUN sed -i 's/\r//' /root/.bashrc

WORKDIR /var/task

CMD ["zappa"]