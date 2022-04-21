matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):  # Contagem linhas
    for coluna in range(0, 3):  # Contagem colunas
        matriz[linha][coluna] = int(input(f'Digite um valor [{linha}, {coluna}]: '))  # Números de entrada

print('-=' * 30)
for linha in range(0, 3):  # Contagem linhas
    for coluna in range(0, 3):  # Contagem colunas
        print(f'[{matriz[linha][coluna]:^5}]', end='')  # Ajeitando colunas e linhas
    print()
