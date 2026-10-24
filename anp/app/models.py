from app import db


class User(db.Model):

    cnpj = db.Column(db.String(18), unique=True, nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<User {self.cpf}>"