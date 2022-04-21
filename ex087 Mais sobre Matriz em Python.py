matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = []  # Lista para guardar valores par
soma_coluna = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor [{linha}, {coluna}]: '))

        if matriz[linha][coluna] % 2 == 0:
            soma_par.append(matriz[linha][coluna])

print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('-=' * 30)

# Novos comandos
print(f'A soma de todos os números par é {sum(soma_par)}')  # Soma dos números par da matriz

for linha in range(0, 3):  # Soma dos valores da linha/coluna
    soma_coluna += matriz[linha][2]
print(f'A soma dos valores da 3° coluna é {soma_coluna}')

print(f'O maior valor da 2° linha é {max(matriz[1])}')  # Maior valor da segunda linha
