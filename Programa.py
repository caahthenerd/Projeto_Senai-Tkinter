from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Produtos import Produtos
# import sqlite3
#produto_viewer.py
class Programa:
    def __init__(self):
        # Janela principal
        self.janela = Tk()
        self.janela.title("Raizes da Caatinga")
        self.janela.configure(bg="#fff0d7")
        largura = 600
        altura = 300
        self.janela.geometry(f"{largura}x{altura}")

        # Conexão com o BD
        # self.conexao = sqlite3.connect("bd_produto.db")
        # self.cursor = self.conexao.cursor()

    

        # Busca dos produtos no banco de dados
        self.produtos = []
        self.buscar_produtos()

        # PanedWindow para dividir a janela
        self.paned_window = PanedWindow(self.janela, orient=HORIZONTAL)
        self.paned_window.pack(fill=BOTH, expand=True)

        self.frame_lista = Frame(self.paned_window, bg="#fff0d7")
        self.paned_window.add(self.frame_lista)

        self.label_pesquisa = Label(self.frame_lista, text="Pesquisar produto:", bg="#fff0d7")
        self.label_pesquisa.pack()

        self.entry_pesquisa = Entry(self.frame_lista, width=30)
        self.entry_pesquisa.pack()

        self.button_pesquisa = Button(self.frame_lista, text="Pesquisar", command=self.pesquisar)
        self.button_pesquisa.pack()

        self.listbox_resultados = Listbox(self.frame_lista, width=40)
        self.listbox_resultados.pack(fill=BOTH, expand=True)

        self.listbox_resultados.bind("<<ListboxSelect>>", self.mostrar_detalhes)

        self.frame_detalhes = Frame(self.paned_window, bg="#fff0d7")
        self.paned_window.add(self.frame_detalhes)

        self.label_detalhes = Label(self.frame_detalhes, text="Detalhes do Produto:", bg="#fff0d7")
        self.label_detalhes.pack()

        self.label_nome = Label(self.frame_detalhes, text="", bg="#fff0d7")
        self.label_nome.pack()

        self.label_preco = Label(self.frame_detalhes, text="", bg="#fff0d7")
        self.label_preco.pack()

        self.label_qtdestoque = Label(self.frame_detalhes, text="", bg="#fff0d7")
        self.label_qtdestoque.pack()

        self.label_lote = Label(self.frame_detalhes, text="", bg="#fff0d7")
        self.label_lote.pack()

        self.label_fabricacao = Label(self.frame_detalhes, text="", bg="#fff0d7")
        self.label_fabricacao.pack()

        self.label_validade = Label(self.frame_detalhes, text="", bg="#fff0d7")
        self.label_validade.pack()

        self.mostrar_resultados()  # Chamar o método aqui para exibir os resultados

        mainloop()

    def mostrar_resultados(self, resultados=None):
        self.listbox_resultados.delete(0, END)

        if not resultados:
            resultados = self.produtos

        if resultados:
            for produto in resultados:
                self.listbox_resultados.insert(END, produto.nomeproduto)
        else:
            self.listbox_resultados.insert(END, "Nenhum resultado encontrado.")

    def pesquisar(self):
        termo_pesquisa = self.entry_pesquisa.get()
        resultados = []

        for produto in self.produtos:
            if termo_pesquisa.lower() in produto.nomeproduto.lower():
                resultados.append(produto)

        self.mostrar_resultados(resultados)


    def mostrar_detalhes(self, event):
        selecionado = self.listbox_resultados.curselection()

        if selecionado:
            indice = selecionado[0]
            nome_produto = self.listbox_resultados.get(indice)  # Obtém o texto selecionado na lista
            produto_selecionado = None

            # Encontra o objeto Produto correspondente ao nome selecionado
            for produto in self.produtos:
                if produto.nomeproduto == nome_produto:
                    produto_selecionado = produto
                    break

            if produto_selecionado:
                self.label_nome.config(text=f"Nome: {produto_selecionado.nomeproduto}")
                self.label_preco.config(text=f"Preço: R${'{:.2f}'.format(float(produto_selecionado.valor))}")
                self.label_qtdestoque.config(text=f"Estoque: {produto_selecionado.qtdestoque}")
                self.label_lote.config(text=f"Lote: {produto_selecionado.lote}")
                self.label_fabricacao.config(text=f"Fabricação: {produto_selecionado.fabricacao}")
                self.label_validade.config(text=f"Validade: {produto_selecionado.validade}")
            else:
                self.label_nome.config(text="")
                self.label_preco.config(text="")
                self.label_qtdestoque.config(text="")
                self.label_lote.config(text="")
                self.label_fabricacao.config(text="")
                self.label_validade.config(text="")
        else:
            self.label_nome.config(text="")
            self.label_preco.config(text="")
            self.label_qtdestoque.config(text="")
            self.label_lote.config(text="")
            self.label_fabricacao.config(text="")
            self.label_validade.config(text="")


    def buscar_produtos(self):
        # self.cursor.execute("SELECT idproduto, nomeproduto, qtdestoque, lote, fabricacao, validade, valor FROM produtos")
        # rows = self.cursor.fetchall()
        # for row in rows:
        #     idproduto = row[0]
        #     nomeproduto = row[1]
        #     qtdestoque = row[2]
        #     lote = row[3]
        #     fabricacao = row[4]
        #     validade = row[5]
        #     valor = row[6]
        produto = Produtos(self.idproduto,self.nomeproduto, self.qtdestoque, self.lote,self.fabricacao, self.validade, self.valor)
        self.produtos.append(produto)

    # def __del__(self):
    #     self.conexao.close()

# class Produto:
#     def __init__(self, idproduto, nomeproduto, qtdestoque, lote, fabricacao, validade, valor):
#         self.idproduto = idproduto
#         self.nomeproduto = nomeproduto
#         self.qtdestoque = qtdestoque
#         self.lote = lote
#         self.fabricacao = fabricacao
#         self.validade = validade
#         self.valor = valor

t = Programa()
