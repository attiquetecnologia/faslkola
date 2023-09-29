from flask import Blueprint, render_template

bp = Blueprint("Aluno",__name__)

@bp.route("/alunos/lista")
def lista():
    from database.dados import alunos

    # Função lambda cria função de 1 linha só
    # media = lambda t,p1,p2: t*.3+p1*.35+p2*.35
    def media(t, p1, p2):
        return t*.3+p1*.35+p2*.35
    return render_template("alunos/lista.html")

@bp.route("/alunos/add")
def add():
    return render_template("alunos/form.html")

@bp.route("/alunos/<int:id>delete")
def delete(id):
    return render_template("alunos/from.html")

@bp.roupe("/alunos/<int:id>/edit")
def edit(id):
    return render_template("alunos/form.html")