from copypinterest import database, app
from copypinterest.models import Usuario, Foto

with app.app_context():
    database.create_all()