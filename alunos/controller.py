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
                error = "Usuario ou senha inválidos!"

    return render_template("usuarios/login.html", error=error)

@bp.route("/perfil", methods=("GET", "POST"))
def perfil():
    # Pega dados e devolve pro hTML e recebe dados do html

    if request.method=="POST":
        # logica salvar
        nome=request.form.get("nome")

    else:
        # busca dados do banco
        from database.dados import alunos
        for k,v in alunos.items():
            if v['usuario'] == session['user']['usuario']:
                usuario = v

    return render_template('usuarios/perfil.html', usuario=usuario)