FROM node:18.10-alpine

WORKDIR /app

COPY ./package.json ./

RUN npm install

COPY . .

# development!
CMD ["npm", "run", "start"]