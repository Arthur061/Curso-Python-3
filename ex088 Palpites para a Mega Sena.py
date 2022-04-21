from time import sleep
from random import randint

print('-=' * 20)
print('          JOGO DA MEGA CENA          ')
print('-=' * 20)

jogos_lista = []
cont = 0
lista_sorteio = []
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1

print('-=' * 5, f' SORTEANDO {jogos} JOGOS', '-=' * 5)
while total <= jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista_sorteio:
            lista_sorteio.append(num)
            cont += 1
        if cont >= 6:
            break

    lista_sorteio.sort()
    jogos_lista.append(lista_sorteio[:])
    lista_sorteio.clear()
    total += 1
for indice, lista in enumerate(jogos_lista):
    indice += 1
    print(f'Jogo {indice}: {lista}')
    sleep(1)

print('-=' * 5, ' <<  BOA SORTE!  >> ', '-=' * 5)
