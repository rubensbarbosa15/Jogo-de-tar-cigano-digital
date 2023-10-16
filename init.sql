-- Arquivo init.sql

-- Criação da tabela 'users'
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);

CREATE TABLE tarot_shuffled_order (
    id SERIAL PRIMARY KEY,
    card_id INT,
    order_position INT
);

