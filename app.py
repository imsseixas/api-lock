from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configurações do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lock_dart:Dart#Lock23@lock_dart.mysql.dbaas.com.br:3306/lock_dart'
app.config['SQLALCHEMY_POOL_RECYCLE'] = 300  # Recicla conexões a cada 300 segundos

db = SQLAlchemy(app)

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    cod_usuario = db.Column(db.Integer, primary_key=True)
    bars_code = db.Column(db.String(255))  # Assumindo que 'bars_code' é uma string de até 255 caracteres
    # Adicione outras colunas correspondentes à sua tabela

@app.route('/dados', methods=['GET'])
def obter_dados():
    try:
        usuarios = Usuario.query.all()
        dados = [
            {'cod_usuario': usuario.cod_usuario, 'bars_code': usuario.bars_code}
            for usuario in usuarios
        ]
        return jsonify(dados)
    except Exception as e:
        print(f"Erro ao obter dados do banco de dados: {e}")
        return jsonify({'error': 'Erro ao obter dados do banco de dados'})

if __name__ == '__main__':
    app.run(debug=True)
    
