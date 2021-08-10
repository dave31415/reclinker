#!/bin/bash

python -m pytest test
echo Flake8:
flake8 --max-line-length=120 --ignore=T001 reclinker
