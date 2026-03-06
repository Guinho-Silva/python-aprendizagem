"""Flask é framework para construir aplicações web em python
"""

from flask import Flask


# __name__= __main__

app = Flask(__name__)

@app.route("/") # rota de inicialização

def mensagem():
    return "Hello word!"

@app.route("/about")

def about():

    return "Pagina sobre"

    
if __name__ =="__main__":
    app.run(debug=True)