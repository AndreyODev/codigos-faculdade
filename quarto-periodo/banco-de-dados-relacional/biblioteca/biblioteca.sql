CREATE TYPE tipo_usuario AS ENUM('aluno', 'funcionario');
CREATE TYPE status AS ENUM('devolvido', 'em andamento');

CREATE ROLE superusuario LOGIN PASSWORD '1qaz'
CREATE ROLE usuario LOGIN PASSWORD '2wsx'

GRANT pg_read_all_data TO superusuario

GRANT pg_write_all_data TO superusuario

GRANT USAGE ON SCHEMA public TO usuario

GRANT SELECT ON vw_detalhada TO usuario

CREATE TABLE usuarios(
	id SERIAL PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	tipo tipo_usuario NOT NULL
);

INSERT INTO usuarios(nome, tipo)
VALUES('Andrey', 'aluno');

INSERT INTO usuarios(nome, tipo)
VALUES('Gabryella', 'aluno');

UPDATE usuarios
SET nome = 'Jeferson'
WHERE id = 1

SELECT * FROM usuarios;

TRUNCATE TABLE usuarios RESTART IDENTITY CASCADE; 

CREATE TABLE livros(
	id SERIAL PRIMARY KEY,
	titulo VARCHAR(100)
);

INSERT INTO livros(titulo) 
VALUES('The secret');

INSERT INTO livros(titulo) 
VALUES('The call of the wild');

TRUNCATE TABLE livros RESTART IDENTITY CASCADE; 

CREATE TABLE emprestimos(
	id SERIAL PRIMARY KEY,
	id_usuario INTEGER NOT NULL,
	id_livro INTEGER NOT NULL,
	data_emprestimo TIMESTAMP DEFAULT NOW(),
	data_devolucao TIMESTAMP NULL, 
	status status NOT NULL,
	FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
	FOREIGN KEY (id_livro) REFERENCES livros(id)
);

INSERT INTO emprestimos(id_usuario, id_livro, status)
VALUES(1,1, 'em andamento'); 

INSERT INTO emprestimos(id_usuario, id_livro, status)
VALUES(2,2, 'em andamento'); 

UPDATE emprestimos
SET status = 'devolvido', data_devolucao = NOW()
WHERE id = 1

TRUNCATE TABLE emprestimos RESTART IDENTITY CASCADE;

CREATE TABLE log_emprestimo(
	id SERIAL PRIMARY KEY,
	id_usuario INTEGER NOT NULL,
	id_livro INTEGER NOT NULL,
	id_emprestimo INTEGER NOT NULL,
	tipo_usuario VARCHAR(100),
	data_emprestimo TIMESTAMP DEFAULT NOW(),
	data_devolucao TIMESTAMP NULL, 
	status status NOT NULL,
	tipo_operacao VARCHAR(100),
	FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
	FOREIGN KEY (id_livro) REFERENCES livros(id),
	FOREIGN KEY (id_emprestimo) REFERENCES emprestimos(id)
);

CREATE OR REPLACE FUNCTION registrar_log()
RETURNS TRIGGER AS $$
BEGIN 
	IF (TG_OP = 'INSERT') THEN 
		INSERT INTO log_emprestimo(id_usuario, id_livro, id_emprestimo, tipo_usuario, data_emprestimo, data_devolucao, status, tipo_operacao)
		VALUES (
			NEW.id_usuario,
			NEW.id_livro,
			NEW.id,
			(SELECT nome FROM usuarios WHERE id = NEW.id_usuario),
			NEW.data_emprestimo,
			NEW.data_devolucao,
			NEW.status,
			'INSERT'
		);
		RETURN NEW;
	ELSIF (TG_OP = 'UPDATE') THEN 
		INSERT INTO log_emprestimo(id_usuario, id_livro, id_emprestimo, tipo_usuario, data_emprestimo, data_devolucao, status, tipo_operacao)
		VALUES (
			NEW.id_usuario,
			NEW.id_livro,
			NEW.id,
			(SELECT nome FROM usuarios WHERE id = NEW.id_usuario),
			NEW.data_emprestimo,
			NEW.data_devolucao,
			NEW.status,
			'UPDATE'
		);
		RETURN NEW;
	ELSIF (TG_OP = 'DELETE') THEN 
		INSERT INTO log_emprestimo(id_usuario, id_livro, id_emprestimo, tipo_usuario, data_emprestimo, data_devolucao, status, tipo_operacao)
		VALUES (
			OLD.id_usuario,
			OLD.id_livro,
			OLD.id,
			(SELECT nome FROM usuarios WHERE id = OLD.id_usuario),
			OLD.data_emprestimo,
			OLD.data_devolucao,
			OLD.status,
			'DELETE'
		);
		RETURN OLD;
	END IF;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER tg_log_emprestimo
AFTER INSERT OR UPDATE OR DELETE ON emprestimos 
FOR EACH ROW
EXECUTE FUNCTION registrar_log();

SELECT * FROM log_emprestimo;

CREATE OR REPLACE VIEW vw_detalhada AS 
SELECT usuarios.nome, livros.titulo, emprestimos.data_emprestimo, emprestimos.data_devolucao, emprestimos.status
FROM emprestimos
JOIN usuarios ON usuarios.id = emprestimos.id_usuario
JOIN livros ON livros.id = emprestimos.id_livro

SELECT * FROM vw_detalhada;

