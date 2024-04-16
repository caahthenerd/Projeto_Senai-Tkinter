from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Database import Database
from Cadastros import Cadastros
from InicialPag import InicialPag

class Login:
    def __init__(self):
        #Configurando a janela
        self.janela = Tk()
        self.janela.title("Tela de Login")
        self.janela["bg"] = "#fae2b6"

        #Logo
        self.img = PhotoImage(file='logo-caatinga.png')
        self.labelImg = Label(image=self.img) 
        self.labelImg.pack(padx=10,pady=5)

        #Formulário
        self.labelTipoUsuario = Label(self.janela, text="Logar como:",
                                bg="#fae2b6",
                                font=("Calibri", 16,))
        self.labelTipoUsuario.pack()
        self.comboTipoUsuario = ttk.Combobox(
        font=("Calibri", 16), width=22, state="readonly")
        self.comboTipoUsuario["values"] = ("Associacao", "Cliente")
        self.comboTipoUsuario.pack(padx=10, pady=10)

        self.label_usuario = Label(self.janela, text="Email:", font=("Calibri", 22))
        self.label_usuario.pack()
        self.label_usuario.pack(padx=10)
        self.label_usuario["bg"] = "#fae2b6"
        self.entry_usuario = Entry(self.janela, width=30,font=("Calibri", 15))
        self.entry_usuario.pack()

        self.label_senha = Label(self.janela, text="Senha:", font=("Calibri", 22))
        self.label_senha.pack()
        self.label_senha["bg"] = "#fae2b6"

        self.entry_senha = Entry(self.janela, show="*", width=30,font=("Calibri", 15))
        self.entry_senha.pack()

        self.button_login = Button(self.janela, text="Entrar",font=("Calibri", 15, "bold"), command=self.verificar_login, width=10)
        self.button_login.pack(pady=5, padx=5)
        self.button_login["bg"] = "#d9a56c"

        self.label_cadastro = Label(self.janela, text="Não é cadastrado?", font=("Calibri", 12))
        self.label_cadastro.pack()
        self.label_cadastro["bg"] = "#fae2b6"
        
        self.button_cadastro = Button(self.janela, text="Realizar Cadastro", font=("Calibri", 15, "bold"), width=20, bg="#7387a0")
        self.button_cadastro.bind("<Button-1>", self.realizarCadastro)
        self.button_cadastro.pack(pady=5)
        
        mainloop()

        #Função de verificar usuario
    def verificar_login(self):
        validaUser = Database
        tipousuario = self.comboTipoUsuario.get()
        email = self.entry_usuario.get()
        senha = self.entry_senha.get()
        if tipousuario != "" or email != "" or senha != "":
            msg = validaUser.selectUser(self, email, tipousuario, senha)
            # Salva os dados da sessão em um arquivo de texto 
            if msg != "Ocorreu um erro ao buscar usuario":
                # messagebox.showinfo("Info", "Usuario encontrado")
                with open("session.txt", "w") as file:
                    file.write(f"TipoUsuario: {tipousuario}\n")
                    file.write(f"Email: {email}\n")
                self.janela.destroy()
                InicialPag()
            else:
                messagebox.showerror("Info", "Verifique login e senha!")
        else: 
            messagebox.showinfo("Info", "Preencha todos os campos!")
    
    def realizarCadastro(self, event):
        # self.janela.destroy()
        Cadastros()

t = Login()
