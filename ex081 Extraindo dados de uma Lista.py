cont = 0
lista_numero = []
continuar = ''

while True:
    lista_numero.append(int(input('Digite um número: ')))
    cont += 1
    while True:
        continuar = str(input('Quer continuar ? [S / N] ')).upper().strip()[0]

        if continuar == 'S':
            break
        elif continuar == 'N':
            break

    if continuar == 'N':
        break
    else:
        print('')

print('-=' * 30)
print(f'Você digitou {cont} números')

print('-=' * 30)
lista_numero.sort(reverse=True)
print(f'Os valores em ordem descrescente são {lista_numero}')

print('-=' * 30)
if 5 not in lista_numero :
    print('O número 5 não faz parte da lista!')
else:
    print('O número 5 faz parte da lista')
print('-=' * 30)
