-- a) Por que a tabela não está na 1FN?

-- A tabela não está na Primeira Forma Normal (1FN) porque:

-- Porque os atributos possui mais de uma de uma informação na célula (ex: endereco_cliente junta rua e número).

-- Mistura de informações de clientes, livros e empréstimos na mesma tabela.

CREATE TABLE clientes (
    id_cliente SERIAL PRIMARY KEY,
    nome_cliente VARCHAR(100) NOT NULL,
    endereco_cliente VARCHAR(200) NOT NULL
);

-- Inserindo clientes
INSERT INTO clientes (nome_cliente, endereco_cliente)
VALUES 
('Zé da Manga', 'Rua das Flores, 123'),
('Zé das Couves', 'Av. Brasil, 456'),
('Zé das Nuves', 'Praça Central, 789');

-- Atualizar endereço do cliente
UPDATE clientes
SET endereco_cliente = 'Rua Nova, 999'
WHERE id_cliente = 1;

CREATE TABLE livros (
    id_livro SERIAL PRIMARY KEY,
    titulo_livro VARCHAR(150) NOT NULL,
    autor_livro VARCHAR(100) NOT NULL
);

-- Inserindo livros
INSERT INTO livros (titulo_livro, autor_livro)
VALUES
('Dom Casmurro', 'Machado de Assis'),
('Capitães da Areia', 'Jorge Amado'),
('Vidas Secas', 'Graciliano Ramos');

CREATE TABLE emprestimo (
    id_emprestimo SERIAL PRIMARY KEY,
    data_emprestimo DATE,
    data_devolucao DATE,
    cliente_id INTEGER,
    livro_id INTEGER,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id_cliente),
    FOREIGN KEY (livro_id) REFERENCES livros(id_livro)
);

-- Inserindo empréstimos
INSERT INTO emprestimo (data_emprestimo, data_devolucao,cliente_id, livro_id)
VALUES
('2025-01-10', '2025-01-20', 1, 1),
('2025-02-05', NULL, 2, 2),
('2025-01-15', '2025-01-28', 3, 3);

-- Registrar devolução atrasada
UPDATE emprestimo
SET data_devolucao = '2025-03-20'
WHERE id_emprestimo = 2;

SELECT c.nome_cliente, l.titulo_livro, e.data_emprestimo
FROM emprestimo e
JOIN clientes c ON e.cliente_id = c.id_cliente
JOIN livros l ON e.livro_id = l.id_livro
WHERE e.data_devolucao IS NULL;


