print('-' * 40)
print('     LISTAGEM DE PREÇO     ')
print('-' * 40)

tupla_preços = ('Lápis', 1.75,
                'Borracha', 2.00,
                'Caderno', 27.00,
                'Caneta', 3.00,
                'Mochila', 120.32,
                'Estojo', 15.50)

for pos in range(0, len(tupla_preços)):
    if pos % 2 == 0:
        print(f'{tupla_preços[pos]:.<30}', end='R$ ')
    else:
        print(f'{tupla_preços[pos]:>7.2f}')
print('-' * 40)