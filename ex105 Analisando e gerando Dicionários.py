def notas(* num, sit=False):
    '''
      -> analisar notas dos alunos:
    :param num: Uma ou mais notas dos alunos
    :param sit: (Opcional) Mostra a situação do aluno
    :return: Dcionario com informações do aluno
    '''
    dicionario = dict()
    dicionario['Total'] = len(num)
    dicionario['Maior'] = max(num)
    dicionario['Menor'] = min(num)
    dicionario['Média'] = sum(num)/len(num)

    if sit:
        if dicionario['Média'] >= 7:
            dicionario['Situação'] = 'BOA'
        elif dicionario['Média'] >= 5:
            dicionario['Situação'] = 'RAZOAVEL'
        else:
            dicionario['Situação'] = 'RUIM'

    return dicionario


resposta = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resposta)
