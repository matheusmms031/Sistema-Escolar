from flask import Flask

app = Flask(__name__)

@app.route("/help")
def pagina_ajuda():
    return "<p>PÁGINA HELP DA API</p>"

@app.route("/alunos/add", methods=['POST']) # Deve ser POST pois um formulário HTML aceita...
def add_aluno(): # Adiciona alunos no banco
    
    
@app.route("/alunos/atualizar", methods=['PATCH'])
def modificar_aluno(): # Modifica aluno X no banco
    