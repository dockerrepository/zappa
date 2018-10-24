FROM python:3.6.5

LABEL maintainer="nielsonnas@gmail.com"

RUN apt-get -y update && apt-get -y install gettext

ADD ./requirements.txt /root/requirements.txt
RUN python -m pip install --upgrade pip==9.0.1
RUN python -m pip install -U virtualenv && pip install -r /root/requirements.txt

ADD ./bashrc.sh /root/.bashrc
RUN sed -i 's/\r//' /root/.bashrc

WORKDIR /var/task

CMD ["zappa"]