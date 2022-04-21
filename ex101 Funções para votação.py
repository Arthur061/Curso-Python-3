def votar(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade < 16:
        return f'Com {idade} anos: O eleitor não vota!'
    elif idade == 16 or idade == 17 or idade >= 65:
        return f'Com {idade} anos: O voto é opcional'
    elif idade < 65:
        return f'com {idade} anos: O voto é obrigatório'


ano_nascimento = int(input('Digite o ano de seu nascimento: '))
votar(ano_nascimento)
