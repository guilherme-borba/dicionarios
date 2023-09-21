import entities

quantidade_disciplinas = int(input('Quantidade disciplinas: '))

disciplinas = {}

while quantidade_disciplinas > 0:
    try:
        linha = input().split()

        nome = linha[0]
        nota = float(linha[1])
        peso = int(linha[2])
        disciplinas[nome] = (nota, peso)

        quantidade_disciplinas -= 1
    except ValueError:
        print("Entrada inválida. Certifique-se de fornecer um nome, uma nota e um peso válidos.")

(nome_menor, nota_menor) = entities.encontra_menor_nota(disciplinas)
(nome_maior, nota_maior) = entities.encontra_maior_nota(disciplinas)
media = entities.calcula_media_ponderada(disciplinas)

print("Menor: %s %.1f" % (nome_menor, nota_menor))
print("Maior: %s %.1f" % (nome_maior, nota_maior))
print("Média: %.2f" % media)
