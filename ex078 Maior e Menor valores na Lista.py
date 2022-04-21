cont = 0
lista_numeros = []

for cont in range(0, 5):
    lista_numeros.append(int(input(f'Digite um valor para a posição {cont}: ')))
    cont += 1

print('-=' * 30)
print(f'Você digitou os seguintes valores: {lista_numeros}')

print(f'Maior número é {max(lista_numeros)} e está na posição {lista_numeros.index(max(lista_numeros))}')

print(f'Menor número é {min(lista_numeros)} e está na posição {lista_numeros.index(min(lista_numeros))}')