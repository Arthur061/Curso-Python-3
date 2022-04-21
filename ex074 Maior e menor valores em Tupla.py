from random import randint

# Sorteando os cinco valores
aleatorio = (randint(0, 10), randint(0, 10), randint(0, 10),
             randint(0, 10), randint(0, 10))

# Respostas:
print(f'Os valores sorteados foram: {aleatorio}')
print(f'Maior número é: {max(aleatorio)}')
print(f'Menor número é: {min(aleatorio)}')
