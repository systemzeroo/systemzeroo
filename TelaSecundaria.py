from tkinter import *
import NameFind

# Funções
def GerarTela():
    root2 = Tk()
    root2.title("Cadastro")
    # root.iconbitmap(default = "icon.png")
    root2.geometry("300x310")
    root2.resizable(width=FALSE, height=FALSE)

    # Titulo
    titulo = Label(root2, text='Preencha os dados abaixo', font='Arial 10 bold')
    titulo.place(x=60, y=0)

    # Label e Entry --> Nome
    nomeLabel = Label(root2, text='Nome', font='Arial 10')
    nomeLabel.place(x=10, y=25)
    nome = Entry(root2, width= 37)
    nome.place(x=60, y=25)

    # Label e Entry --> E-mail
    emailLabel = Label(root2, text='E-mail', font='Arial 10')
    emailLabel.place(x=10, y=50)
    email = Entry(root2, width= 37)
    email.place(x=60, y=50)

    # Label e Entry --> Senha
    senhaLabel = Label(root2, text='Senha', font='Arial 10')
    senhaLabel.place(x=10, y=75)
    senha = Entry(root2, width=37, show='*')
    senha.place(x=60, y=75)

    # Titulo2
    titulo2 = Label(root2, text='Sites Favoritos', font='Arial 10 bold')
    titulo2.place(x=100, y=100)

    # Label e Entry --> Site1
    site1label = Label(root2, text='1º Site', font='Arial 10')
    site1label.place(x=10, y= 130)
    site1 = Entry(root2, width=37)
    site1.place(x=60, y=130)

    # Label e Entry --> Site2
    site2label = Label(root2, text='2º Site', font='Arial 10')
    site2label.place(x=10, y= 160)
    site2 = Entry(root2, width=37)
    site2.place(x=60, y=160)

    # Label e Entry --> Site3
    site3 = Label(root2, text='3º Site', font='Arial 10')
    site3.place(x=10, y= 190)
    site3 = Entry(root2, width=37)
    site3.place(x=60, y=190)

    # Label e Entry --> Site4
    site4label = Label(root2, text='4º Site', font='Arial 10')
    site4label.place(x=10, y= 220)
    site4 = Entry(root2, width=37)
    site4.place(x=60, y=220)

    # Label e Entry --> Site5
    site5label = Label(root2, text='5º Site', font='Arial 10')
    site5label.place(x=10, y= 250)
    site5 = Entry(root2, width=37)
    site5.place(x=60, y=250)

    def EnviarDados():
        NameFind.AddName(nome.get(), site1.get(), site2.get(), site3.get(), site4.get(), site5.get())
        root2.destroy()
        import Face_Capture_With_Rotate
        Face_Capture_With_Rotate

    # Config btnIniciarSessao
    btnEnviarDados = Button(root2, text='Enviar Dados', command=EnviarDados)
    btnEnviarDados.place(x=110, y=280)

    root2.mainloop()




