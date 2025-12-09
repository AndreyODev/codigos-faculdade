--Aluno: Andrey de Oliveira Nunes
--Matrícula: 202411297

--a) Problemas:  É dito que a normalização é uma forma de organizar os 
-- dados dentro da tabela, onde essa organização requer que você siga 3 regras.
-- 1° regra é o 1FN, que diz que não pode ter mais de uma informação na célula e que os dados devem ser único,
-- no caso dessa tabela desnormalizada, vemos que a várias repetições. 
-- 2° regra é o 2FN, que diz que cada tabela precisa ter um tema principal, como assim? Exemplo:
-- Se temos uma tabela chamada aluno, nessa tabela aluno só deve ter informações relacionadas ao aluno(Nome, CPF......),
-- No caso dessa tabela desnormalizada, vemos que temos vários temas, usuario, livro, emprestimo....
-- 3° regra é o 3FN, que diz que as colunas da tabela não pode depender de outra coluna a não ser que seja a coluna da primary key dessa tabela, 
-- No caso dessa tabela desnormalizada, vemos que a data da devolução vai depender da coluna data_emprestimo, então logo deveria ter uma tabela de emprestimo para essas duas colunas. 


-- CRIANDO A TABELA DE USUÁRIOS
CREATE TABLE usuarios(
	id_usuario SERIAL PRIMARY KEY,
	nome_usuario VARCHAR(100)
);
-- Abaixo está sendo feito as inserções
INSERT INTO usuarios(nome_usuario) 
VALUES ('Zé da Manga');

INSERT INTO usuarios(nome_usuario) 
VALUES ('Zé das Couves');

INSERT INTO usuarios(nome_usuario) 
VALUES ('Goku da Silva');

INSERT INTO usuarios(nome_usuario) 
VALUES ('Titi de Cabral da Silva');

INSERT INTO usuarios(nome_usuario) 
VALUES ('Andrey de Oliveira Nunes');

INSERT INTO usuarios(nome_usuario) 
VALUES ('Rafella Oliveira Faria');

SELECT * FROM usuarios;

-- CRIANDO A TABELA DE CURSO
-- ESTOU CRIANDO A TABELA CURSO PORQUE O CURSO
-- ESTAVA SE REPETINDO NA TABELA DE USUÁRIO, O QUE ACABA NÃO SENDO CORRETO PORQUE
-- NA 1FN DIZ QUE A CÉLULA PRECISA CONTER APENAS 1 INFORMAÇÃO E PRECISA SER ÚNICA PARA EVITAR REPETIÇÃO

CREATE TABLE curso(
	id_curso SERIAL PRIMARY KEY,
	nome_curso VARCHAR(100),
	usuario_id INTEGER,
	FOREIGN KEY (usuario_id) REFERENCES usuarios(id_usuario)
);
-- Abaixo está sendo feito as inserções
INSERT INTO curso (nome_curso, usuario_id)
VALUES('Engenharia', 1);

INSERT INTO curso (nome_curso, usuario_id)
VALUES('Computação', 2);

INSERT INTO curso (nome_curso, usuario_id)
VALUES('Engenharia', 3);

INSERT INTO curso (nome_curso, usuario_id)
VALUES('Administração', 4);

INSERT INTO curso (nome_curso, usuario_id)
VALUES('Análise e desenvolvimento de sistemas', 5);

INSERT INTO curso (nome_curso, usuario_id)
VALUES('Pedagogia', 6);

-- Questão 3 – Atualizações
-- Aqui atualizei o curso do Titi de Cabral da Silva  
UPDATE curso
SET nome_curso = 'Recursos Humanos' WHERE id_curso = 3

SELECT * FROM curso;

-- CRIANDO A TABELA DE MATRICULA
-- ESTOU CRIANDO A TABELA DE MATRICULA PORQUE A MATRÍCULA
-- ESTAVA SE REPETINDO NA TABELA DE USUÁRIO, O QUE ACABA NÃO SENDO CORRETO PORQUE
-- NA 1FN DIZ QUE A CÉLULA PRECISA CONTER APENAS 1 INFORMAÇÃO E PRECISA SER ÚNICA PARA EVITAR REPETIÇÃO
-- CRIANDO A TABELA DE LIVROS

CREATE TABLE matricula(
	id_matricula SERIAL PRIMARY KEY,
	matricula INTEGER, 
	usuario_id INTEGER,
	FOREIGN KEY (usuario_id) REFERENCES usuarios(id_usuario)
);
-- Abaixo está sendo feito as inserções
INSERT INTO matricula(matricula, usuario_id) 
VALUES(2023001, 1);

INSERT INTO matricula(matricula, usuario_id) 
VALUES(2023002, 2);

INSERT INTO matricula(matricula, usuario_id) 
VALUES(2023003, 3);

INSERT INTO matricula(matricula, usuario_id) 
VALUES(2023004, 4);

INSERT INTO matricula(matricula, usuario_id) 
VALUES(2023005, 5);

INSERT INTO matricula(matricula, usuario_id) 
VALUES(2023006, 6);

SELECT * FROM matricula;

