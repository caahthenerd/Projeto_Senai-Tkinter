from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Database import Database


class Cadastros:
    def __init__(self):
        #Area de criação da tela 
        self.janela = Tk()
        self.janela.title("Crie seu cadastro")
        self.janela.geometry("1024x768")
        self.janela.configure(bg = "#fff0d7")
        self.janela.state("zoomed")

        #Gestão de telas e frames
        self.frame1 = Frame(self.janela, bg = "#fff0d7")
        self.frame1.pack()

        self.titulo = Label(self.frame1, text= "Primeiro precisamos de alguns dados", font=("Montserrat", 30),bg = "#fff0d7")
        self.titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=30, sticky="w")

        self.labelNome = Label(self.frame1, text="Nome/Razão:", bg = "#fff0d7", font=("Montserrat", 16))
        self.labelNome.grid(row=1, column=0, padx=5, pady=10, sticky="w")
        self.txtNome = Entry(self.frame1, font=("Montserrat", 14), width=30)
        self.txtNome.grid(row=1, column=1, padx=5, pady=18, sticky="w")

        self.labelDoc = Label(self.frame1, text="CPF/CNPJ:", bg = "#fff0d7",font=("Montserrat", 16))
        self.labelDoc.grid(row=2, column=0, padx=5, pady=10, sticky="w")
        self.txtDoc = Entry(self.frame1, font=("Montserrat", 14), width=30)
        self.txtDoc.grid(row=2, column=1, padx=5, pady=18, sticky="w")

        self.labelEmail = Label(self.frame1, text="Email:", bg = "#fff0d7", font=("Montserrat", 16))
        self.labelEmail.grid(row=3, column=0, padx=5, pady=10, sticky="w")
        self.txtEmail = Entry(self.frame1, font=("Montserrat", 14), width=30)
        self.txtEmail.grid(row=3, column=1, padx=5, pady=18, sticky="w")

        self.labelTipoUsuario = Label(self.frame1, text="Tipo de Usuário:", bg = "#fff0d7", font=("Montserrat", 16))
        self.labelTipoUsuario.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.comboTipoUsuario = ttk.Combobox(self.frame1, font=("Calibri", 16), width=28, state="readonly")
        self.comboTipoUsuario["values"] = ("Associacao", "Cliente")
        self.comboTipoUsuario.grid(row=4, column=1, padx=5, pady=10, sticky="w")

        self.labelDataN = Label(self.frame1, text="Data de Nascimento:", bg = "#fff0d7", font=("Montserrat", 16))
        self.labelDataN.grid(row=5, column=0, padx=5, pady=10, sticky="w")
        self.txtDataN = Entry(self.frame1, font=("Montserrat", 14), width=30)
        self.txtDataN.grid(row=5, column=1, padx=5, pady=18, sticky="w")
        self.labelDataN = Label(self.frame1, text="Exemplo: dia/mês/ano", bg = "#fff0d7", font=("Montserrat", 12,))
        self.labelDataN.grid(row=6, column=0, padx=5, pady=0, sticky="w")


        self.labelSenha = Label(self.frame1, text="Crie uma senha: ", bg = "#fff0d7",font=("Montserrat", 16))
        self.labelSenha.grid(row=7, column=0, padx=5, pady=10, sticky="w")
        self.txtSenha = Entry(self.frame1, font=("Montserrat", 14), width=30)
        self.txtSenha.grid(row=7, column=1, padx=5, pady=18, sticky="w")

        self.labelTelefone = Label(self.frame1, text="Telefone: ", bg = "#fff0d7",font=("Montserrat", 16))
        self.labelTelefone.grid(row=8, column=0, padx=5, pady=10, sticky="w")
        self.txtTelefone = Entry(self.frame1, font=("Montserrat", 14), width=30)
        self.txtTelefone.grid(row=8, column=1, padx=5, pady=18, sticky="w")


        self.frame2 = Frame(self.frame1, bg= "#fff0d7")
        self.frame2.grid(row=9, column=0, columnspan=4, padx=10, pady=10, sticky="w")
        self.cancelar =  Button(self.frame2, text="Cancelar", width=15, command=self.close, font=("Montserrat", 16, "bold"), bg="#776621", fg="#ffffff")
        self.cancelar.grid(row=0, column=0, padx=10, pady= 10)
        self.continuar =  Button(self.frame2, text="Continuar", width=15, command=self.add_cliente,font=("Montserrat", 16, "bold"), bg="#7387a0")
        self.continuar.grid(row=0, column=1, padx=10, pady= 10)

        mainloop()

    #Funções
    def add_cliente(self):

        if self.txtNome.get() != "" and self.txtDataN.get() != "" and self.txtTelefone.get() != "" and self.txtEmail.get() != "" and self.txtSenha.get() != "" and self.txtDoc.get() != self.comboTipoUsuario.get() != "":
            cadUser = Database
            cadUser.nome = self.txtNome.get()
            cadUser.dataN = self.txtDataN.get()
            cadUser.telefone = self.txtTelefone.get()
            cadUser.email = self.txtEmail.get()
            cadUser.senha = self.txtSenha.get()
            cadUser.docUser = self.txtDoc.get()
            cadUser.tipousuario = self.comboTipoUsuario.get()
            msg = cadUser.insertUser(cadUser)
            if msg == "Tudo certo":
                messagebox.showinfo("Sucesso", "Cadastro Concluído!")
            else:
                messagebox.showerror("Erro", "Erro ao cadastrar! Solicite suporte do desenvolvedor.")
        else:
            messagebox.showerror("Info", "Preencha todos os campos!")

    def close(self):
        exit()


        