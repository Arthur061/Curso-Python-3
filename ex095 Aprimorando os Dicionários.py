time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partidas.clear()
    for c in range(1, total + 1):
        partidas.append(int(input(f'Quantos gols na partida {c}: ')))
    jogador['Gols'] = partidas [:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resposta = str(input('Quer continuar? [S/ N] ')).upper().strip()[0]
        if resposta == 'S' or resposta == 'N':
            break
    if resposta == 'N':
        break

print('-' * 40)
print('COD', end='')
for valor in jogador.keys():
    print(f'{valor:<15}', end='')
print()
for key, valor in enumerate(time):
    print(f'{key:>3} ', end='')
    for dado in valor.values():
        print(f'{str(dado):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERROR!! Não existe jogador com o código {busca}')
    else:
        print(f'  -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for indice, gols in enumerate(time[busca]["Gols"]):
            print(f'  No jogo {indice + 1} fez {gols} gols')
    print('-' * 40)
print('  ---VOLTE SEMPRE---  ')
