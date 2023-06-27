import sqlite3
class Conexao:
    def __init__(self):

        self.conexao = sqlite3.connect("bd_produto.db")

        self.createTable()

    def createTable(self):

        c = self.conexao.cursor()

        c.execute("CREATE TABLE IF NOT EXISTS produtos(idproduto INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nomeproduto TEXT,qtdestoque INT, lote INT, fabricacao TEXT,validade TEXT, valor TEXT, datainsercaoproduto TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

        self.conexao.commit()
        c.close()