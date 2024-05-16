lista = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']

lista_partidas_A = list()
lista_partidas_B = list()
lista_partidas_C = list()
lista_partidas_D = list()

lista_A = lista[:4]
lista_B = lista[4:8]
lista_C = lista[8:12]
lista_D = lista[12:]

for i in range(0,len(lista_A)-1):
    for j in range(i,len(lista_A)):
        if(i != j):
            lista_partidas_A.append((lista_A[i],lista_A[j]))
            lista_partidas_B.append((lista_B[i],lista_B[j]))
            lista_partidas_C.append((lista_C[i],lista_C[j]))
            lista_partidas_D.append((lista_D[i],lista_D[j]))

lista_final_ida = list()
lista_final_volta = list()
for rodada in range(1,len(lista_A)):
    lista_rodada = list()
    for partida in range(1,int((len(lista_A)/2))+1):
        for index, (itemA, itemB, itemC, itemD) in enumerate(zip(lista_partidas_A,lista_partidas_B,lista_partidas_C,lista_partidas_D)):
            if(itemA[0] not in lista_rodada and itemA[1] not in lista_rodada):
                lista_final_ida.append((rodada, partida) + itemA)
                lista_final_ida.append((rodada, partida) + itemB)
                lista_final_ida.append((rodada, partida) + itemC)
                lista_final_ida.append((rodada, partida) + itemD)
                lista_final_volta.append((rodada+(len(lista_A)-1), partida) + itemA)
                lista_final_volta.append((rodada+(len(lista_A)-1), partida) + itemB)
                lista_final_volta.append((rodada+(len(lista_A)-1), partida) + itemC)
                lista_final_volta.append((rodada+(len(lista_A)-1), partida) + itemD)
                lista_rodada.append(itemA[0])
                lista_rodada.append(itemA[1])
                lista_partidas_A.pop(index)
                lista_partidas_B.pop(index)
                lista_partidas_C.pop(index)
                lista_partidas_D.pop(index)
                break

lista_final = lista_final_ida + lista_final_volta

for partida in lista_final:
    print(partida)
