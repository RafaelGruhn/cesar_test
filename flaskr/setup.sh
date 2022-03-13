#!/bin/bash
set -e

if [[ "$MODE" == "development" ]]; then
  echo "Intall Development Dependencies"
  pip3 install -r ./requirements/main.txt
else
  echo "Intall Production Dependencies"
  pip3 install -r ./requirements/prd.txt
fi
