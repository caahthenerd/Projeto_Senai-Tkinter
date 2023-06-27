from ConexaoCad import ConexaoCad

class Database(object):
    def _init_(self):

        self.idusuario = 0
        self.nome = ""
        self.dataN = ""
        self.telefone = ""
        self.email = ""
        self.senha = ""
        self.docUser = ""
        self.tipousuario = ""

    def insertUser(self):
        conn = ConexaoCad()
        try:
            c = conn.conexao.cursor()
            c.execute("INSERT INTO usuarios(nome, dataN, telefone, email, senha, docUser, tipousuario) VALUES(?, ?, ?, ?, ?, ?, ?)", (self.nome, self.dataN, self.telefone, self.email, self.senha, self.docUser, self.tipousuario))
            conn.conexao.commit()
            c.close()

            return "Tudo certo"
        
        except(RuntimeError, TypeError, NameError):

            return "Deu Ruim"

    def selectUser(self, email, tipousuario, senha):
        conn = ConexaoCad()
        try:
            c = conn.conexao.cursor()
            c.execute("select nome,email,tipousuario from usuarios where email=? and tipousuario=? and senha = ?", (email,tipousuario, senha))
            for dados in c:
                self.nome = dados[0]
                self.email = dados[1]
                self.tipousuario = dados[2]
            print(dados)
            c.close()

            return dados

        except(RuntimeError, TypeError, NameError):

            return "Ocorreu um erro ao buscar usuario"