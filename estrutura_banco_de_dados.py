# SQLAlchemy
from flask import Flask # Criar um API flask
from flask_sqlalchemy import SQLAlchemy # Criar banco de dados

# Criar um API flask
app = Flask(__name__)

# Criar uma instância de SQLAlchemy
app.config['SECRET_KEY'] = 'PATY@123' # gerar acesso de autenticação
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.igzpznoqkyinbneistkl:3l8f5cIHWHw1SqNT@aws-0-us-east-1.pooler.supabase.com:6543/postgres'
 # localização do banco de dados

db = SQLAlchemy(app)
db:SQLAlchemy

# Definir a estrutura da tabela Postagem
# id_postagem, titulo, autor
class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor')) # nome da tabela

# Definir a estrutura da tabela Autor
# id_autor, nome, email, senha, admin, postagens
class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem') # nome da classe

# Executar o comando para criar o banco de dados
def inicializar_banco():
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Criar usuários adminstradores
        autor = Autor(nome='paty',email='paty@email.com',senha='123456',admin=True)
        db.session.add(autor) # adicionar o autor ao banco de dados
        db.session.commit() # salvar

if __name__ == '__main__':
    inicializar_banco()