expressão = str(input('Digite a expressão: '))
lista = []
for simbolo in expressão:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está incorreta!')
