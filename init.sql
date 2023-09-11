-- Arquivo init.sql

-- Criação da tabela 'users'
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);

-- Criação da tabela 'chosen_cards'
CREATE TABLE IF NOT EXISTS chosen_cards (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    card_name TEXT NOT NULL
);

-- Outras tabelas ou comandos SQL podem ser adicionados aqui, se necessário
