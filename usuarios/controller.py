from flask import Blueprint, request, url_for, session, redirect, render_template

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

    return render_template("/login.html", error=error)

@bp.route("/logout")
def logout():
    return redirect(url_for("login"))

@bp.route("/perfil", methods=('POSTE', 'GET'))
def perfil():
        
        # 1-Pegar dados do banco

        # for k,v in alunos... session ['user']['email']==email
        
        if request.method == "POST":
            #logica salvar
            nome = request.form.get("nome")
        return render_template("perfil.html")


@bp.route("/registro", methods=('POSTE', 'GET'))
def regitro():
     return render_template("registro.html")