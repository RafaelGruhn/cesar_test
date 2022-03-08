FROM python:3.9 AS flask

WORKDIR /code/
ADD ./requirements /code/requirements/
RUN pip3 install -r ./requirements/main.txt
RUN mkdir -p /var/log/cesar_test
RUN mkdir -p /data

EXPOSE 8000
ENTRYPOINT ["/code/run_web.sh"]
