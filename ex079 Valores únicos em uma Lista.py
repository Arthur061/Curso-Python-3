lista_valores = []
continuar = 'SN'

while True:
    lista_valores1 = int(input('Digite um valor: '))  # Entrada do valor

    if lista_valores1 not in lista_valores: # Valor não duplicado
        print('Valor adicionado com sucesso!')
        lista_valores.append(lista_valores1)

    else:
        print('Error, número duplicado não será adicionado.')  # Valor duplicado

    continuar = str(input('Quer continuar ? [S /N] ')).upper().strip()[0]  # Continuar sim ou não

    if continuar == 'S':
        print('-' * 30)

    else:
        break

print('-' * 30)
lista_valores.sort()
print(f'Você digitou os valores {lista_valores}')  # Lista imprimida em ordem crescente
