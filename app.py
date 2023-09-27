from flask import Flask, redirect, render_template, request, session, url_for, flash

def create_app(): # cria uma função para definir o aplicativo
    app = Flask(__name__) # instancia o Flask
    app.secret_key = "abax"
    @app.route("/") # cria uma rota
    def index(): # função que gerencia rota
        nome = "Rodrigo 123"
        return render_template("index.html", nome=nome) # combina o python com html

    @app.route("/alunos")
    def alunos():
        import json
        from database.dados import alunos

        # Função lambda cria funções de 1 linha só
        # media = lambda t,p1,p2: t*.3+p1*.35+p2*.35
        def media(t, p1, p2):
            return t*.3+p1*.35+p2*.35
        
        return render_template("lista.html", alunos=alunos, media=media )

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
        session.clear()
        return redirect(url_for("index"))

    @app.route("/perfil")
    def perfil():
        if 'user' not in session:
            flash("Usuário não está logado!")
            return redirect(url_for("login"))
        
        if request.method == "POST": # lógica para salvar
            pass
        
        # senão pega usuario no banco
        from database.dados import alunos
        for k,v in alunos.items():
            if v.get("usuario") == session['user'].get("usuario"):
                usuario = v # {"nome": "Batman", "t": 9.1, "p1": 8.5, "p2": 9, "avatar": url_for('static', filename="images/batman.jpg"), "usuario":"batman@email.com", "senha":"curinga"}
        
        return render_template("perfil.html", usuario=usuario)

    from componentes import bp
    app.register_blueprint(bp)

    from alunos import bp
    app.register_blueprint(bp)

    return app # retorna o app criado

if __name__ == "__main__": # 'função principal' do python
    create_app().run(debug=True) # executa o flask na porta http://127.0.0.1:5000