
CREATE TABLE produtos (
    id_produto SERIAL PRIMARY KEY,
    nome_produto VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL
);
INSERT INTO produtos (nome_produto, preco) VALUES 
('Arroz 5kg', 25.00),
('Sabonete', 3.50);

CREATE TABLE estoque (
    id_estoque SERIAL PRIMARY KEY,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER DEFAULT 0,
    FOREIGN KEY (produto_id) REFERENCES produtos(id_produto)
);
INSERT INTO estoque (produto_id, quantidade) VALUES (1, 100), (2, 50);

CREATE TABLE cliente (
    id_cliente SERIAL PRIMARY KEY,
    nome_cliente VARCHAR(100) NOT NULL
);
INSERT INTO cliente (nome_cliente) VALUES ('Andrey');

CREATE TABLE venda (
    id_venda SERIAL PRIMARY KEY,
    data_venda TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    cliente_id INTEGER,
    FOREIGN KEY (cliente_id) REFERENCES cliente(id_cliente)
);
INSERT INTO venda (cliente_id) VALUES (1); 

CREATE TABLE itens_venda (
    id_item SERIAL PRIMARY KEY,
    venda_id INTEGER NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    FOREIGN KEY (venda_id) REFERENCES venda(id_venda),
    FOREIGN KEY (produto_id) REFERENCES produtos(id_produto)
);
INSERT INTO itens_venda (venda_id, produto_id, quantidade)
VALUES (1, 1, 2),(1, 2, 3); 

CREATE TABLE log_vendas (
    id_caixa SERIAL PRIMARY KEY,
    data_log TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    venda_id INTEGER,
    produto_id INTEGER,
    quantidade INTEGER,
    FOREIGN KEY (venda_id) REFERENCES venda(id_venda),
    FOREIGN KEY (produto_id) REFERENCES produtos(id_produto)
);

-- FUNÇÃO TRIGGER

CREATE OR REPLACE FUNCTION registrar_log_venda()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO log_vendas (venda_id, produto_id, quantidade)
    VALUES (NEW.venda_id, NEW.produto_id, NEW.quantidade);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- TRIGGER
CREATE TRIGGER trigger_log_vendas
AFTER INSERT ON itens_venda
FOR EACH ROW
EXECUTE FUNCTION registrar_log_venda();

SELECT * FROM log_vendas;
