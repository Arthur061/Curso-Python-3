tulpla_palavras = ('arthur', 'alves', 'ribeiro', 'cursando',
                   'progamaçao', 'python')

for p in tulpla_palavras:  # Analisar cada elemento dentro da tupla
    print(f'\nNa palavra {p.upper()} temos ', end='')  # Imprimir frase já com o elemento
    for letra in p:
        if letra.lower() in 'aeiou':  # Se tiver 'aeiou' na palavra imprimir a vogal
            print(letra, end=' ')
