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

if __name__ == "__main__":
    app.run(debug=True)
