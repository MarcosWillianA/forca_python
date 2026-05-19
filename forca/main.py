import random
from palavras import lista_de_palavras

def escolher_tema_e_palavra(palavras):
    chave_aleatoria = random.choice(list(palavras.keys()))
    lista_selecionada = palavras[chave_aleatoria]
    palavra_escolhida = random.choice(lista_selecionada)
    return (chave_aleatoria, palavra_escolhida)


print(escolher_tema_e_palavra(lista_de_palavras))