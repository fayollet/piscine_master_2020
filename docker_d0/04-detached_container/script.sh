#!/usr/bin/env bash

docker run -d -p 8000:8000 php:7.3-cli php -S 0.0.0.0:8000
