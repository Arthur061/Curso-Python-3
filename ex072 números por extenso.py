
# Números por extenso
extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

# Comando a realizar se o usuario colocar um número incorreto
while True:
    numero = int(input('Digite um número de 0 até 20: '))  # Entrada número
    while True:
        if numero < 0 or numero > 20:
            numero = int(input('Tente novamente. Digite um número de 0 até 20: '))  # Entrada número 'secundario'
        else:
            break

    print(f'Você digitou o número {extenso[numero]}')  # Imprime o resultado

    pergunta = str(input('Você quer continuar ? [S / N] ')).upper().strip()[0]  # Pergunta se quer ou não continuar

    if pergunta == 'N':
        break
    elif pergunta == 'S':
        print('Ok, vamos continuar!')

print('Acabou')