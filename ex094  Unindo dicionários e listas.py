dados_gerais = dict()
lista_gerais = list()
cont = soma = media = 0
femininas_lista = list()

while True:
    dados_gerais.clear()
    dados_gerais['Nome'] = str(input('Nome: '))
    while True:
        dados_gerais['Sexo'] = str(input('Sexo [M / F]: ')).strip().upper()[0]
        if dados_gerais['Sexo'] == 'F':
            femininas_lista.append(dados_gerais['Nome'])
        if dados_gerais['Sexo'] == 'M' or dados_gerais['Sexo'] == 'F':
            break

    dados_gerais['Idade'] = int(input('Idade: '))
    soma += dados_gerais['Idade']
    lista_gerais.append(dados_gerais.copy())
    cont += 1

    while True:
        continuar = str(input('Quer continuar ? [S / N] ')).strip().upper()[0]
        if continuar == 'S' or continuar == 'N':
            break
    if continuar == 'N':
        break

media = soma / cont
print(f'A)  Ao todo temos {cont} pessoas cadastradas.')
print(f'B)  A média de idade é de {media:5.2f} anos.')
print(f'C)  As mulheres cadastradas foram {femininas_lista}')
print(f'D)  Pessoas com idade acima da média:')
for p in lista_gerais:
    if p['Idade'] >= media:
        print('     ', end='')
        for keys, valor in p.items():
            print(f'{keys} = {valor};', end='')
        print()
print('     <<<ENCERRADO>>>     ')