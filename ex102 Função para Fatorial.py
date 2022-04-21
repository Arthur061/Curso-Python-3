def fatorial(num=1, show=False):
    '''
      -> Calcular faorial
    :param num: O número que vai ser calculado
    :param show: (Opcional) Mostra os passos do fatorial
    :return: Retorna o calculo do número
    Feito por Arthur :)
    '''
    f = 1
    for cont in range(num, 0, -1):
        if show:
            print(cont, end='')
            if cont > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= cont
    return f


numero = int(input('Digite um número: '))
print(fatorial(numero, True))
