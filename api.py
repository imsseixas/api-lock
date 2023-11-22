from flask import Flask, jsonify
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configurações do banco de dados
db = None

try:
    db = mysql.connector.connect(
        host='lock_dart.mysql.dbaas.com.br',
        port=3306,
        user='lock_dart',
        password='Dart#Lock23',
        database='lock_dart'
    )
    print("Conexão ao banco de dados bem-sucedida!")
except mysql.connector.Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
    # Tratar o erro, como registrar ou notificar alguém responsável

@app.route('/dados', methods=['GET'])
def obter_dados():
    if db is None:
        return jsonify({'error': 'Erro ao conectar ao banco de dados'})

    try:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM usuarios')
        dados = cursor.fetchall()
        cursor.close()
        return jsonify(dados)
    except mysql.connector.Error as e:
        print(f"Erro ao executar a consulta SQL: {e}")
        # Aqui você pode lidar com o erro de acordo com sua lógica de aplicação
        return jsonify({'error': 'Erro ao obter dados do banco de dados'})

if __name__ == '__main__':
    app.run(debug=True)
