FROM python:3.6.5

LABEL maintainer="nielsonnas@gmail.com"

RUN apt-get update && apt-get install openssl ca-certificates libxml2-dev libxslt-dev \
    libffi-dev musl-dev postgresql-client

RUN pip install -U pip virtualenv zappa

ADD ./entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /var/task

ENTRYPOINT ["/entrypoint.sh"]
CMD ["zappa"]