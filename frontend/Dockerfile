FROM node:16.20.2-alpine


WORKDIR /app

COPY package.json ./
RUN npm install -g expo-cli@latest
RUN npm install
RUN npx expo install --fix

COPY . .
