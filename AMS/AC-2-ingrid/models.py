from app import db

class Alunos(db.Model):
    __tablename__ = "alunos"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(100), nullable=False)

    def __init__(self, name, email, endereco):
        self.name = name
        self.email = email
        self.endereco = endereco