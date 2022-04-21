times = ('Palmeiras',   'Santos',  'Vasco',   'Grêmio',  'Flamengo',
      'Corinthians',   'Internacional',   'Cruzeiro',    'São Paulo',   'Atlético Mineiro',
      'Botafogo',    'Fluminense',   'Coritiba',    'Bahia',   'Goiás',
      'Guarani',   'Sport',   'Portuguesa',   'Atlético Paranaense',   'Vitória')

print('-=' * 40)
print(f'Lista de times 2022: {times}')

print('-=' * 40)
print(f'Os 5 primeiros times são: {times[:5]}')

print('-=' * 40)
print(f'Os últimos 4 colocados são: {times[-4:]}')

print('-=' * 40)
print(f'Times em ordem alfabética: {sorted(times[0:])}')

print('-=' * 40)
print(f'Flamengo está na {times.index("Flamengo")+ 1}° posição')