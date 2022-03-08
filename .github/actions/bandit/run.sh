#!/bin/sh
set -e
echo "############################################"
echo "Checking for errors on Pylint..."
bandit -r $INPUT_BASEPATH/
echo "############################################"
