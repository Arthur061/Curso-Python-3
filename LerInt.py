'''def leiaInt(mensagem):
    while True:
        try:
            n = str(input(mensagem))
        except (ValueError, TypeError):
            print(f'\033[31mERROR! Por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return n'''

#  OU


def leiaInt(mensagem):
    while True:
        try:
            n = int(input(mensagem))
        except (ValueError, TypeError):
            print(f'\033[31mERROR! Por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mERROR! O comando foi interropido pelo usuário.')
            return 0
        else:
            return n
