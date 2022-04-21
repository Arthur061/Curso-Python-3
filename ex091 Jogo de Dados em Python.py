from random import randint
from time import sleep
from operator import itemgetter

numeros_dados = {'Jogador1': randint(1, 6), 'Jogador2': randint(1, 6),
                 'Jogador3': randint(1, 6), 'Jogador4': randint(1, 6)}  # keys e valores com números sorteados

print('Valores sorteados: ')  # Filurinha

rank = list()

for keys, valor in numeros_dados.items():  # Impreção dos ranks normais (sem modificação)
    print(f'{keys} tirou {valor} no dado')
    sleep(1)

rank = sorted(numeros_dados.items(), key=itemgetter(1), reverse=True)  # Comando importante, faz o rank ficar do maior para o menor

print('-=' * 30)
print('  == RANK DOS JOGADORES ==  ')  # Filurinha
for indice, valor in enumerate(rank):
    print(f'{indice + 1}° lugar: {valor[0]} com {valor[1]}')
    sleep(1)
