from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "segredo_super_seguro"  # Necessário para usar sessões

@app.route("/")
def index():
    return render_template("index.html")

# ---------------------------
# 🧩 MODO 1: Usuário adivinha
# ---------------------------
@app.route("/user_guess", methods=["GET", "POST"])
def user_guess():
    if "numero_computador" not in session:
        session["numero_computador"] = random.randint(1, 100)
        session["tentativas_usuario"] = 0

    resultado = ""

    if request.method == "POST":
        palpite = int(request.form.get("palpite"))
        session["tentativas_usuario"] += 1
        numero_computador = session["numero_computador"]

        if palpite == numero_computador:
            resultado = f"🎉 Parabéns! Você acertou o número {numero_computador} em {session['tentativas_usuario']} tentativas!"
            session.pop("numero_computador")
            session.pop("tentativas_usuario")
        elif palpite < numero_computador:
            resultado = "Seu palpite é menor que o número correto."
        else:
            resultado = "Seu palpite é maior que o número correto."

    return render_template("user_guess.html", resultado=resultado)


# --------------------------------
# 🧠 MODO 2: Computador adivinha
# --------------------------------
@app.route("/computer_guess", methods=["GET", "POST"])
def computer_guess():
    # Inicializa variáveis de sessão se ainda não existem
    if "computador_min" not in session:
        session["computador_min"] = 1
        session["computador_max"] = 100
        session["tentativas_pc"] = 0
        session["numero_usuario"] = None

    mensagem = ""
    palpite = None

    if request.method == "POST":
        # Primeiro envio — usuário escolhe número
        if session["numero_usuario"] is None:
            session["numero_usuario"] = int(request.form.get("numero_usuario"))
            session["tentativas_pc"] = 0

        # Calcula palpite do computador
        palpite = (session["computador_min"] + session["computador_max"]) // 2
        session["tentativas_pc"] += 1

        # Verifica resposta do usuário
        resposta = request.form.get("resposta")

        if resposta == "maior":
            session["computador_min"] = palpite + 1
        elif resposta == "menor":
            session["computador_max"] = palpite - 1
        elif resposta == "acertou":
            mensagem = (
                f"🎯 Computador acertou o número {session['numero_usuario']} "
                f"em {session['tentativas_pc']} tentativas!"
            )
            # Reinicia variáveis para novo jogo
            session.pop("computador_min")
            session.pop("computador_max")
            session.pop("numero_usuario")
            session.pop("tentativas_pc")
            return render_template("computer_guess.html", mensagem=mensagem, fim=True)

        # Atualiza o novo palpite
        palpite = (session["computador_min"] + session["computador_max"]) // 2
        mensagem = f"💭 Computador chutou {palpite}..."

    return render_template("computer_guess.html", mensagem=mensagem, palpite=palpite, fim=False)


if __name__ == "__main__":
    app.run(debug=True)
