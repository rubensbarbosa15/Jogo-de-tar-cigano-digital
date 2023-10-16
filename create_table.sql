-- create_table.sql

CREATE TABLE tarot_shuffled_order (
    id SERIAL PRIMARY KEY,
    card_id INT,
    order_position INT
);
