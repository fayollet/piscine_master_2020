cd ../
docker build -t codingstyle:python -f ./\#moulinette/Dockerfile . >/dev/null && docker run codingstyle:python
