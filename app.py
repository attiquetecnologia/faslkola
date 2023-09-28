from flask import Flask, redirect, render_template, request, session, url_for


def create_app():
    app = Flask(__name__)
    app.secret_key = "abax"

    @app.route("/home")
    def home():
        nome = "Rodrigo 123"
        return render_template("index.html", nome=nome)

    @app.route("/alunos")
    def alunos():
        import json
        from database.dados import alunos

        def media(t, p1, p2):
            return t * 0.3 + p1 * 0.35 + p2 * 0.35

        return render_template("lista.html", alunos=alunos, media=media)

    @app.route("/", methods=["POST", "GET"])
    def index():
        error = ""
        if request.method == "POST":
            email = request.form.get("email")
            senha = request.form.get("senha")

            from database.dados import alunos

            for k, v in alunos.items():
                if email == v.get("email") and senha == v.get("senha"):
                    session["user"] = v
                    return redirect(url_for("home"))
                else:
                    error = "Usuário ou senha inválidos!"

        return render_template("login.html", error=error)

    @app.route("/recuperar", methods=["POST", "GET"])
    def recuperar():
        return render_template("recuperarsenha.html")

    @app.route("/registro", methods=["POST", "GET"])
    def registro():
        if request.method == "POST":
            email = request.form.get("email")
            senha = request.form.get("senha")
            nome = request.form.get("nome")

            user_info = {
                "email": email,
                "senha": senha,
                "nome": nome,
            }
            from database.dados import alunos
            
            alunos[email]=user_info 

            return redirect(url_for("index"))

        return render_template("registro.html")

    return app

if __name__ == "__main__":
    create_app().run(debug=True)