def escreva (mensagem):
    tamanho = len(mensagem) + 4
    print('~' * tamanho)
    print(f'  {mensagem}')
    print('~' * tamanho)


escreva('Arthur Alves')
escreva('Python')
escreva('Olá mundo!')