from app import app
from models.ModelConn import ClienteModel

@app.route('/Cadastrar/', methods=["GET"])
def index():
    return ClienteModel.cadastrarEmail()