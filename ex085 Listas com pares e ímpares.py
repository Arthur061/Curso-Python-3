numeros = []
teste = 0
cont = 1
lista_par = []
lista_impar = []

for teste in range(1, 8):
    teste1 = int(input(f'Digite o {cont}° valor: '))
    cont += 1
    if teste1 % 2 == 0:
        lista_par.append(teste1)
    elif teste1 % 2 == 1:
        lista_impar.append(teste1)

lista_par.sort()
lista_impar.sort()
numeros.append(lista_impar[:])
lista_impar.clear()
numeros.append(lista_par[:])
lista_par.clear()

print(f'Os números par são {numeros[1]}')
print(f'Os números ímpar são {numeros[0]}')
