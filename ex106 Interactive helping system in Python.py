def ajuda(mensagem):
    help(mensagem)


def titulo(mensagem, cor=0):
    tamanho = len(mensagem) + 4
    print('\033[0:43m~' * tamanho)
    print(f'  {mensagem} :)')
    print('~' * tamanho)


comando = ''
while True:
    from time import sleep
    titulo('SISTEMA DE AJUDINHAS')
    comando = str(input('\033[mFuncão ou blibioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        print('\033[0:46m-' * 30)
        print(f'     BUSCANDO POR {comando}'.upper())
        print('-' * 30)
        sleep(1.5)
        print('\033[7;30m')
        ajuda(comando)

print('Até logo :)')
