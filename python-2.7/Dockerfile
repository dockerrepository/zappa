FROM python:2.7.14

LABEL maintainer="nielsonnas@gmail.com"

RUN pip install -U virtualenv && \
  pip install -U virtualenv zappa

ADD ./entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /var/task

ENTRYPOINT ["/entrypoint.sh"]
CMD ["zappa"]