
-- CRIAÇÃO DAS TABELAS
CREATE TABLE cliente (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE pedidos (
    id SERIAL PRIMARY KEY,
    cliente_id INT REFERENCES cliente(id),
    data_pedido DATE NOT NULL,
    valor DECIMAL(10,2) NOT NULL
);

-- INSERÇÃO DE NOVOS DADOS
INSERT INTO cliente (nome, email) VALUES
    ('rafaella', 'rafaella@gmail.com'),
    ('Jeferson', 'jeferson@gmail.com'),
    ('Andrey', 'andrey@gmail.com'),
    ('Gabryella', 'gabryella@gmail.com');

INSERT INTO pedidos (cliente_id, data_pedido, valor) VALUES
    (1, '2024-12-10', 450.90),
    (2, '2025-01-22', 980.00),
    (3, '2025-03-18', 150.50),
    (4, '2025-07-05', 300.00),
    (2, '2025-09-25', 720.75);
	
-- INSERÇÃO DE NOVAS COLUNAS
ALTER TABLE cliente ADD COLUMN telefone VARCHAR(20);
ALTER TABLE cliente ADD COLUMN cidade VARCHAR(50);

-- Atualizando
UPDATE cliente SET telefone = '(21) 98877-1234', cidade = 'Rio de Janeiro' WHERE id = 1;
UPDATE cliente SET telefone = '(22) 99745-9876', cidade = 'Saquarema' WHERE id = 2;
UPDATE cliente SET telefone = '(21) 99633-2221', cidade = 'Niterói' WHERE id = 3;
UPDATE cliente SET telefone = '(24) 99988-1111', cidade = 'Petrópolis' WHERE id = 4;

-- DELETANDO UMA COLUNA
ALTER TABLE cliente DROP COLUMN cidade;

-- CRIANDO BACKUP COM CONDIÇÃO WHERE

CREATE TABLE cliente_backup AS
SELECT DISTINCT c.*
FROM cliente c
JOIN pedidos p ON c.id = p.cliente_id
WHERE p.valor > 500;

-- INNER JOIN
-- Mostra apenas clientes que têm pedidos
SELECT c.nome, c.email, p.valor, p.data_pedido
FROM cliente c
INNER JOIN pedidos p ON c.id = p.cliente_id;

-- FULL JOIN (todos clientes e todos pedidos)
SELECT c.nome, p.valor, p.data_pedido
FROM cliente c
FULL JOIN pedidos p ON c.id = p.cliente_id;

-- CROSS JOIN (produto cartesiano)
SELECT c.nome AS cliente, p.valor AS valor_pedido
FROM cliente c
CROSS JOIN pedidos p;


SELECT * FROM cliente;
SELECT * FROM cliente_backup;
