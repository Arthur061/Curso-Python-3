from time import sleep


def maior(* numeros):

    tamanho = len(numeros)
    maior = contador = 0
    print('Analisando os valores...')

    for valor in numeros:
        print(f'{valor} ', end='')
        sleep(0.3)

        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1

    print(f'\nFoi um total de {tamanho} números e o maior número foi {maior}')
    print('-=' * 30)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
