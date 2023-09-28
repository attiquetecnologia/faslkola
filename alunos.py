from flask import Blueprint, redirect, render_template, request, url_for

bp = Blueprint("Aluno", __name__)

@bp.route("/alunos/lista")
def lista():
    from database.dados import alunos

    def media(t, p1 , p2):
        return t*.3+p1*.35+p2*.35

    return render_template("alunos/lista.html", media=media, alunos=alunos)

@bp.route("/alunos/add")
def add():
    return render_template("alunos/form.html")

@bp.route("/alunos/<int:id>/delete", methods=("GET", "POST"))
def delete(id):
    from database.dados import alunos

    aluno = alunos.get(id)

    if request.method == "POST" and request.form.get("apagar") == "sim":
        del alunos[id] 
        return redirect(url_for("Aluno.lista"))

    return render_template("alunos/delete.html", id=id, aluno=aluno)

@bp.route("/alunos/<int:id>edit")
def edit(id):
    return render_template("alunos/form.html")