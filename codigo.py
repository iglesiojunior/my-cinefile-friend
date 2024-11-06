import requests
from tkinter import *

api_key = "02023ee90b0830edef76e7db8bd93af5"

def search_button(botoes, selecao, janela, botao_pesquisa, botao_resultado_films):
    # Obtenha os IDs dos gêneros selecionados
    selecao.clear()
    selecao.extend(botoes_selecionados(botoes))  # Atualiza `selecao` com os IDs dos botões selecionados
    
    reorganizar_janela(janela, botoes)
    botao_pesquisa.grid_forget()
    botao_resultado_films.grid(column=1, row=1, sticky="nsew")
    botao_resultado_films.config(command=lambda: search_films(selecao, janela))

def reorganizar_janela(janela, botoes):
    for id, botao in botoes.items():
        botao.grid_forget()
    botoes.clear()

def search_films(selecao, janela):
    url = "https://api.themoviedb.org/3/discover/movie?&language=pt-BR&sort_by=popularity.desc"
    params = {
        "api_key": api_key,
        "with_genres": ",".join(map(str, selecao)),
        "vote_count.gte": 500,
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        films = data.get("results", [])
        print("Deu certo demais paezao")
        print(films)
        
        # Limpar resultados anteriores
        for widget in janela.winfo_children():
            if isinstance(widget, Label) and widget.grid_info().get("row") > 1:
                widget.destroy()
        
        for i in range(len(films)):
            texto_filme = Label(janela, text=films[i]["title"])
            texto_filme.grid(column=0, row=i + 2, sticky="nsew")
    
        return films
    else:
        print("Erro ao buscar filmes:", response.status_code)
        return None
    
def botoes_selecionados(botoes):
    # Retorna uma lista de IDs dos botões selecionados
    selecionados = [id for id, botao in botoes.items() if botao.cget('relief') == 'sunken']
    # log do sistema
    for id in selecionados:
        print(id)
    return selecionados  # Retorna a lista dos IDs selecionados

def alternar_selecao(botao):
    if botao.cget('relief') == 'raised':
        botao.config(bg="lightblue", relief="sunken")  # Muda a cor e o relevo para indicar seleção
    else:
        botao.config(bg="SystemButtonFace", relief="raised")  # Retorna à cor padrão e relevo normal

def get_genres(api_key):
    url = "https://api.themoviedb.org/3/genre/movie/list?language=pt-BR"
    params = {"api_key": api_key}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        genres = data.get("genres", [])
        print("Deu certo demais paezao")
        return genres
    else:
        print("Erro ao buscar os gêneros:", response.status_code)
        return None

def get_text(barra_pesquisa):
    texto = barra_pesquisa.get()

def main():
    global selecionado
    
    janela = Tk()
    janela.geometry("300x550")
    janela.title("Seu melhor amigo cinéfilo")
    
    # Chave da API do The Movie Database
    genres = get_genres(api_key)
    
    selecionado = False
    
    botoes = {}
    
    i = 2
    for genre in genres:
        # Criação de cada botão para gênero
        botao = Button(janela, text=genre["name"], relief="raised")
        botao.config(command=lambda b=botao: alternar_selecao(b))
        botao.grid(column=0, row=i, sticky="nsew")
        botoes[genre["id"]] = botao
        i += 1
    
    texto_inicial = Label(janela, text="Olá, eu sou seu melhor amigo cinéfilo!")
    texto_inicial.grid(column=0, row=0, sticky="nsew")
    
    texto_guia = Label(janela, text="Escolha um gênero para começar a navegar:")
    texto_guia.grid(column=0, row=1, sticky="nsew")
    
    selecao = []
    
    botao_resultado_films = Button(janela, text="Resultados")
    
    botao_pesquisa = Button(janela, text="Pesquisar")
    botao_pesquisa.grid(column=1, row=1, sticky="nsew")
    botao_pesquisa.config(command=lambda: search_button(botoes, selecao, janela, botao_pesquisa, botao_resultado_films))
    
    janela.mainloop()
    
main()
