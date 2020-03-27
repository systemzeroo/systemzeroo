from tkinter import *
import cv2

# Funções
def bt_onclick():
    import index
    import Recogniser_Video_LBPHFace

def TelaSecundaria():
    root.destroy()
    import TelaSecundaria
    TelaSecundaria.GerarTela()

# Configurações da página
root = Tk()
root.update()
root.title("System Zero")
# root.iconbitmap(default = "icon.png")
root.geometry("300x100")
root.resizable(width=FALSE, height=FALSE)

# Label e Entry --> E-mail
emailLabel = Label(root, text ='E-mail', font='Arial 10 bold')
emailLabel.place(x=10, y=10)

email = Entry(root, width=37)
email.place(x=60, y=12)

# Label e Entry --> Senha
senhaLabel = Label(root,text ='Senha', font='Arial 10 bold')
senhaLabel.place(x=10, y=35)

senha = Entry(root, width = 37, show='*')
senha.place(x=60, y=37)

# Config btnIniciarSessao
btnIniciarSessao = Button(root, text ='Iniciar Sessão', command= bt_onclick)
btnIniciarSessao.place(x=70, y=65)

# Config btnCriarConta
btnCriarConta = Button(root,text ='Criar Conta', command= TelaSecundaria)
btnCriarConta.place(x=170, y=65)

root.mainloop()