CREATE TABLE livro(
	id_livro SERIAL PRIMARY KEY,
	titulo_livro VARCHAR(100),
	autor_livro VARCHAR(100),
	usuario_id INTEGER,
	matricula_id INTEGER,
	curso_id INTEGER,
	FOREIGN KEY (usuario_id) REFERENCES usuarios(id_usuario),
	FOREIGN KEY (matricula_id) REFERENCES matricula(id_matricula),
	FOREIGN KEY (curso_id) REFERENCES curso(id_curso)
);
-- Abaixo está sendo feito as inserções
INSERT INTO livro (titulo_livro, autor_livro, usuario_id, matricula_id, curso_id)
VALUES('Estrutura de Dados', 'N.Wirth', 1, 1, 1);

INSERT INTO livro (titulo_livro, autor_livro, usuario_id, matricula_id, curso_id)
VALUES('Banco de Dados', 'C.Date', 2, 2, 2);

INSERT INTO livro (titulo_livro, autor_livro, usuario_id, matricula_id, curso_id)
VALUES('Redes de Computadores', 'A.Tanenbaum', 3, 3, 1);

INSERT INTO livro (titulo_livro, autor_livro, usuario_id, matricula_id, curso_id)
VALUES('Estatística Aplicada', 'R.Bussab', 4, 4, 3);

INSERT INTO livro (titulo_livro, autor_livro, usuario_id, matricula_id, curso_id)
VALUES('The secret', 'Não sei', 5, 5, 5);

INSERT INTO livro (titulo_livro, autor_livro, usuario_id, matricula_id, curso_id)
VALUES('O segredo da mente milionária', 'Não sei', 6, 6, 6);

INSERT INTO livro (titulo_livro, autor_livro, usuario_id, matricula_id, curso_id)
VALUES('Compiladores', 'A.Aho', 1, 1, 1);

INSERT INTO livro (titulo_livro, autor_livro, usuario_id, matricula_id, curso_id)
VALUES('Sistemas Operacionais', 'S.Silbershatz', 2, 2, 2);

INSERT INTO livro (titulo_livro, autor_livro, usuario_id, matricula_id, curso_id)
VALUES('Inteligência Artificial', 'S.Russell', 3, 3, 1);

INSERT INTO livro (titulo_livro, autor_livro, usuario_id, matricula_id, curso_id)
VALUES('Gestão de projetos', 'H.Kerzner', 4, 4, 4);

SELECT * FROM livro;

-- CRIANDO A TABELA DE EMPRÉSTIMO
CREATE TABLE emprestimo(
	id_emprestimo SERIAL PRIMARY KEY,
	data_emprestimo DATE,
	data_devolucao DATE,
	usuario_id INTEGER,
	livro_id INTEGER,
	matricula_id INTEGER,
	curso_id INTEGER,
	FOREIGN KEY (usuario_id) REFERENCES usuarios(id_usuario),
	FOREIGN KEY (livro_id) REFERENCES livro(id_livro),
	FOREIGN KEY (matricula_id) REFERENCES matricula(id_matricula),
	FOREIGN KEY (curso_id) REFERENCES curso(id_curso)
);
-- Abaixo está sendo feito as inserções
INSERT INTO emprestimo (data_emprestimo, data_devolucao, usuario_id, livro_id, matricula_id, curso_id)
VALUES('2025-01-15', '2025-01-30', 1, 1, 1, 1);

INSERT INTO emprestimo (data_emprestimo, data_devolucao, usuario_id, livro_id, matricula_id, curso_id)
VALUES('2025-02-01', NULL, 2, 2, 2, 2);

INSERT INTO emprestimo (data_emprestimo, data_devolucao, usuario_id, livro_id, matricula_id, curso_id)
VALUES('2025-02-15', '2025-02-25', 3, 3, 3, 1);

INSERT INTO emprestimo (data_emprestimo, data_devolucao, usuario_id, livro_id, matricula_id, curso_id)
VALUES('2025-02-12', '2025-03-01', 4, 4, 4, 4);

INSERT INTO emprestimo (data_emprestimo, data_devolucao, usuario_id, livro_id, matricula_id, curso_id)
VALUES('2025-09-10', '2025-09-22', 5, 5, 5, 5);

INSERT INTO emprestimo (data_emprestimo, data_devolucao, usuario_id, livro_id, matricula_id, curso_id)
VALUES('2025-08-07', NULL, 6, 6, 6, 6);

-- Questão 3 – Deleções
DELETE FROM emprestimo WHERE data_devolucao = '2025-02-25';

SELECT id_emprestimo as id_registro, data_emprestimo, data_devolucao, usuario_id, livro_id, matricula_id, curso_id FROM emprestimo;

-- Questão 5 – Consultas com JOIN

SELECT 
	usuarios.id_usuario,
	usuarios.nome_usuario,
	curso.nome_curso, 
	livro.id_livro,
	livro.titulo_livro,
	livro.autor_livro,
	emprestimo.id_emprestimo,
	emprestimo.data_emprestimo,
	emprestimo.data_devolucao
FROM 
	usuarios
INNER JOIN curso ON id_usuario = id_curso
INNER JOIN livro ON id_usuario = id_livro
INNER JOIN emprestimo ON id_usuario = id_emprestimo
	
