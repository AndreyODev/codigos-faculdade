CREATE DATABASE escola;

CREATE TABLE alunos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    curso VARCHAR(100)
);

CREATE TABLE professores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    disciplina VARCHAR(100)
);

CREATE TABLE matriculas (
    id SERIAL PRIMARY KEY,
    aluno_id INT REFERENCES alunos(id),
    data DATE
);

-- Criando Usuário
CREATE USER andrey WITH PASSWORD '1qaz2wsx';

-- Concedendo Permissões
GRANT CONNECT ON DATABASE escola TO andrey;
GRANT USAGE ON SCHEMA public TO andrey;

GRANT SELECT ON alunos TO andrey;
GRANT INSERT, UPDATE, DELETE ON matriculas To andrey;

-- Inserções
INSERT INTO alunos (nome, curso) VALUES
('Andrey', 'Engenharia de software'),
('Rafaella', 'Pedagogia'),
('Jeferson', 'Engenharia da computação');

INSERT INTO professores (nome, disciplina) VALUES
('Bandeira', 'Matemática'),
('Gioliano', 'Programação');

-- inserções feitas pelo usuário
INSERT INTO matriculas (aluno_id, data) VALUES
(1, '2025-01-01'),
(2, '2025-02-10'),
(3, '2025-03-05');

-- Updates
UPDATE matriculas SET data = '2025-01-10' WHERE id = 1;
UPDATE matriculas SET data = '2025-02-15' WHERE id = 2;

-- Delete
DELETE FROM matriculas WHERE id = 3;

-- Revogando a permissão do usuário
REVOKE INSERT, UPDATE, DELETE ON matriculas FROM andrey;

-- Permitindo que o usuáio leia as tabelas
GRANT SELECT ON public.alunos, public.professores, public.matriculas TO andrey;


