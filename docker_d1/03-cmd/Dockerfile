FROM node:14

WORKDIR /data
COPY ./index.js ./
COPY ./package.json ./
RUN npm i

CMD ["npm", "start"]
