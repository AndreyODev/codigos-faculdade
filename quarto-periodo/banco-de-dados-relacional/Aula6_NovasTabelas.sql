
-- CRIAÇÃO DE TABELAS
CREATE TABLE funcionarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    cargo VARCHAR(100)
);

CREATE TABLE departamentos (
    id SERIAL PRIMARY KEY,
    nome_departamento VARCHAR(100),
    localizacao VARCHAR(100)
);

-- INSERINDO DADOS NAS TABELAS
INSERT INTO funcionarios (nome, cargo) VALUES
    ('Jeferson', 'Analista de Sistemas'),
    ('Andrey', 'Desenvolvedor Backend'),
    ('Rafaella', 'Gerente de Projetos');

INSERT INTO departamentos (nome_departamento, localizacao) VALUES
    ('TI', 'Rio de Janeiro'),
    ('Recursos Humanos', 'São Paulo'),
    ('Financeiro', 'Minas Gerais');

-- INSERÇÃO DE COLUNAS (ALTER TABLE + ADD COLUMN)
ALTER TABLE funcionarios ADD COLUMN salario DECIMAL(10,2);
ALTER TABLE funcionarios ADD COLUMN departamento_id INT REFERENCES departamentos(id);

UPDATE funcionarios SET salario = 4500.00, departamento_id = 1 WHERE id = 1;
UPDATE funcionarios SET salario = 5200.00, departamento_id = 1 WHERE id = 2;
UPDATE funcionarios SET salario = 7000.00, departamento_id = 3 WHERE id = 3;

-- DELETAR UMA COLUNA
ALTER TABLE funcionarios DROP COLUMN cargo;

-- CRIAR BACKUP DE TABELA COM CONDIÇÃO WHERE
-- (Apenas funcionários com salário maior que 5000)
CREATE TABLE funcionarios_backup AS
SELECT * FROM funcionarios WHERE salario > 5000;

-- INNER JOIN: mostra apenas registros com correspondência
SELECT f.nome, f.salario, d.nome_departamento
FROM funcionarios f
INNER JOIN departamentos d ON f.departamento_id = d.id;

-- FULL JOIN: mostra todos, mesmo sem correspondência
SELECT f.nome, d.nome_departamento
FROM funcionarios f
FULL JOIN departamentos d ON f.departamento_id = d.id;

-- CROSS JOIN: combina todos com todos (produto cartesiano)
SELECT f.nome AS funcionario, d.nome_departamento
FROM funcionarios f
CROSS JOIN departamentos d;

SELECT * FROM funcionarios;
SELECT * FROM funcionarios_backup;
