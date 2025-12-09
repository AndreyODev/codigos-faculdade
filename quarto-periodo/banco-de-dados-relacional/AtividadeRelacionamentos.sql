--
-- PostgreSQL database dump
--

\restrict hQQkEMILcjzLo2Odd0Lehn7HQcSUoBbbnYTsd1sgXaLPNg0tDSHAac0gxlT1A1h

-- Dumped from database version 17.6
-- Dumped by pg_dump version 17.6

-- Started on 2025-09-08 11:11:11

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 219 (class 1259 OID 24603)
-- Name: alunos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alunos (
    id_aluno integer NOT NULL,
    nome character varying(100),
    matricula character varying(10),
    email character varying(100),
    curso_id integer
);


ALTER TABLE public.alunos OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 24588)
-- Name: cursos_disciplinas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cursos_disciplinas (
    id_curso integer NOT NULL,
    nome_curso character varying(100),
    codigo character varying(10),
    disciplina character varying(100),
    periodo character varying(20),
    professor_id integer
);


ALTER TABLE public.cursos_disciplinas OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 24633)
-- Name: ensalamento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ensalamento (
    id_ensalamento integer NOT NULL,
    curso_id integer,
    sala_id integer,
    professor_id integer,
    data_hora timestamp without time zone
);


ALTER TABLE public.ensalamento OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 24583)
-- Name: professores; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.professores (
    id_professores integer NOT NULL,
    nome character varying(100),
    email character varying(100),
    departamento character varying(100)
);


ALTER TABLE public.professores OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 24613)
-- Name: salas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.salas (
    id_sala integer NOT NULL,
    numero_sala character varying(100),
    capacidade integer,
    localizacao character varying(100)
);


ALTER TABLE public.salas OWNER TO postgres;

--
-- TOC entry 4818 (class 0 OID 24603)
-- Dependencies: 219
-- Data for Name: alunos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alunos (id_aluno, nome, matricula, email, curso_id) FROM stdin;
1	Rafaella	202511400	rafaella@gmal.com	1
2	Gabryella	202512500	gabryela@gmal.com	1
\.


--
-- TOC entry 4817 (class 0 OID 24588)
-- Dependencies: 218
-- Data for Name: cursos_disciplinas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cursos_disciplinas (id_curso, nome_curso, codigo, disciplina, periodo, professor_id) FROM stdin;
1	Engenharia de Software	1qaz	Algoritmo	1° Período	1
2	Administração	2wsx	Pacote office	3° Período	1
3	Engenharia de Software	1qaz	Algoritmo	1° Período	2
\.


--
-- TOC entry 4820 (class 0 OID 24633)
-- Dependencies: 221
-- Data for Name: ensalamento; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ensalamento (id_ensalamento, curso_id, sala_id, professor_id, data_hora) FROM stdin;
1	2	1	2	2025-09-07 14:01:50
\.


--
-- TOC entry 4816 (class 0 OID 24583)
-- Dependencies: 217
-- Data for Name: professores; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.professores (id_professores, nome, email, departamento) FROM stdin;
1	Andrey	andrey@gmail.com	Acadêmico
2	Andrey	jeferson@gmail.com	Administrativo
\.


--
-- TOC entry 4819 (class 0 OID 24613)
-- Dependencies: 220
-- Data for Name: salas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.salas (id_sala, numero_sala, capacidade, localizacao) FROM stdin;
1	Laboratório 1	50	BLOCO 1
\.


--
-- TOC entry 4661 (class 2606 OID 24607)
-- Name: alunos alunos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alunos
    ADD CONSTRAINT alunos_pkey PRIMARY KEY (id_aluno);


--
-- TOC entry 4659 (class 2606 OID 24592)
-- Name: cursos_disciplinas cursos_disciplinas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cursos_disciplinas
    ADD CONSTRAINT cursos_disciplinas_pkey PRIMARY KEY (id_curso);


--
-- TOC entry 4665 (class 2606 OID 24637)
-- Name: ensalamento ensalamento_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ensalamento
    ADD CONSTRAINT ensalamento_pkey PRIMARY KEY (id_ensalamento);


--
-- TOC entry 4657 (class 2606 OID 24587)
-- Name: professores professores_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.professores
    ADD CONSTRAINT professores_pkey PRIMARY KEY (id_professores);


--
-- TOC entry 4663 (class 2606 OID 24617)
-- Name: salas salas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.salas
    ADD CONSTRAINT salas_pkey PRIMARY KEY (id_sala);


--
-- TOC entry 4667 (class 2606 OID 24608)
-- Name: alunos alunos_curso_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alunos
    ADD CONSTRAINT alunos_curso_id_fkey FOREIGN KEY (curso_id) REFERENCES public.cursos_disciplinas(id_curso);


--
-- TOC entry 4666 (class 2606 OID 24593)
-- Name: cursos_disciplinas cursos_disciplinas_professor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cursos_disciplinas
    ADD CONSTRAINT cursos_disciplinas_professor_id_fkey FOREIGN KEY (professor_id) REFERENCES public.professores(id_professores);


--
-- TOC entry 4668 (class 2606 OID 24638)
-- Name: ensalamento ensalamento_curso_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ensalamento
    ADD CONSTRAINT ensalamento_curso_id_fkey FOREIGN KEY (curso_id) REFERENCES public.cursos_disciplinas(id_curso);


--
-- TOC entry 4669 (class 2606 OID 24648)
-- Name: ensalamento ensalamento_professor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ensalamento
    ADD CONSTRAINT ensalamento_professor_id_fkey FOREIGN KEY (professor_id) REFERENCES public.professores(id_professores);


--
-- TOC entry 4670 (class 2606 OID 24643)
-- Name: ensalamento ensalamento_sala_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ensalamento
    ADD CONSTRAINT ensalamento_sala_id_fkey FOREIGN KEY (sala_id) REFERENCES public.salas(id_sala);


-- Completed on 2025-09-08 11:11:12

--
-- PostgreSQL database dump complete
--

\unrestrict hQQkEMILcjzLo2Odd0Lehn7HQcSUoBbbnYTsd1sgXaLPNg0tDSHAac0gxlT1A1h

