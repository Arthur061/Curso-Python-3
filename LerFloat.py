'''def LerFloat(mensagem):
    while True:
        try:
            n = float(input(mensagem))
        except (TypeError, ValueError):
            print(f'\033[31mERROR! Por favor, digite um número real válido.')
        else:
            return n'''

        # OU

def LerFloat(mensagem):
    while True:
        try:
            n = float(input(mensagem))
        except (ValueError, TypeError):
            print(f'\033[31mERROR! Por favor, digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mERROR! O comando foi interropido pelo usuário.')
            return 0
        else:
            return n


