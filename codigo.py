from tkinter import *


def get_text(barra_pesquisa):
    texto = barra_pesquisa.get()
    print(texto)

def main():
    janela = Tk()
    janela.geometry("350x300")
    janela.title("Seu melhor amigo cinéfilo")
    
    texto_inicial = Label(janela, text="Olá, eu sou seu melhor amigo cinéfilo!")
    texto_inicial.grid(column=0, row=0, sticky="nsew")
    
    barra_pesquisa = Entry(janela, width=50)
    barra_pesquisa.grid(column=0, row=1, sticky="nsew")
    
    botão_barra_pesquisa = Button(janela, text="Buscar", command=lambda: get_text(barra_pesquisa))
    botão_barra_pesquisa.grid(column=1, row=1, sticky="nsew")
    
    
    
    janela.mainloop()
    
main()