from flask import Blueprint, request, url_for, redirect, flash, render_template, session

bp = Blueprint("Usuario", __name__) 

@bp.route("/login", methods=('POST', 'GET'))
def login():
    error = None
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        from database.dados import alunos
        for k,v in alunos.items():
            if email == v.get('usuario') and senha == v.get('senha'):
                session['user'] = v
                return redirect(url_for('index'))
        else:
            error = "usuario ou senha inválidos!"

    return render_template("usuarios/login.html", error=error) 