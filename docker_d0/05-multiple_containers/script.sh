#!/usr/bin/env bash

docker run -d --name elegant_tony -e MYSQL_ROOT_PASSWORD=test mysql:latest ; 
docker run -d --name dazzling_robin httpd:latest; 
docker run -d --name ginger_jeremie php:7.3-cli php -S 0.0.0.0:8080
