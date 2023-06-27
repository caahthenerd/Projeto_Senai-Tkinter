from Conexao import Conexao

class Produtos(object):
    def __init__(self):

        self.idproduto = 0
        self.nomeproduto = ""
        self.qtdestoque = ""
        self.lote = ""
        self.fabricacao = ""
        self.validade = ""
        self.valor = ""
        self.datainsercaoproduto = 0

    def insertProduto(self):
        conn = Conexao()
        # print(self.nomeproduto)
        try:
            c = conn.conexao.cursor()
            c.execute("insert into produtos(nomeproduto, qtdestoque, lote,fabricacao, validade, valor) values(?, ?, ?, ?, ?, ?)",(self.nomeproduto, self.qtdestoque, self.lote, self.fabricacao, self.validade, self.valor))
            conn.conexao.commit()
            c.close()

            return "Produto cadastrado!"

        except(RuntimeError, TypeError, NameError):

            return "Erro no cadastro do produto!"
        
    def buscar_produtos():
        conn = Conexao()
        cursor = conn.conexao.cursor()
        cursor.execute("SELECT idproduto, nomeproduto, qtdestoque, lote, fabricacao, validade, valor FROM produtos")
        rows = cursor.fetchall()
        return rows
    

    def selectProduto(id):
        conn = Conexao()
        try:
            c = conn.conexao.cursor()
            c.execute("SELECT * FROM produtos where idproduto= ?",str(id))
            return c.fetchall()[0]
        except(RuntimeError, TypeError, NameError):
            return "Ocorreu um erro ao buscar produtos"