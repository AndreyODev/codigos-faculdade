
-- CRIAÇÃO DAS TABELAS ORIGINAIS
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE pedidos (
    id SERIAL PRIMARY KEY,
    cliente_id INT REFERENCES clientes(id),
    data_pedido DATE NOT NULL,
    valor DECIMAL(10,2) NOT NULL
);

-- INSERÇÃO DE NOVOS DADOS
INSERT INTO clientes (nome, email) VALUES
    ('rafaella', 'rafaella@gmail.com'),
    ('Jeferson', 'jeferson@gmail.com'),
    ('Andrey', 'andrey@gmail.com'),
    ('Rafael Alves', 'ramail.com');

INSERT INTO pedidos (cliente_id, data_pedido, valor) VALUES
    (1, '2024-12-10', 450.90),
    (2, '2025-01-22', 980.00),
    (3, '2025-03-18', 150.50),
    (4, '2025-07-05', 300.00),
    (2, '2025-09-25', 720.75);

-- ==========================================
-- INSERÇÃO DE NOVAS COLUNAS
-- ==========================================
ALTER TABLE clientes ADD COLUMN telefone VARCHAR(20);
ALTER TABLE clientes ADD COLUMN cidade VARCHAR(50);

-- Atualizando os novos campos
UPDATE clientes SET telefone = '(21) 98877-1234', cidade = 'Rio de Janeiro' WHERE id = 1;
UPDATE clientes SET telefone = '(22) 99745-9876', cidade = 'Saquarema' WHERE id = 2;
UPDATE clientes SET telefone = '(21) 99633-2221', cidade = 'Niterói' WHERE id = 3;
UPDATE clientes SET telefone = '(24) 99988-1111', cidade = 'Petrópolis' WHERE id = 4;

-- ==========================================
-- DELETAR UMA COLUNA
-- ==========================================
ALTER TABLE clientes DROP COLUMN cidade;

-- ==========================================
-- CRIAR BACKUP DE TABELA COM CONDIÇÃO WHERE
-- (Apenas clientes com pedidos acima de R$500)
-- ==========================================
CREATE TABLE clientes_backup AS
SELECT DISTINCT c.*
FROM clientes c
JOIN pedidos p ON c.id = p.cliente_id
WHERE p.valor > 500;

-- ==========================================
-- INNER JOIN
-- Mostra apenas clientes que têm pedidos
-- ==========================================
SELECT c.nome, c.email, p.valor, p.data_pedido
FROM clientes c
INNER JOIN pedidos p ON c.id = p.cliente_id;

-- ==========================================
-- FULL JOIN
-- Mostra todos os clientes e pedidos, mesmo sem correspondência
-- ==========================================
SELECT c.nome, p.valor, p.data_pedido
FROM clientes c
FULL JOIN pedidos p ON c.id = p.cliente_id;

-- ==========================================
-- CROSS JOIN
-- Combina todos os clientes com todos os pedidos
-- ==========================================
SELECT c.nome AS cliente, p.valor AS valor_pedido
FROM clientes c
CROSS JOIN pedidos p;

-- ==========================================
-- VERIFICAÇÃO FINAL
-- ==========================================
SELECT * FROM clientes;
SELECT * FROM clientes_backup;
