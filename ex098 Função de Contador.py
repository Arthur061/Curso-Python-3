from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo = abs(passo)
    if passo == 0:
        passo = 1

    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    sleep(2)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end=' ')
            sleep(0.5)
            cont += passo
        print('FIM')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end=' ')
            sleep(0.5)
            cont -= passo
        print('FIM')


contador(inicio=1, fim=10, passo=1)
contador(inicio=10, fim=0, passo=2)
print('-=' * 20)
print('Agora é sua vez de escolher uma contagem:')

i = int(input('Inicio: '))
f = int(input('Fim:    '))
p = int(input('Passos: '))
contador(i, f, p)
