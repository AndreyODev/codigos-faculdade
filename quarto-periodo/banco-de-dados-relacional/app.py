from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

# Ajuste conforme seu ambiente / pgAdmin
DB_NAME = "univassouras_db"   # <-- coloque o nome correto do seu DB
DB_USER = "postgres"
DB_PASSWORD = "@Sedutornato2"
DB_HOST = "localhost"

def get_connection():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST
    )
    # força cliente para UTF8 (útil se houver mismatch)
    conn.set_client_encoding('UTF8')
    return conn

@app.route('/aluno', methods=['POST'])
def add_aluno():
    data = request.get_json()
    nome = data.get('nome')
    idade = data.get('idade')
    curso = data.get('curso')

    if not nome or not idade or not curso:
        return jsonify({'error': 'Dados incompletos'}), 400

    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO alunos (nome, idade, curso) VALUES (%s, %s, %s)",
            (nome, int(idade), curso)
        )
        conn.commit()
        return jsonify({'message': 'Aluno inserido com sucesso'}), 201
    except psycopg2.Error as e:
        if conn:
            conn.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

@app.route('/alunos', methods=['GET'])
def get_alunos():
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM alunos ORDER BY id")
        alunos = cur.fetchall()
        return jsonify(alunos)
    except psycopg2.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

@app.route('/professor', methods=['POST'])
def add_professor():
    data = request.get_json()
    nome = data.get('nome')
    disciplina = data.get('disciplina')

    if not nome or not disciplina:
        return jsonify({'error': 'Dados incompletos'}), 400

    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO professores (nome, disciplina) VALUES (%s, %s)",
            (nome, disciplina)
        )
        conn.commit()
        return jsonify({'message': 'Professor inserido com sucesso'}), 201
    except psycopg2.Error as e:
        if conn:
            conn.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

@app.route('/professores', methods=['GET'])
def get_professores():
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM professores ORDER BY id")
        professores = cur.fetchall()
        return jsonify(professores)
    except psycopg2.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)
