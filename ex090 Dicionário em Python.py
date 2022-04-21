dicionario = dict()

dicionario['Nome'] = str(input('Nome: '))  # Entranda valor nome
dicionario['Média'] = float(input(f'Média de {dicionario["Nome"]}: '))  # Entranda valor média

# Situação aluno
if dicionario['Média'] <= 5:
    dicionario['Situação'] = 'Reprovado'
elif dicionario['Média'] < 7:
    dicionario['Situação'] = 'Recuperação'
elif dicionario['Média'] >= 7:
    dicionario['Situação'] = 'Aprovado'

print('-=' * 30)

# Resolução 1
'''print(f'- Nome é igual a {dicionario["Nome"]}')  # Resolução 1
print(f'- Média é igual a {dicionario["Média"]}')
print(f'- Situação é igual a {dicionario["Situação"]}')'''

# Resolução 2
for keys, valor in dicionario.items():
    print(f'  - {keys} é igual a {valor}')
