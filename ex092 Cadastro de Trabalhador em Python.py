from datetime import date

atual = date.today().year  # Calcular ano atual
dados = dict()

while True:  # CRiando entrada para sem carteira de trabalho
    dados['Nome'] = str(input('Nome: '))
    dados['Idade'] = int(input('Ano de nascimento: '))
    dados['CTPS'] = int(input('Carteira de trabalho: (0 se não tem) '))

    if dados['CTPS'] == 0:
        break

    if dados['CTPS'] != 0:  # Restante entrada se tiver carteira de trabalho
        dados['Contratação'] = int(input('Ano de contratação: '))
        dados['Salário'] = float(input('Salario R$'))
        dados['Idade'] = atual - dados['Idade']
        dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - atual)
        break

print('-=' * 30)
for keys, valor in dados.items():
    print(f'{keys} tem o valor de {valor}')
