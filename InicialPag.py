from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Produtos import Produtos
from CadastroProduto import Tela 

class InicialPag:
    def __init__(self):
        # Janela principal
        self.janela = Tk()
        self.janela.title("Raizes da Caatinga")
        self.janela.configure(bg="#fff0d7")
        largura = 600
        altura = 300
        self.janela.geometry(f"{largura}x{altura}")
        # PanedWindow para dividir a janela
        self.paned_window = PanedWindow(self.janela, orient=HORIZONTAL)
        self.paned_window.pack(fill=BOTH, expand=True)

        self.frame_lista = Frame(self.paned_window, bg="#fff0d7")
        self.paned_window.add(self.frame_lista)

        self.buttonCadastrarProduto = Button(self.frame_lista, text="Cadastrar Produtos", font=("Calibri", 10, "bold"), bg="#7387a0", fg="#ffffff")
        self.buttonCadastrarProduto.bind("<Button-1>", self.direcionarCadastro)
        self.buttonCadastrarProduto.pack(padx=10, pady=10)

        self.label_pesquisa = Label(self.frame_lista, text="Pesquisar produto:", bg="#fff0d7", font=("Calibri", 10, "bold"))
        self.label_pesquisa.pack()

        self.entry_pesquisa = Entry(self.frame_lista, width=30, font=("Calibri", 12))
        self.entry_pesquisa.pack()

        self.button_pesquisa = Button(self.frame_lista, text="Pesquisar", bg="#9a511f",font=("Calibri", 10, "bold"), fg="#ffffff", command=self.pesquisar)
        self.button_pesquisa.pack(padx=5, pady=5)

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

        self.mostrar_resultados() 

        mainloop()

    def mostrar_resultados(self):
        self.listbox_resultados.delete(0, END)
        produto = Produtos
        lista = produto.buscar_produtos()
        for produto in lista:
            self.listbox_resultados.insert(END, produto[1])
        if (len(lista) == 0):
            self.listbox_resultados.insert(END, "Nenhum resultado encontrado.")

    def pesquisar(self):
        termo_pesquisa = self.entry_pesquisa.get()
        resultados = []

        for produto in self.produtos:
            if termo_pesquisa.lower() in produto.nomeproduto.lower():
                resultados.append(produto)

        self.mostrar_resultados(resultados)


    def mostrar_detalhes(self, event):
        produtoObj = Produtos
        selecionado = self.listbox_resultados.curselection()
        indice = selecionado[0]
        produto = produtoObj.selectProduto(indice + 1)

        self.label_nome.config(text=f"Nome: {produto[1]}")
        self.label_preco.config(text=f"Preço: R${produto[6]}")
        self.label_qtdestoque.config(text=f"Estoque: {produto[2]}")
        self.label_lote.config(text=f"Lote: {produto[3]}")
        self.label_fabricacao.config(text=f"Fabricação: {produto[4]}")
        self.label_validade.config(text=f"Validade: {produto[5]}")

    def direcionarCadastro(self, event):
        self.janela.destroy()
        Tela()
