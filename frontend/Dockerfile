FROM node:16.20.2-alpine


WORKDIR /app

COPY package.json ./
RUN npm i expo-cli@latest
RUN npx expo install --fix

COPY . .
