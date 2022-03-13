#!/bin/bash
set -e
set -x

export FLASK_ENV=$MODE

echo "Starting Morse Code as `whoami`"
if [[ $MODE == "development" ]]; then
  flask run --host=$HOST --port=$PORT
else
  uwsgi --http $HOST:$PORT --gevent 1000 --http-websockets --master \
    --wsgi-file wsgi.py --callable app \
    --req-logger file:$LOGS_ROOT/uwsgi_req.log \
    --logger file:$LOGS_ROOT/uwsgi_log.log
fi
