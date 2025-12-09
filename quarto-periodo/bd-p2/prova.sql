-- Usuário criado
CREATE ROLE usuario_read_Andrey LOGIN PASSWORD '1qaz'
-- Eu sei que poderia usar o CREATE USER usuario_read_Andrey WITH PASSWORD '1qaz'

-- Permissão somente de leitura
GRANT pg_read_all_data TO usuario_read_Andrey

-- Tabela de departamento
CREATE TABLE departamentos(
	id SERIAL PRIMARY KEY,
	nome VARCHAR(100) NOT NULL
);

INSERT INTO departamentos(nome) 
VALUES('Administrativo');

TRUNCATE TABLE departamentos RESTART IDENTITY CASCADE;

-- Tabela de funcionario
CREATE TABLE funcionarios(
	id SERIAL PRIMARY KEY,
	nome VARCHAR(255) NOT NULL,
 	cargo VARCHAR(255) NOT NULL,
 	salario NUMERIC(10,2) NOT NULL,
	id_departamento INTEGER NOT NULL,
	FOREIGN KEY (id_departamento) REFERENCES departamentos(id)
);

INSERT INTO funcionarios(nome, cargo, salario, id_departamento)
VALUES('Andrey', 'Administrativo', '2.250', 1);

TRUNCATE TABLE funcionarios RESTART IDENTITY CASCADE;

-- Tabela de projetos
CREATE TABLE projetos(
	id SERIAL PRIMARY KEY,
	id_funcionario INTEGER NOT NULL,
	nome VARCHAR(255) NOT NULL,
 	descricao TEXT,
	id_departamento INTEGER NOT NULL,
	FOREIGN KEY (id_departamento) REFERENCES departamentos(id),
	FOREIGN KEY (id_funcionario) REFERENCES funcionarios(id)
);

INSERT INTO projetos(nome, id_funcionario, descricao, id_departamento)
VALUES('JourneyWell', 1, 'Aplicativo voltado para os moradores e turista de Saquarema', 1);

TRUNCATE TABLE projetos RESTART IDENTITY CASCADE;

-- Tabela de log_projetos
CREATE TABLE log_projetos(
	id SERIAL PRIMARY KEY,
	id_projeto INTEGER NOT NULL,
	nome VARCHAR(100) NOT NULL,
	descricao TEXT,
	operacao VARCHAR(50) NOT NULL,
 	data_operacao TIMESTAMP DEFAULT NOW(),
	FOREIGN KEY (id_projeto) REFERENCES projetos(id)
);

SELECT * FROM log_projetos;

-- Função Trigger
CREATE OR REPLACE FUNCTION registrar_log()
RETURNS TRIGGER AS $$
BEGIN 
	IF (TG_OP = 'INSERT') THEN
		INSERT INTO log_projetos(id_projeto, nome, descricao, operacao, data_operacao)
		VALUES(
			NEW.id,
			(SELECT nome FROM funcionarios WHERE id = NEW.id_funcionario),
			NEW.descricao,
			'INSERT',
			NOW()
		);
		RETURN NEW;
		
	ELSIF (TG_OP = 'UPDATE') THEN
		INSERT INTO log_projetos(id_projeto, nome, descricao, operacao, data_operacao)
		VALUES(
			NEW.id,
			(SELECT nome FROM funcionarios WHERE id = NEW.id_funcionario),
			NEW.descricao,
			'UPDATE',
			NOW()
		);
		RETURN NEW;
		
	ELSIF (TG_OP = 'DELETE') THEN
		INSERT INTO log_projetos(id_projeto, nome, descricao, operacao, data_operacao)
		VALUES(
			OLD.id,
			(SELECT nome FROM funcionarios WHERE id = OLD.id_funcionario),
			OLD.descricao,
			'DELETE',
			NOW()
		);
		RETURN OLD;
	END IF;
END;
$$ LANGUAGE plpgsql;

-- Trigger
CREATE TRIGGER tg_log_projetos
AFTER INSERT OR UPDATE OR DELETE ON projetos
FOR EACH ROW
EXECUTE FUNCTION registrar_log();

-- View
CREATE OR REPLACE VIEW vw_funcionario_projetos AS
SELECT funcionarios.nome as funcionario, funcionarios.cargo, departamentos.nome as departamento, projetos.nome as nome_projeto, projetos.descricao
FROM projetos
JOIN funcionarios ON funcionarios.id = projetos.id_funcionario
JOIN departamentos ON departamentos.id = projetos.id_departamento

SELECT * FROM vw_funcionario_projetos;

