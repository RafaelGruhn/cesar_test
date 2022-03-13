FROM python:3.9 AS flask

ARG MODE

WORKDIR /code/
ADD ./requirements /code/requirements/
ADD ./setup.sh /code/setup.sh
RUN sh /code/setup.sh
RUN mkdir -p /var/log/morse_code

EXPOSE 8000
ENTRYPOINT ["/code/run_web.sh"]
