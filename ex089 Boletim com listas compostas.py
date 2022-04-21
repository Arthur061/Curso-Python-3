ficha_alunos = []
continuar = ''
cont = 0

while True:
    nome = str(input('Nome: '))
    nota1 = (float(input('1° nota: ')))
    nota2 = (float(input('2° nota: ')))
    media = (nota1 + nota2) / 2
    ficha_alunos.append([nome, [nota1, nota2], media])

    cont += 1
    while True:
        continuar = str(input('Quer continuar: [S / N] ')).upper().strip()[0]
        if continuar == 'N':
            break
        if continuar == 'S':
            break
    if continuar == 'N':
        break

print('-=' * 30)
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 25)
for indice, aluno in enumerate(ficha_alunos):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    print('-' * 30)
    duvida = int(input('Mostrar notas de qual aluno ? (999 interrompe) '))
    if duvida == 999:
        print('FINALIZANDO...')
        break
    if duvida <= len(ficha_alunos) - 1:
        print(f'Notas de {ficha_alunos[duvida][0]} são {ficha_alunos[duvida][1]}')
print('_-_-_- Volte Sempre!! _-_-_-_')