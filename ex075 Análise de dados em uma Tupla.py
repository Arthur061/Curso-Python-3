números1 = int(input('Digite o 1° número: ', ))
números2 = int(input('Digite o 2° número: '))
números3 = int(input('Digite o 3° número: '))
números4 = int(input('Digite o 4° número: '))

tupla = números1, números2, números3, números4

print(f'Você digitou os números: {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na posição {tupla.index(3)+ 1}')
else:
    print('O valor 3 não apareceu em  nenhuma posição.')
print('Os valores PAR digitados foram: ', end='')
for n in tupla:
    if n % 2 ==0:
        print(n, end='')
