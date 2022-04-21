dados_jogador = dict()

dados_jogador['Nome'] = str(input('Nome do jogador: '))
dados_jogador['Partidas'] = int(input(f'Quantas partidas {dados_jogador["Nome"]} jogou? '))
cont = 1
lista_gols = list()

for cont in range(1, dados_jogador['Partidas'] + 1):
    gols = int(input(f'Quantos gols na {cont}° partida:'))
    lista_gols.append(gols)
    cont += 1

dados_jogador['Gols'] = lista_gols
dados_jogador['Total'] = sum(lista_gols)
print('-=' * 30)
print(dados_jogador)
print('-=' * 30)

for keys, valor in dados_jogador.items():
    print(f'O campo {keys} tem o valor {valor}')

print('-=' * 30)
print(f'O jogador {dados_jogador["Nome"]} jogou {dados_jogador["Partidas"]} partidas')
for indice, valor in enumerate(lista_gols):
    print(f'    => Na partida {indice + 1}, fez {valor} gols')

print(f'O total de gols foi de {dados_jogador["Total"]}.')