from flask import Flask, app, redirect, render_template, request, session, url_for

def create_app(): # cria uma função para definir o aplicativo
    app = Flask(__name__) # instancia o Flask
    app.secret_key = "abax"
    @app.route("/") # cria uma rota
    def index(): # função que gerencia rota
        nome = "Alexandre xandon 07"
        return render_template("index.html", nome=nome) # combina o python com html


    @app.route("/login", methods=('POST', 'GET'))
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

        return render_template("login.html", error=error)
    
    @app.route("/logout")
    def logout():
        return redirect(url_for("login"))
    
    @app.route("/recsenha", methods=('POST', 'GET'))
    def recsenha():
        error = None
        return render_template("recsenha.html", error=error)
    
    @app.route("/perfil")
    def perfil():

        if 'user' not in session and False:
            # se não tiver lgoado devolve para login
            return redirect(url_for('login'))

        # 1-Pegar dados do banco
        # for k,v ... in alunos... session['user']['email']==email

        if request.method == 'POST':
            # lógica salvar
            nome = request.form.get("nome")
            email = request.form.get("email")

            from database.dados import alunos
            for k,v,x in alunos.items():
                pass
    
        return render_template("usuarios/perfil.html") #, usuario=usuario
    
    from usuarios.controller import bp
    app.register_blueprint(bp)
    
    from alunos.controller import bp 
    app.register_blueprint(bp)
    
    return app # retorna o app criado

if __name__ == "__main__": # 'função principal' do python
    create_app().run(debug=True) # executa o flask na porta http://127.0.0.1:5000
