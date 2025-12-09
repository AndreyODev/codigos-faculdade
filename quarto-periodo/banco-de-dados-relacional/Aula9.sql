
-- CRIAÇÃO DA TABELA PRODUTO
CREATE TABLE produto (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    preco NUMERIC(10,2),
    categoria VARCHAR(50)
);

-- INSERINDO DADOS NA TABELA
INSERT INTO produto (nome, preco, categoria) VALUES
('Notebook Dell', 4500.00, 'Informática'),
('Mouse Logitech', 150.00, 'Informática'),
('Sofá Retrátil', 2000.00, 'Móveis'),
('Mesa de Jantar', 1200.00, 'Móveis'),
('Geladeira Brastemp', 3800.00, 'Eletrodomésticos'),
('Micro-ondas LG', 700.00, 'Eletrodomésticos'),
('Camisa Polo', 90.00, 'Vestuário'),
('Calça Jeans', 120.00, 'Vestuário');

-- View para a categoria Informática
CREATE VIEW vw_informatica AS
SELECT * FROM produto
WHERE categoria = 'Informática';

-- View para a categoria Móveis
CREATE VIEW vw_moveis AS
SELECT * FROM produto
WHERE categoria = 'Móveis';

-- View para a categoria Eletrodomésticos
CREATE VIEW vw_eletrodomesticos AS
SELECT * FROM produto
WHERE categoria = 'Eletrodomésticos';

-- View para a categoria Vestuário
CREATE VIEW vw_vestuario AS
SELECT * FROM produto
WHERE categoria = 'Vestuário';


-- CONSULTANDO AS VIEWS
SELECT * FROM vw_informatica;

SELECT * FROM vw_moveis;

SELECT * FROM vw_eletrodomesticos;

SELECT * FROM vw_vestuario;

-- Inserindo novo produto na categoria Informática
INSERT INTO produto (nome, preco, categoria)
VALUES ('Teclado Mecânico', 350.00, 'Informática');

-- Verificando atualização automática na view
SELECT * FROM vw_informatica;
