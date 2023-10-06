from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy import select
from database.connection import db
from .model import Aluno

bp = Blueprint("Aluno", __name__)

@bp.route("/alunos/lista")
def lista():
    lista = db.session.scalars(select(Aluno))
    # Função lambda cria funções de 1 linha só
    # media = lambda t,p1,p1: t* .3+p1*.35+p2*.35
    def media(t, p1, p2):
        return t*.3+p1* .35+p2* .35

    return render_template("alunos/lista.html", lista=lista, media=media)

@bp.route("/aluno/add")
def add():
    
    erros = []

    if request.method=="POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        t = float(request.form.get("t"))
        p1 = float(request.form.get("p1"))
        p2 = float(request.form.get("p2"))

        #validações
        if not nome: erros.append("Nome é um campo obrigatório")
        if not email: erros.append("Email é um campo obrigatório")
        if not t or t <0 or t >10: erros.append("Trabalho é um campo obrigatório ou valores não entre 0-10")
        if not p1 or p1 <0 or p1 >10: erros.append("Prova 1 é um campo obrigatório ou valores não entre 0-10")
        if not p2 or p2 <0 or p2 >10: erros.append("Prova 2 é um campo obrigatório ou valores não entre 0-10")
   
        if len(erros) == 0:
            aluno = Aluno(**{"nome" : nome, "email": email, "t": t, "p1": p1,"p2": p2})
            db.session.add(aluno)
            db.session.commit() #|persiste no

            flash(f"Usuário {nome}, salvo com sucesso!")

            return redirect(url_for("Aluno.edit", id=id))
        
    return render_template("alunos/form.html", erros=erros)



@bp.route("/alunos/<int:id>/delete", methods=("GET", "POST"))
def delete(id):
    from database.dados import alunos

    aluno = alunos.get(id)

    if request.method == "POST" and request.form.get("apagar") == "sim":
        del alunos[id] 
        return redirect(url_for("Aluno.lista"))

    return render_template("alunos/delete.html", id=id, aluno=aluno)

@bp.route("/alunos/<int:id>/edit", methods= ("GET", "POST"))
def edit(id):
    
    erros = []
    aluno = Aluno.query.filter_by(id=id). first()

    if request.method=="POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        t = float(request.form.get("t"))
        p1 = float(request.form.get("p1"))
        p2 = float(request.form.get("p2"))

        #validações
        if not nome: erros.append("Nome é um campo obrigatório")
        if not email: erros.append("Email é um campo obrigatório")
        if not t or t <0 or t >10: erros.append("Trabalho é um campo obrigatório ou valores não entre 0-10")
        if not p1 or p1 <0 or p1 >10: erros.append("Prova 1 é um campo obrigatório ou valores não entre 0-10")
        if not p2 or p2 <0 or p2 >10: erros.append("Prova 2 é um campo obrigatório ou valores não entre 0-10")

        if email in str(aluno): erros.append("Email já registrado")

        if len(erros) == 0:
            aluno.nome = nome
            aluno.email= email
            aluno.t= t
            aluno.p1= p1
            aluno.p2 = p2
            db.session.add(Aluno)
            db.session.commit()

            flash(f"Usuário {nome}, salvo com sucesso!")

            return redirect(url_for("Aluno.edit", id=id))

    return render_template("alunos/lista.html", id=id, erros=erros)