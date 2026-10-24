from flask import Blueprint, render_template, request, jsonify

from app import db
from app.models import User

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/api/cadastro", methods=["POST"])
def cadastro():

    dados = request.json

    usuario = User(
        cnpj=dados["cnpj"],
        cpf=dados["cpf"],
        password=dados["password"]
    )

    db.session.add(usuario)
    db.session.commit()

    return jsonify({
        "mensagem": "Usuário cadastrado"
    }), 201