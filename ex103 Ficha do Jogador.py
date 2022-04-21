def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


jogador = str(input('Nome do jogador: '))
g = str(input('Quantidade de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if jogador == '':
    ficha(gols=g)
else:
    ficha(jogador, g)
