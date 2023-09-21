import math


def encontra_menor_nota(disciplinas):
    nota_menor = math.inf
    nome_menor = ""
    for nome, (nota, _) in disciplinas.items():
        if nota < nota_menor:
            nota_menor = nota
            nome_menor = nome

    return nome_menor, nota_menor


def encontra_maior_nota(disciplinas):
    nota_maior = -math.inf
    nome_maior = ""
    for nome, (nota, _) in disciplinas.items():
        if nota > nota_maior:
            nota_maior = nota
            nome_maior = nome

    return nome_maior, nota_maior


def calcula_media_ponderada(disciplinas):
    soma = 0
    soma_pesos = 0
    for _, (nota, peso) in disciplinas.items():
        soma += nota * peso
        soma_pesos += peso

    media = soma / soma_pesos
    return media
