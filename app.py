from flask import Flask, render_template, request, jsonify
import psycopg2

app = Flask(__name__)

# Conexão com o banco de dados PostgreSQL
db_connection = psycopg2.connect(
    host="localhost",  # O endereço do contêiner Docker do banco de dados
    database="tarot_db",  # O nome do banco de dados
    user="tarot_user",  # O usuário do banco de dados
    password="tarot_password"  # A senha do usuário do banco de dados
)

db_cursor = db_connection.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST'])
def cadastrar():
    nome = request.form.get('name')
    email = request.form.get('email')

    # Inserir o usuário no banco de dados
    inserir_usuario(nome, email)

    mensagem = f'Boas-vindas, {nome}! Seu cadastro foi realizado com sucesso.'

    return jsonify({"mensagem": mensagem})

def inserir_usuario(nome, email):
    insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    db_cursor.execute(insert_query, (nome, email))
    db_connection.commit()

@app.route('/listar', methods=['GET'])
def listar():
    # Conectar ao banco de dados
    db_connection = psycopg2.connect(
        host="localhost",
        database="tarot_db",
        user="tarot_user",
        password="tarot_password"
    )

    # Criar um cursor para executar consultas SQL
    db_cursor = db_connection.cursor()

    try:
        # Executar uma consulta SQL para obter os dados que você deseja listar
        db_cursor.execute("SELECT * FROM users")
        
        # Buscar todos os resultados da consulta
        resultados = db_cursor.fetchall()
        
        # Criar uma lista para armazenar os resultados
        lista_usuarios = []

        # Estruturar os resultados em um formato adequado (por exemplo, uma lista de dicionários)
        for resultado in resultados:
            usuario = {
                'id': resultado[0],
                'nome': resultado[1],
                'email': resultado[2]
            }
            lista_usuarios.append(usuario)

        # Retornar os dados em formato JSON
        return jsonify({"usuarios": lista_usuarios})
    except Exception as e:
        return jsonify({"erro": str(e)})
    finally:
        # Fechar o cursor e a conexão com o banco de dados
        db_cursor.close()
        db_connection.close()

if __name__ == "__main__":
    app.run(debug=True)
