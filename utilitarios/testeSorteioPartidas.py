from random import shuffle

lista = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']

lista = lista[:6]

lista_partidas = list()
for i in range(0,len(lista)-1):
    for j in range(i,len(lista)):
        if(i != j):
            lista_partidas.append((lista[i],lista[j]))

lista_final_ida = list()
lista_final_volta = list()
for rodada in range(1,len(lista)):
    lista_rodada = list()
    for partida in range(1,int((len(lista)/2))+1):
        for index, item in enumerate(lista_partidas):
            if(item[0] not in lista_rodada and item[1] not in lista_rodada):
                print((rodada, partida) + item)
                lista_final_ida.append((rodada, partida) + item)
                lista_final_volta.append((rodada+(len(lista)-1), partida) + item)
                lista_rodada.append(item[0])
                lista_rodada.append(item[1])
                lista_partidas.pop(index)
                break



#shuffle(lista)
#lista_partidas = list()
#for time1, time2, partida in zip(range(0,15,2),range(1,16,2),range(1,9)):
#    lista_partidas.append((lista[time1],lista[time2],1,partida))

#for partida in lista_partidas:
#    print(f'{partida[0]} X {partida[1]} - Rodada {partida[2]} | Partida {partida[3]}')