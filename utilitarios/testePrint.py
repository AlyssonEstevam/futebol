listaTimes = [('Fire Ball', '9', '3'),('CSA','12','4'),('Phoenix Sports','6','2')]


print('NOME            PONTOS   VITÓRIAS')
for time in listaTimes:
    print('{}{}{}{}{}'.format(time[0],' '*(16-len(time[0])),time[1],' '*(9-len(time[1])),time[2]))
