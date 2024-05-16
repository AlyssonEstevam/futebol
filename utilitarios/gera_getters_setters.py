lista = ['codigo',
'codigoTime',
'pontos',
'partidas',
'vitorias',
'empates',
'derrotas',
'golsMarcados',
'golsSofridos',
'saldoGols']


for item in lista:
    print(f'def get_{item}(self):\n'
          f'\treturn self._{item}\n\n'
          f'def set_{item}(self, valor):\n'
          f'\tself._{item} = valor\n')

