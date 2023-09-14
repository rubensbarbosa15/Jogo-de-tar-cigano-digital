from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL

mysql = MySQL()
app = Flask(__name__)

#app.template_folder = "templates" 

app.config['MYSQL_HOST'] = '172.19.0.3'  # Altere para o endereço IP correto
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'tarot_password'
app.config['MYSQL_DB'] = 'tarot_db'

mysql.init_app(app)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST'])
def cadastrar():
    nome = request.form.get('name')
    email = request.form.get('email')

    conn = mysql.connect()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (nome, email) VALUES (%s, %s)", (nome, email))  # Alterado para 'nome'
        conn.commit()
        mensagem = f'Boas-vindas, {nome}! Seu cadastro foi realizado com sucesso.'
    except Exception as e:
        conn.rollback()
        mensagem = f'Erro ao cadastrar usuário: {str(e)}'
    finally:
        cursor.close()
        conn.close()

    return jsonify({"mensagem": mensagem})

@app.route('/listar', methods=['GET'])
def listar():
    conn = mysql.connect()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM users")
        resultados = cursor.fetchall()
        lista_usuarios = []

        for resultado in resultados:
            usuario = {
                'id': resultado[0],
                'nome': resultado[1],  # Alterado para 'nome'
                'email': resultado[2]
            }
            lista_usuarios.append(usuario)

    except Exception as e:
        mensagem = f'Erro ao listar usuários: {str(e)}'
    finally:
        cursor.close()
        conn.close()

    return jsonify({"usuarios": lista_usuarios})

if __name__ == "__main__":
    app.run(debug=True)
