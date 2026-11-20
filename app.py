from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def status_servico():
    return jsonify({
        "disciplina": "Computação Orientada a Serviços",
        "ferramenta": "CircleCI",
        "status": "Serviço ativo"
    })

if __name__ == "__main__":
    app.run()
