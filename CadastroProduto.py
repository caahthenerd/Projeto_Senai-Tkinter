from Produtos import Produtos
from tkinter import *
from tkinter import messagebox

class Tela:

    def __init__(self):
        self.janela = Tk()
        self.janela.title("Cadastro de Produtos")
        # self.janela.geometry("768x768")
        self.janela.config(bg = "#fae2b6")
        self.janela.state("zoomed")
        self.fonte = ("Verdana", 15)
        self.bgpadrao = ("#fae2b6")

        self.frame1 = Frame(self.janela, bg=self.bgpadrao)
        self.frame1.pack(fill=X)


        #Adicionando formulário na tela
        self.titulo = Label(self.frame1, text="Cadastrar Produto", font=("Calibri", 18,     "bold"), bg=self.bgpadrao, fg="black")
        self.titulo.grid(row=0, padx=10, pady=10)

        self.labelNome = Label(self.frame1, text="Nome do produto: ", font=self.fonte,  width=15, bg=self.bgpadrao)
        self.textNome = Entry(self.frame1, width=25, font=self.fonte)
        self.labelNome.grid(row=1, column=0)
        self.textNome.grid(row=1, column=1,  sticky="w")


        self.labelEstoque = Label(self.frame1, text="Quantidade em estoque: ", bg=self. bgpadrao, font=self.fonte, width=20)
        self.textEstoque = Entry(self.frame1, width= 25, font=self.fonte)
        self.labelEstoque.grid(row=1, column=3)
        self.textEstoque.grid(row=1, column=4,  sticky="w")


        self.labelLote = Label(self.frame1, text="Lote do produto: ", bg=self.bgpadrao,     font=self.fonte, width=20)
        self.textLote = Entry(self.frame1, width= 25, font=self.fonte)
        self.labelLote.grid(row=2, column=0)
        self.textLote.grid(row=2, column=1,  sticky="w")


        self.labelFabricacao = Label(self.frame1, text="Data de fabricação: ", bg=self. bgpadrao, font=self.fonte, width=20)
        self.textFabricacao = Entry(self.frame1, width= 25, font=self.fonte)
        self.labelFabricacao.grid(row=2, column=3)
        self.textFabricacao.grid(row=2, column=4,  sticky="w")


        self.labelValidade = Label(self.frame1, text="Validade: ", bg=self.bgpadrao, font=self. fonte, width=20)
        self.textValidade = Entry(self.frame1, width= 25, font=self.fonte)
        self.labelValidade.grid(row=3, column=0)
        self.textValidade.grid(row=3, column=1,  sticky="w")


        self.labelValor = Label(self.frame1, text="Valor: ", bg=self.bgpadrao, font=self.   fonte, width=20)
        self.textValor = Entry(self.frame1, width= 25, font=self.fonte)
        self.labelValor.grid(row=3, column=3)
        self.textValor.grid(row=3, column=4,  sticky="w")


        self.inserirproduto = Button(self.frame1, width=12, text="Inserir Produto", command=self.salvarProdutosNoBD, font=self.fonte, bg="#776621",fg="white")
        self.inserirproduto.grid(row=4, column=1, pady=10, padx=10)

        mainloop()  

    def salvarProdutosNoBD(self):
        osProdutos = Produtos
        osProdutos.nomeproduto = self.textNome.get()
        osProdutos.qtdestoque = self.textEstoque.get()
        osProdutos.lote = self.textLote.get()
        osProdutos.fabricacao = self.textFabricacao.get()
        osProdutos.validade = self.textValidade.get()
        osProdutos.valor = self.textValor.get()
        print(osProdutos.nomeproduto)
        messagebox.showinfo("Info", osProdutos.insertProduto(osProdutos))
