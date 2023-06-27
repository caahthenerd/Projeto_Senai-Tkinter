import sqlite3
class ConexaoCad:
    def __init__(self):

        self.conexao = sqlite3.connect("usuarios.db")

        self.createTable()

    def createTable(self):

        c = self.conexao.cursor()

        c.execute("CREATE TABLE IF NOT EXISTS usuarios(idusuario INTEGER PRIMARY KEY, nome TEXT, dataN TEXT, telefone TEXT, email TEXT, senha TEXT, docUser TEXT, tipousuario TEXT)")

        self.conexao.commit()
        c.close()