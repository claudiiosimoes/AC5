from app import app
from flask_mysqldb import MySQL

mysql = MySQL(app)


class ClienteModel():

    def cadastrarEmail():
        name = 'João Ayrton'
        email = 'exemplo@hotmail.com'
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO clientes (nome, email, telefone) VALUES(%s,%s)''',(name,email))
        mysql.connection.commit()
        cursor.close()

        return 'Email cadastrado com sucesso!'