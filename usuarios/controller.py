from flask import Blueprint, request, session, url_for, redirect, flash, render_template  # importa bibliotecas


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
                error = "Usuario ou senha inválidos!"

    return render_template("usuarios/login.html", error=error)

@bp.route("/logout", methods=('POSTE', 'GET'))
def logout():
    return redirect(url_for("login"))

@bp.route("/perfil", methods=('POSTE', 'GET'))
def perfil():
    pass

@bp.route("/recuperarsenha", methods=('POST', 'GET'))
def recuperarsenha():
    error = None
    return render_template("recuperarsenha.html", error=error)
