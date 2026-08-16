from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

ARQUIVO_DOACOES = "data/doacoes.csv"


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/campanhas")
def campanhas():
    return render_template("campanhas.html")

@app.route("/doacoes")
def doacoes():
    lista_doacoes = []

    with open(ARQUIVO_DOACOES, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        next(leitor, None)

        for linha in leitor:
            lista_doacoes.append(linha)

    return render_template("doacoes.html", doacoes=lista_doacoes)
@app.route("/resumo")
def resumo():
    total_doacoes = 0
    valor_total = 0

    with open(ARQUIVO_DOACOES, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        next(leitor, None)

        for linha in leitor:
            total_doacoes += 1
            try:
                valor_total += float(linha[2])
            except (ValueError, IndexError):
                pass  # Ignora linhas com valores inválidos ou incompletos

    valor_total_formatado = f"{valor_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    return render_template(
        "resumo.html",
        total_doacoes=total_doacoes,
        valor_total=valor_total_formatado
    )


@app.route("/doar", methods=["GET", "POST"])
def doar():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        valor = request.form["valor"]
        campanha = request.form["campanha"]


        arquivo_existe = os.path.exists(ARQUIVO_DOACOES)
        arquivo_vazio = not arquivo_existe or os.path.getsize(ARQUIVO_DOACOES) == 0

        with open(ARQUIVO_DOACOES, "a", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)

            if arquivo_vazio:
                escritor.writerow(["Nome", "E-mail", "Valor", "Campanha"])

            escritor.writerow([nome, email, valor, campanha])
        print("===== NOVA DOAÇÃO =====")


        print("Nome:", nome)
        print("E-mail:", email)
        print("Valor:", valor)
        print("Campanha:", campanha)
        print("=======================")

        return f"""
        <h1>💚 Obrigado, {nome}!</h1>
        <p>Sua intenção de doação foi registrada.</p>
        <p>Valor: R$ {valor}</p>
        <p>Campanha: {campanha}</p>
        <br>
        <a href="/doar">← Fazer outra doação</a>
        """

    return render_template("doar.html")

if __name__ == "__main__":
    app.run(debug=True)