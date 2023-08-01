from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)

# Verifica o valor da variável de ambiente DEBUG
# Se for "0", usa a URI do banco de dados da variável DATABASE_URL
# Se for qualquer outra coisa ou não estiver definida, usa o banco de dados SQLite local
if os.getenv("DEBUG") == "0":
    link_banco = os.getenv("DATABASE_URL")
else:
    link_banco = "sqlite:///comunidade.db"  # Note a adição de "///" para o banco de dados SQLite

app.config["SQLALCHEMY_DATABASE_URI"] = link_banco
app.config["SECRET_KEY"] = "a3190c71717b80582c2b580d8bc02528"
app.config["UPLOAD_FOLDER"] = "static/fotos_posts"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"

from copypinterest import routes
