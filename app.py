from flask import Flask, render_template, request, jsonify
import psycopg2
import random

app = Flask(__name__, template_folder="templates")

# Conexão com o banco de dados PostgreSQL
db_connection = psycopg2.connect(
    host="localhost",  # O endereço do contêiner Docker do banco de dados
    database="tarot_db",  # O nome do banco de dados
    user="tarot_user",  # O usuário do banco de dados
    password="tarot_password"  # A senha do usuário do banco de dados
)

db_cursor = db_connection.cursor()

tarot_cards = [{"id": i, "card_name": f"Carta {i}"} for i in range(1, 37)]

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

@app.route('/embaralhar', methods=['GET'])
def embaralhar_cartas():
    try:
        # Embaralhar as cartas
        random.shuffle(tarot_cards)

        # Limpar a tabela 'tarot_shuffled_order' antes de inserir as cartas embaralhadas
        clear_table_query = "DELETE FROM tarot_shuffled_order"
        db_cursor.execute(clear_table_query)
        
        # Inserir as cartas embaralhadas na tabela 'tarot_shuffled_order'
        for index, carta in enumerate(tarot_cards):
            insert_query = "INSERT INTO tarot_shuffled_order (card_id, order_position) VALUES (%s, %s)"
            db_cursor.execute(insert_query, (carta["id"], index))
        
        db_connection.commit()

        # Retornar a ordem embaralhada das cartas como JSON
        return jsonify({"cartas_embaralhadas": tarot_cards})
    except Exception as e:
        return jsonify({"erro": str(e)})

    # Retornar a ordem embaralhada das cartas como JSON
    return jsonify({"cartas_embaralhadas": tarot_cards})

if __name__ == "__main__":
    app.run(debug=True)
