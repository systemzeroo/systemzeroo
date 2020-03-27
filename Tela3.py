from tkinter import *
import TelaPrincipal
import TelaSecundaria

def fecharJanela():
    root3.destroy()
    import TelaPrincipal

root3 = Tk()
root3.title("")
# root.iconbitmap(default = "icon.png")
root3.geometry("265x100")
root3.resizable(width=FALSE, height=FALSE)

# Titulo
titulo = Label(root3, text='Cadastro Concluído com Sucesso!', font='Arial 10 bold')
titulo.place(x=20, y=10)

# Config btnIniciarSessao
btnEnviarDados = Button(root3, text='OK', command=fecharJanela)
btnEnviarDados.place(x=120, y=50)

root3.mainloop()