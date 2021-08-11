#!/bin/bash

python -m pytest --cov=reclinker --cov-config=./coveragerc --cov-report html:cov_html test
echo Flake8:
flake8 --max-line-length=120 --ignore=T001 reclinker
