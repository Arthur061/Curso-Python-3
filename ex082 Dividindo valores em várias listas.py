lista_numero = []
cont = 1
numeros_par = []
numeros_impar = []

while True:
    numero = int(input(f'Digite o {cont}° número: '))
    lista_numero.append(numero)
    cont += 1
    while True:
        continuar = str(input('Deseja continuar ? [S / N] ')).upper().strip()[0]
        if continuar == 'S':
            break
        elif continuar == 'N':
            break
    if cont == 1:
        if numero % 2 == 0:
            numeros_par.append(numero)
        if numero % 2 == 1:
            numeros_impar.append(numero)
    else:
        if numero % 2 == 0:
            numeros_par.append(numero)
        if numero % 2 == 1:
            numeros_impar.append(numero)

    if continuar == 'N':
        break
    else:
        print('')

print('-=' * 30)
print(f'Lista completa é {lista_numero}')
print('-=' * 30)
print(f'Os números ímpar são {numeros_impar}')
print('-=' * 30)
print(f'Os números par são {numeros_par}')
print('-=' * 30)
