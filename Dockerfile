version: '3'
services:
  postgres:
    image: postgres
    container_name: tarot-postgres
    environment:
      POSTGRES_USER: tarot_user
      POSTGRES_PASSWORD: tarot_password
      POSTGRES_DB: tarot_db
    volumes:
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
    ports:
      - "5432:5432"

  web:
    build: ./app  # Seu Dockerfile para a aplicação Flask
    container_name: tarot-app
    ports:
      - "5000:5000"
    depends_on:
      - postgres
