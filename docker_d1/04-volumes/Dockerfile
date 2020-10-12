FROM node:14

RUN npm i eslint -g

WORKDIR /test
RUN echo '{"rules": {"semi": ["error", "always"],"quotes": ["error", "double"]}}' > .eslintrc.json

ENTRYPOINT cp -R /data/* /test && eslint ./*.js
