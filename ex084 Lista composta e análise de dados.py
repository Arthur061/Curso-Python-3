lista = []
dados = []
cont = maior = menor = 0
continuar = ''

while True:
    dados.append(str(input('Nome: ')))  # Adicionando Nome
    dados.append(float(input('Peso: Kg ')))  # Adicionando Peso

    if len(lista) == 0:  # Maior peso e menor peso
        maior = menor = dados[1]
    else:  # Maior peso e menor peso
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    lista.append(dados[:])  # Clonando lista provisoria (dados)
    dados.clear()  # Limpando lista provisoria para não dar merda

    while True:
        continuar = str(input('Quer continuar ? [S / N] ')).upper().strip()[0]  # Caso o usuario não pague de doido
        if continuar == 'N':
            break
        elif continuar == 'S':
            break
    if continuar == 'N':
        break

print('-=' * 30)
print(f'O total de pessoas cadastradas foi de {len(lista)} pessoas.')
print('-=' * 30)
print(f'O maior peso foi de {maior}Kg e foi de ', end='')

for p in lista:  # Mostrando de quem é os maiores kilos
    if p[1] == maior:
        print(f'{[p[0]]} ', end='')

print()
print('-=' * 30)
print(f'O menor peso foi de {menor}Kg e foi de ', end='')

for p in lista:  # Mostrando de quem é os menores kilos
    if p[1] == menor:
        print(f'{[p[0]]} ', end='')

print()
print('-=' * 30)

