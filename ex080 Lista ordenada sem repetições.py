lista_num = []
for cont in range(0, 5):
    numero = int(input('Digite um valor: '))
    if numero == 0 or numero > lista_num[-1]:
        lista_num.append()
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(lista_num):
            if numero <= lista_num[pos]:
                lista_num.insert(pos, numero)
                print(f'Adicionado na posição {pos}...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista_num }')