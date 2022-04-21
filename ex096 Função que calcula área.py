def area(l, c):
    print('-=' * 30)
    multiplica = l * c
    print(f'A área de um terreno de {l} x {c} é de {multiplica}m².')


print('     Calculando área     ')
print('-' * 30)
largura = float(input('LARGURA: (m) '))
comprimento = float(input('COMPRIMENTO: (m) '))
area(l=largura, c=comprimento)
