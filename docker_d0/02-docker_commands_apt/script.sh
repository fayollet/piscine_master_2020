#!/usr/bin/env bash

docker run ubuntu:latest /bin/sh -c 'apt-get update; apt-get install figlet -y; export HELLO="Hello etna"; figlet $HELLO'
