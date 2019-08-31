#!/bin/bash

set -euxo pipefail

docker build -t test .

docker run -it --rm -w /home/flask/src test /flaskvenv/bin/python __test__.py
