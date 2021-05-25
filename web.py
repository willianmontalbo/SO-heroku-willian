import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "amigo vc nem eh um passaro, vc nao possui bico nem penas, muito menos asas, eu duvido que algum especialista da area da taxonomia um dia poderia considerar vc como um passaro, sinto muita pena da sua vida miseravel e como voce tirou a vida de meu amigo a sangue frio, não consigo sentir a minima empatia por um ser como voce, espero que vc repense seus conceitos e tome um bom rumo com a tua vida"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
