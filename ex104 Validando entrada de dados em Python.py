def leiaInt(mensagem):
    ok = False
    valor = 0
    while True:
        n = str(input(mensagem))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERROR!! Digite um número inteiro valido.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'\033[32mO número digitado foi {n}')
