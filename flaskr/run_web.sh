#!/bin/bash
set -e
set -x

export FLASK_ENV=$MODE

if [[ $MODE == "development" ]] ; then
  flask run --host=$HOST --port=$PORT
fi
