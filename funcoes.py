import os
import sys
sys.path.append("D:\\python_projetos\\futebol")

from random import randint, shuffle

import controllers.times_controller as times_controller
import controllers.parametros_controller as parametros_controller
import controllers.campeonatos_controller as campeonatos_controller
import controllers.partidas_controller as partidas_controller
import controllers.pontuacao_controller as pontuacao_controller
import controllers.pontuacao_grupos_controller as pontuacao_grupos_controller
from modelos.campeonato_modelo import Campeonato
from modelos.partida_modelo import Partida


def menu_principal():
    print('\033[1m###########\033[m \033[1;34mMENU PRINCIPAL\033[m \033[1m##########\033[m')
    print('\033[1m#                                   #\033[m')
    print('\033[1m#   1. RANKING DE TIMES             #\033[m')
    print('\033[1m#   2. PRÓXIMA PARTIDA              #\033[m')
    print('\033[1m#   3. PRÓXIMA RODADA               #\033[m')
    print('\033[1m#   4. EXIBIR PARTIDAS              #\033[m')
    print('\033[1m#   5. TABELA DE PONTOS             #\033[m')
    print('\033[1m#   6. TABELAS DOS GRUPOS           #\033[m')
    print('\033[1m#   7. INICIAR PRÓXIMO CAMPEONATO   #\033[m')
    print('\033[1m#   8. EXIBIR PARÂMETROS            #\033[m')
    print('\033[1m#   9. JOGO AMISTOSO                #\033[m')
    print('\033[1m#   10. CADASTRAR NOVO TIME         #\033[m')
    print('\033[1m#                                   #\033[m')
    print('\033[1m#   0. SAIR                         #\033[m')
    print('\033[1m#                                   #\033[m')
    print('\033[1m#####################################\033[m')

    return input('\n\n> ')


def cadastrar_novo_time():
    nomeTime = input('\033[1mDIGITE O NOME DO TIME: \033[m')
    times_controller.inserir(nomeTime)
    print('TIME CADASTRADO COM SUCESSO!')
    print('\n\n\n')
    os.system('pause')


def listar_ranking_times():
    lista_times = times_controller.seleciona_todos_ranking()

    print('\033[1m            \033[1;34mRANKING DE TIMES\033[m\n\033[m')
    print('\033[1m#--------------------------------------#\033[m')
    print('\033[1m| # |TIME          |T  |V  |E  |D  |G  |\033[m')
    print('\033[1m|---|--------------|---|---|---|---|---|\033[m')
    for index, time in enumerate(lista_times):
        print('\033[1m| {}{}{}{}{}{}{}{}{}{}{}{}{}{}|\033[m'.format(index+1,
                                                (' '*(2-len(str(index+1)))+'|'),
                                                time.get_nome(),
                                                (' '*(14-len(str(time.get_nome())))+'|'),
                                                time.get_quantidadeTitulo(),
                                                (' '*(3-len(str(time.get_quantidadeTitulo())))+'|'),
                                                time.get_quantidadeVitoria(),
                                                (' '*(3-len(str(time.get_quantidadeVitoria())))+'|'),
                                                time.get_quantidadeEmpate(),
                                                (' '*(3-len(str(time.get_quantidadeEmpate())))+'|'),
                                                time.get_quantidadeDerrota(),
                                                (' '*(3-len(str(time.get_quantidadeDerrota())))+'|'),
                                                time.get_quantidadeGols(),
                                                (' '*(3-len(str(time.get_quantidadeGols())))),
                                                ))
        if(index == len(lista_times)-1):
            print('\033[1m#--------------------------------------#\033[m')
        else:
            print('\033[1m|---|--------------|---|---|---|---|---|\033[m')

    print('\n\n\n')
    os.system('pause')


def exibir_parametros():
    parametro = parametros_controller.seleciona_parametros()

    print(f'\033[1;34mANO:\033[m \033[1m{parametro.get_ano()}\033[m')
    print(f'\033[1;34mTRIMESTRE:\033[m \033[1m{parametro.get_trimestre()}\033[m')
    if(parametro.get_codigoCampeonatoAtual() != None):
        campeonato_atual = campeonatos_controller.seleciona(parametro.get_codigoCampeonatoAtual())
        print(f'\033[1;34mCAMPEONATO:\033[m \033[1m{campeonato_atual.get_nome()}\033[m')
        print(f'\033[1;34mDIVISÃO:\033[m \033[1m{campeonato_atual.get_divisao()}\033[m')
        print(f'\033[1;34mRODADA:\033[m \033[1m{parametro.get_rodadaAtual()}\033[m')
        print(f'\033[1;34mPARTIDA:\033[m \033[1m{parametro.get_partidaAtual()}\033[m')
    
    print('\n\n\n')
    os.system('pause')


def iniciar_proximo_campeonato():
    parametro = parametros_controller.seleciona_parametros()

    ano_atual = parametro.get_ano()
    trimestre_atual = parametro.get_trimestre()
    divisao_atual = parametro.get_divisao()
    codigo_campeonato_atual = parametro.get_codigoCampeonatoAtual()
    verifica_campeonato = not partidas_controller.verifica_partida_ativa(codigo_campeonato_atual)

    if(verifica_campeonato):
        if(trimestre_atual == 1 or trimestre_atual == 3):
            campeonatos_controller.inserir(Campeonato(nome=f'CAMPEONATO PONTUAL - {divisao_atual}ª DIVISÃO - {trimestre_atual}º TRIMESTRE',
                                                      divisao=divisao_atual,ano=ano_atual,trimestre=trimestre_atual, formato='PONTO CORRIDO'))
            codigo_campeonato_atual = campeonatos_controller.seleciona_atual(ano_atual, trimestre_atual, divisao_atual)
            parametro.set_codigoCampeonatoAtual(codigo_campeonato_atual)
            parametro.set_rodadaAtual(1)
            parametro.set_partidaAtual(1)
            parametros_controller.atualiza_parametros(parametro)
            lista_times = times_controller.seleciona_codigos(divisao_atual)
            shuffle(lista_times)
            lista_partidas = sortear_partidas(lista_times, trimestre_atual)
            for partida in lista_partidas:
                partidas_controller.inserir(Partida(codigoCampeonato=codigo_campeonato_atual,
                                                    numeroRodada=partida[0],
                                                    numeroPartida=partida[1],
                                                    codigoTime1=partida[2],
                                                    codigoTime2=partida[3],))
            pontuacao_controller.limpa_tabela()
            for codigoTime in lista_times:
                pontuacao_controller.inserir_inicial(codigoTime)
        elif(trimestre_atual == 2):
            campeonatos_controller.inserir(Campeonato(nome=f'COPINHA MATA-MATA - {trimestre_atual}º TRIMESTRE',ano=ano_atual, 
                                                      divisao=1,trimestre=trimestre_atual, formato='MATA-MATA'))
            codigo_campeonato_atual = campeonatos_controller.seleciona_atual(ano_atual, trimestre_atual, 1)
            parametro.set_codigoCampeonatoAtual(codigo_campeonato_atual)
            parametro.set_rodadaAtual(1)
            parametro.set_partidaAtual(1)
            parametros_controller.atualiza_parametros(parametro)
            lista_times = times_controller.seleciona_codigos(1)
            lista_partidas = sortear_partidas(lista_times, trimestre_atual)
            for partida in lista_partidas:
                partidas_controller.inserir(Partida(codigoCampeonato=codigo_campeonato_atual,
                                                    numeroRodada=partida[0],
                                                    numeroPartida=partida[1],
                                                    codigoTime1=partida[2],
                                                    codigoTime2=partida[3]))
        elif(trimestre_atual == 4):
            campeonatos_controller.inserir(Campeonato(nome=f'COPA FINAL - {trimestre_atual}º TRIMESTRE',ano=ano_atual, 
                                                      divisao=1,trimestre=trimestre_atual, formato='MISTO'))
            codigo_campeonato_atual = campeonatos_controller.seleciona_atual(ano_atual, trimestre_atual, 1)
            parametro.set_codigoCampeonatoAtual(codigo_campeonato_atual)
            parametro.set_rodadaAtual(1)
            parametro.set_partidaAtual(1)
            parametros_controller.atualiza_parametros(parametro)
            lista_times = times_controller.seleciona_codigos(1)
            shuffle(lista_times)
            lista_partidas = sortear_partidas(lista_times, trimestre_atual)
            for partida in lista_partidas:
                partidas_controller.inserir(Partida(codigoCampeonato=codigo_campeonato_atual,
                                                    numeroRodada=partida[0],
                                                    numeroPartida=partida[1],
                                                    codigoTime1=partida[2],
                                                    codigoTime2=partida[3]))
            pontuacao_grupos_controller.limpa_tabela()
            for index, codigoTime in enumerate(lista_times):
                if(index >= 0 and index < 4):
                    grupo = 'A'
                elif(index >= 4 and index < 8):
                    grupo = 'B'
                elif(index >= 8 and index < 12):
                    grupo = 'C'
                elif(index >= 12 and index < 16):
                    grupo = 'D'
                pontuacao_grupos_controller.inserir_inicial(codigoTime, grupo)

        print('\033[1;32mNOVO CAMPEONATO INICIADO!\033[m')
    else:
        print('\033[1;31mEXISTE UM CAMPEONATO EM ANDAMENTO, FINALIZE AS PARTIDAS PRIMEIRO.\033[m')

    print('\n\n\n')
    os.system('pause')


def sortear_partidas(lista, trimestre_atual):
    if(trimestre_atual == 1 or trimestre_atual == 3):
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
                        lista_final_ida.append((rodada, partida) + item)
                        lista_final_volta.append((rodada+(len(lista)-1), partida) + item)
                        lista_rodada.append(item[0])
                        lista_rodada.append(item[1])
                        lista_partidas.pop(index)
                        break

        return lista_final_ida + lista_final_volta
    elif(trimestre_atual == 2):
        shuffle(lista)
        lista_partidas = list()
        for time1, time2, partida in zip(range(0,15,2),range(1,16,2),range(1,9)):
            lista_partidas.append((1,partida,lista[time1],lista[time2]))

        return lista_partidas
    elif(trimestre_atual == 4):
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

        return lista_final_ida + lista_final_volta


def iniciar_proxima_partida(flagRodada=False):
    parametro = parametros_controller.seleciona_parametros()

    if(parametro.get_trimestre() == 1 or parametro.get_trimestre() == 3):
        if(flagRodada):
            quantidadePartidas = 8
        else:
            quantidadePartidas = 1

        rodadaPassada = 0
        rodadaAtual = 0

        for i in range(0,quantidadePartidas):
            parametro = parametros_controller.seleciona_parametros()
            codigo_campeonato_atual = parametro.get_codigoCampeonatoAtual()
            if(partidas_controller.verifica_partida_ativa(codigo_campeonato_atual)):
                partida = partidas_controller.consulta_proxima_partida(codigo_campeonato_atual)

                rodadaAtual = partida.get_numeroRodada()

                if(i != 0 and rodadaAtual != rodadaPassada):
                    break

                pontuacao_time1 = pontuacao_controller.seleciona_pontuacao_time(partida.get_codigoTime1())
                pontuacao_time2 = pontuacao_controller.seleciona_pontuacao_time(partida.get_codigoTime2())

                time1 = times_controller.seleciona(partida.get_codigoTime1())
                time2 = times_controller.seleciona(partida.get_codigoTime2())

                gols_time1 = randint(0,5)
                gols_time2 = randint(0,5)

                pontuacao_time1.set_golsMarcados(pontuacao_time1.get_golsMarcados()+gols_time1)
                pontuacao_time2.set_golsMarcados(pontuacao_time2.get_golsMarcados()+gols_time2)
                pontuacao_time1.set_golsSofridos(pontuacao_time1.get_golsSofridos()+gols_time2)
                pontuacao_time2.set_golsSofridos(pontuacao_time2.get_golsSofridos()+gols_time1)
                pontuacao_time1.set_saldoGols(pontuacao_time1.get_golsMarcados()-pontuacao_time1.get_golsSofridos())
                pontuacao_time2.set_saldoGols(pontuacao_time2.get_golsMarcados()-pontuacao_time2.get_golsSofridos())
                pontuacao_time1.set_partidas(pontuacao_time1.get_partidas()+1)
                pontuacao_time2.set_partidas(pontuacao_time2.get_partidas()+1)

                time1.set_quantidadeGols(time1.get_quantidadeGols()+gols_time1)
                time2.set_quantidadeGols(time2.get_quantidadeGols()+gols_time2)

                partida.set_golsTime1(gols_time1)
                partida.set_golsTime2(gols_time2)
                partida.set_flagFinalizada(True)

                nomeTime1 = time1.get_nome()
                nomeTime2 = time2.get_nome()
                nomeCampeonato = campeonatos_controller.seleciona(parametro.get_codigoCampeonatoAtual()).get_nome()

                if(not flagRodada):
                    print(f'{nomeCampeonato.upper()}')
                print(f'\033[1;34mRODADA {partida.get_numeroRodada()} | PARTIDA {partida.get_numeroPartida()}\033[m\n')
                print(f'\033[1m{nomeTime1} {gols_time1} X {gols_time2} {nomeTime2}\033[m\n')

                if(gols_time1 == gols_time2):
                    pontuacao_time1.set_empates(pontuacao_time1.get_empates()+1)
                    pontuacao_time2.set_empates(pontuacao_time2.get_empates()+1)
                    pontuacao_time1.set_pontos(pontuacao_time1.get_pontos()+1)
                    pontuacao_time2.set_pontos(pontuacao_time2.get_pontos()+1)

                    time1.set_quantidadeEmpate(time1.get_quantidadeEmpate()+1)
                    time2.set_quantidadeEmpate(time2.get_quantidadeEmpate()+1)

                    partida.set_flagEmpate(True)
                    partida.set_codigoTimeVitoria(0)
                    partida.set_codigoTimeDerrota(0)
                elif(gols_time1 > gols_time2):
                    pontuacao_time1.set_vitorias(pontuacao_time1.get_vitorias()+1)
                    pontuacao_time2.set_derrotas(pontuacao_time2.get_derrotas()+1)
                    pontuacao_time1.set_pontos(pontuacao_time1.get_pontos()+3)

                    time1.set_quantidadeVitoria(time1.get_quantidadeVitoria()+1)
                    time2.set_quantidadeDerrota(time2.get_quantidadeDerrota()+1)

                    partida.set_codigoTimeVitoria(partida.get_codigoTime1())
                    partida.set_codigoTimeDerrota(partida.get_codigoTime2())
                else:
                    pontuacao_time2.set_vitorias(pontuacao_time2.get_vitorias()+1)
                    pontuacao_time1.set_derrotas(pontuacao_time1.get_derrotas()+1)
                    pontuacao_time2.set_pontos(pontuacao_time2.get_pontos()+3)

                    time2.set_quantidadeVitoria(time2.get_quantidadeVitoria()+1)
                    time1.set_quantidadeDerrota(time1.get_quantidadeDerrota()+1)

                    partida.set_codigoTimeVitoria(partida.get_codigoTime2())
                    partida.set_codigoTimeDerrota(partida.get_codigoTime1())

                pontuacao_controller.atualiza_pontuacoes(pontuacao_time1, pontuacao_time2)
                partidas_controller.atualiza_resultado_partida(partida)
                times_controller.atualizar_time(time1)
                times_controller.atualizar_time(time2)

                if(partidas_controller.verifica_partida_ativa(codigo_campeonato_atual)):
                    partida = partidas_controller.consulta_proxima_partida(codigo_campeonato_atual)
                    parametro.set_partidaAtual(partida.get_numeroPartida())
                    parametro.set_rodadaAtual(partida.get_numeroRodada())
                else:
                    codigo_time_vencedor = pontuacao_controller.seleciona_pontuacao_ordenada()[0][9]
                    campeonatos_controller.atualiza_campeao(codigo_campeonato_atual, codigo_time_vencedor)
                    
                    time_vencedor = times_controller.seleciona(codigo_time_vencedor)
                    time_vencedor.set_quantidadeTitulo(time_vencedor.get_quantidadeTitulo()+1)

                    times_controller.atualizar_time(time_vencedor)

                    ano_atual = parametro.get_ano()
                    trimestre_atual = parametro.get_trimestre()
                    divisao_atual = parametro.get_divisao()
                    
                    if(parametro.get_trimestre() == 1):
                        if(divisao_atual == 1):
                            parametro.set_divisao(2)
                            pontuacao_controller.atualiza_divisao_times(2)
                        else:
                            pontuacao_controller.atualiza_divisao_times(1)
                            parametro.set_divisao(1)
                            trimestre_atual += 1
                            parametro.set_trimestre(trimestre_atual)
                    elif(parametro.get_trimestre() == 3):
                        if(divisao_atual == 1):
                            parametro.set_divisao(2)
                            pontuacao_controller.atualiza_divisao_times(2)
                        else:
                            pontuacao_controller.atualiza_divisao_times(1)
                            parametro.set_divisao(1)
                            trimestre_atual += 1
                            parametro.set_trimestre(trimestre_atual)

                parametros_controller.atualiza_parametros(parametro)

            else:
                print('\n\033[1;31mNÃO EXISTEM PARTIDAS A SEREM JOGADAS, INICIE UM NOVO CAMPEONATO!\033[m')
                break
            
            rodadaPassada = rodadaAtual
    elif(parametro.get_trimestre() == 2):
        codigoTime1 = 0
        codigoTime2 = 0
        rodadaAtual = 0

        if(partidas_controller.consulta_partidas_restantes() > 1):
            quantidadePartidas = 2
        else:
            quantidadePartidas = 1

        for i in range(0,quantidadePartidas):
            parametro = parametros_controller.seleciona_parametros()
            codigo_campeonato_atual = parametro.get_codigoCampeonatoAtual()
            if(partidas_controller.verifica_partida_ativa(codigo_campeonato_atual)):
                partida = partidas_controller.consulta_proxima_partida(codigo_campeonato_atual)
                rodadaAtual = partida.get_numeroRodada()

                gols_time1 = randint(0,5)
                gols_time2 = randint(0,5)

                while(gols_time1 == gols_time2):
                    gols_time1 = randint(0,5)
                    gols_time2 = randint(0,5)

                partida.set_golsTime1(gols_time1)
                partida.set_golsTime2(gols_time2)
                partida.set_flagFinalizada(True)

                time1 = times_controller.seleciona(partida.get_codigoTime1())
                time2 = times_controller.seleciona(partida.get_codigoTime2())

                time1.set_quantidadeGols(time1.get_quantidadeGols()+gols_time1)
                time2.set_quantidadeGols(time2.get_quantidadeGols()+gols_time2)

                nomeTime1 = time1.get_nome()
                nomeTime2 = time2.get_nome()
                nomeCampeonato = campeonatos_controller.seleciona(parametro.get_codigoCampeonatoAtual()).get_nome()

                if(i == 0):
                    print(f'{nomeCampeonato.upper()}')

                #print('\033[1m{}\033[m'.format('-'*35))
                print(f'\033[1;34mRODADA {partida.get_numeroRodada()} | PARTIDA {partida.get_numeroPartida()}\033[m\n')
                print(f'\033[1m{nomeTime1} {gols_time1} X {gols_time2} {nomeTime2}\033[m\n')

                if(gols_time1 > gols_time2):
                    partida.set_codigoTimeVitoria(partida.get_codigoTime1())
                    partida.set_codigoTimeDerrota(partida.get_codigoTime2())

                    time1.set_quantidadeVitoria(time1.get_quantidadeVitoria()+1)
                    time2.set_quantidadeDerrota(time2.get_quantidadeDerrota()+1)

                    if(i == 0):
                        codigoTime1 = partida.get_codigoTime1()
                    else:
                        codigoTime2 = partida.get_codigoTime1()
                    if(quantidadePartidas == 1):
                        campeonatos_controller.atualiza_campeao(codigo_campeonato_atual, partida.get_codigoTime1())
                        time1.set_quantidadeTitulo(time1.get_quantidadeTitulo()+1)
                else:
                    partida.set_codigoTimeVitoria(partida.get_codigoTime2())
                    partida.set_codigoTimeDerrota(partida.get_codigoTime1())

                    time2.set_quantidadeVitoria(time2.get_quantidadeVitoria()+1)
                    time1.set_quantidadeDerrota(time1.get_quantidadeDerrota()+1)

                    if(i == 0):
                        codigoTime1 = partida.get_codigoTime2()
                    else:
                        codigoTime2 = partida.get_codigoTime2()
                    if(quantidadePartidas == 1):
                        campeonatos_controller.atualiza_campeao(codigo_campeonato_atual, partida.get_codigoTime2())
                        time2.set_quantidadeTitulo(time2.get_quantidadeTitulo()+1)

                partidas_controller.atualiza_resultado_partida(partida)
                times_controller.atualizar_time(time1)
                times_controller.atualizar_time(time2)

                if(quantidadePartidas == 2 and partidas_controller.verifica_partida_ativa(codigo_campeonato_atual)):
                    partida = partidas_controller.consulta_proxima_partida(codigo_campeonato_atual)
                    parametro.set_partidaAtual(partida.get_numeroPartida())
                    parametro.set_rodadaAtual(partida.get_numeroRodada())
                elif(quantidadePartidas == 2):
                    parametro.set_partidaAtual(1)
                    parametro.set_rodadaAtual(4)
                else:
                    ano_atual = parametro.get_ano()
                    trimestre_atual = parametro.get_trimestre()
                    trimestre_atual += 1
                    parametro.set_trimestre(trimestre_atual)

                parametros_controller.atualiza_parametros(parametro)
            else:
                print('\033[1;31mNÃO EXISTEM PARTIDAS A SEREM JOGADAS, INICIE UM NOVO CAMPEONATO!\033[m')
                break

        if(codigoTime1 != 0 and codigoTime2 != 0):
            rodadaAtual += 1
            ultima_partida = partidas_controller.consulta_ultima_partida()
            if(ultima_partida == 8 or ultima_partida == 4 or ultima_partida == 2 or ultima_partida == None):
                ultima_partida = 1
            else:
                ultima_partida += 1

            partidas_controller.inserir(Partida(codigoCampeonato=parametro.get_codigoCampeonatoAtual(),
                                                    numeroRodada=rodadaAtual,
                                                    numeroPartida=ultima_partida,
                                                    codigoTime1=codigoTime1,
                                                    codigoTime2=codigoTime2))
    elif(parametro.get_trimestre() == 4):
        parametro = parametros_controller.seleciona_parametros()

        if(parametro.get_rodadaAtual() <= 6):
            if(flagRodada):
                quantidadePartidas = 8
            else:
                quantidadePartidas = 1
            
            rodadaPassada = 0
            rodadaAtual = 0

            for i in range(0,quantidadePartidas):
                codigo_campeonato_atual = parametro.get_codigoCampeonatoAtual()
                if(partidas_controller.verifica_partida_ativa(codigo_campeonato_atual)):
                    partida = partidas_controller.consulta_proxima_partida(codigo_campeonato_atual)

                    rodadaAtual = partida.get_numeroRodada()

                    if(i != 0 and rodadaAtual != rodadaPassada):
                        break

                    pontuacao_time1 = pontuacao_grupos_controller.seleciona_pontuacao_time(partida.get_codigoTime1())
                    pontuacao_time2 = pontuacao_grupos_controller.seleciona_pontuacao_time(partida.get_codigoTime2())

                    time1 = times_controller.seleciona(partida.get_codigoTime1())
                    time2 = times_controller.seleciona(partida.get_codigoTime2())

                    gols_time1 = randint(0,5)
                    gols_time2 = randint(0,5)

                    pontuacao_time1.set_golsMarcados(pontuacao_time1.get_golsMarcados()+gols_time1)
                    pontuacao_time2.set_golsMarcados(pontuacao_time2.get_golsMarcados()+gols_time2)
                    pontuacao_time1.set_golsSofridos(pontuacao_time1.get_golsSofridos()+gols_time2)
                    pontuacao_time2.set_golsSofridos(pontuacao_time2.get_golsSofridos()+gols_time1)
                    pontuacao_time1.set_saldoGols(pontuacao_time1.get_golsMarcados()-pontuacao_time1.get_golsSofridos())
                    pontuacao_time2.set_saldoGols(pontuacao_time2.get_golsMarcados()-pontuacao_time2.get_golsSofridos())
                    pontuacao_time1.set_partidas(pontuacao_time1.get_partidas()+1)
                    pontuacao_time2.set_partidas(pontuacao_time2.get_partidas()+1)

                    time1.set_quantidadeGols(time1.get_quantidadeGols()+gols_time1)
                    time2.set_quantidadeGols(time2.get_quantidadeGols()+gols_time2)

                    partida.set_golsTime1(gols_time1)
                    partida.set_golsTime2(gols_time2)
                    partida.set_flagFinalizada(True)

                    nomeTime1 = time1.get_nome()
                    nomeTime2 = time2.get_nome()
                    nomeCampeonato = campeonatos_controller.seleciona(parametro.get_codigoCampeonatoAtual()).get_nome()

                    if(not flagRodada):
                        print(f'\033[1m{nomeCampeonato.upper()}\033[m')
                    print(f'\033[1;34mRODADA {partida.get_numeroRodada()} | PARTIDA {partida.get_numeroPartida()}\033[m\n')
                    print(f'\033[1m{nomeTime1} {gols_time1} X {gols_time2} {nomeTime2}\033[m\n')

                    if(gols_time1 == gols_time2):
                        pontuacao_time1.set_empates(pontuacao_time1.get_empates()+1)
                        pontuacao_time2.set_empates(pontuacao_time2.get_empates()+1)
                        pontuacao_time1.set_pontos(pontuacao_time1.get_pontos()+1)
                        pontuacao_time2.set_pontos(pontuacao_time2.get_pontos()+1)

                        time1.set_quantidadeEmpate(time1.get_quantidadeEmpate()+1)
                        time2.set_quantidadeEmpate(time2.get_quantidadeEmpate()+1)

                        partida.set_flagEmpate(True)
                        partida.set_codigoTimeVitoria(0)
                        partida.set_codigoTimeDerrota(0)
                    elif(gols_time1 > gols_time2):
                        pontuacao_time1.set_vitorias(pontuacao_time1.get_vitorias()+1)
                        pontuacao_time2.set_derrotas(pontuacao_time2.get_derrotas()+1)
                        pontuacao_time1.set_pontos(pontuacao_time1.get_pontos()+3)

                        time1.set_quantidadeVitoria(time1.get_quantidadeVitoria()+1)
                        time2.set_quantidadeDerrota(time2.get_quantidadeDerrota()+1)

                        partida.set_codigoTimeVitoria(partida.get_codigoTime1())
                        partida.set_codigoTimeDerrota(partida.get_codigoTime2())
                    else:
                        pontuacao_time2.set_vitorias(pontuacao_time2.get_vitorias()+1)
                        pontuacao_time1.set_derrotas(pontuacao_time1.get_derrotas()+1)
                        pontuacao_time2.set_pontos(pontuacao_time2.get_pontos()+3)

                        time2.set_quantidadeVitoria(time2.get_quantidadeVitoria()+1)
                        time1.set_quantidadeDerrota(time1.get_quantidadeDerrota()+1)

                        partida.set_codigoTimeVitoria(partida.get_codigoTime2())
                        partida.set_codigoTimeDerrota(partida.get_codigoTime1())

                    pontuacao_grupos_controller.atualiza_pontuacoes(pontuacao_time1, pontuacao_time2)
                    partidas_controller.atualiza_resultado_partida(partida)
                    times_controller.atualizar_time(time1)
                    times_controller.atualizar_time(time2)
                    
                    if(partidas_controller.verifica_partida_ativa(codigo_campeonato_atual)):
                        partida = partidas_controller.consulta_proxima_partida(codigo_campeonato_atual)
                        parametro.set_partidaAtual(partida.get_numeroPartida())
                        parametro.set_rodadaAtual(partida.get_numeroRodada())
                    elif(partida.get_numeroRodada() == 6):
                        grupo_A = pontuacao_grupos_controller.seleciona_pontuacao_ordenada_grupo('A')
                        grupo_B = pontuacao_grupos_controller.seleciona_pontuacao_ordenada_grupo('B')
                        grupo_C = pontuacao_grupos_controller.seleciona_pontuacao_ordenada_grupo('C')
                        grupo_D = pontuacao_grupos_controller.seleciona_pontuacao_ordenada_grupo('D')

                        partidas_controller.inserir(Partida(codigoCampeonato=parametro.get_codigoCampeonatoAtual(),
                                                            numeroRodada=7,
                                                            numeroPartida=1,
                                                            codigoTime1=grupo_A[0][9],
                                                            codigoTime2=grupo_A[1][9]))
                        partidas_controller.inserir(Partida(codigoCampeonato=parametro.get_codigoCampeonatoAtual(),
                                                            numeroRodada=7,
                                                            numeroPartida=2,
                                                            codigoTime1=grupo_B[0][9],
                                                            codigoTime2=grupo_B[1][9]))
                        partidas_controller.inserir(Partida(codigoCampeonato=parametro.get_codigoCampeonatoAtual(),
                                                            numeroRodada=7,
                                                            numeroPartida=3,
                                                            codigoTime1=grupo_C[0][9],
                                                            codigoTime2=grupo_C[1][9]))
                        partidas_controller.inserir(Partida(codigoCampeonato=parametro.get_codigoCampeonatoAtual(),
                                                            numeroRodada=7,
                                                            numeroPartida=4,
                                                            codigoTime1=grupo_D[0][9],
                                                            codigoTime2=grupo_D[1][9]))
                        parametro.set_partidaAtual(1)
                        parametro.set_rodadaAtual(7)

                    parametros_controller.atualiza_parametros(parametro)

                else:
                    print('\n\033[1;31mNÃO EXISTEM PARTIDAS A SEREM JOGADAS, INICIE UM NOVO CAMPEONATO!\033[m')
                    break
                
                rodadaPassada = rodadaAtual
        else:
            codigoTime1 = 0
            codigoTime2 = 0
            rodadaAtual = 0

            if(partidas_controller.consulta_partidas_restantes() > 1):
                quantidadePartidas = 2
            else:
                quantidadePartidas = 1

            for i in range(0,quantidadePartidas):
                parametro = parametros_controller.seleciona_parametros()
                codigo_campeonato_atual = parametro.get_codigoCampeonatoAtual()
                if(partidas_controller.verifica_partida_ativa(codigo_campeonato_atual)):
                    partida = partidas_controller.consulta_proxima_partida(codigo_campeonato_atual)
                    rodadaAtual = partida.get_numeroRodada()

                    gols_time1 = randint(0,5)
                    gols_time2 = randint(0,5)

                    while(gols_time1 == gols_time2):
                        gols_time1 = randint(0,5)
                        gols_time2 = randint(0,5)

                    partida.set_golsTime1(gols_time1)
                    partida.set_golsTime2(gols_time2)
                    partida.set_flagFinalizada(True)

                    time1 = times_controller.seleciona(partida.get_codigoTime1())
                    time2 = times_controller.seleciona(partida.get_codigoTime2())

                    time1.set_quantidadeGols(time1.get_quantidadeGols()+gols_time1)
                    time2.set_quantidadeGols(time2.get_quantidadeGols()+gols_time2)

                    nomeTime1 = time1.get_nome()
                    nomeTime2 = time2.get_nome()
                    nomeCampeonato = campeonatos_controller.seleciona(parametro.get_codigoCampeonatoAtual()).get_nome()

                    if(i == 0):
                        print(f'{nomeCampeonato.upper()}')

                    #print('\033[1m{}\033[m'.format('-'*35))
                    print(f'\033[1;34mRODADA {partida.get_numeroRodada()} | PARTIDA {partida.get_numeroPartida()}\033[m\n')
                    print(f'\033[1m{nomeTime1} {gols_time1} X {gols_time2} {nomeTime2}\033[m\n')

                    if(gols_time1 > gols_time2):
                        partida.set_codigoTimeVitoria(partida.get_codigoTime1())
                        partida.set_codigoTimeDerrota(partida.get_codigoTime2())

                        time1.set_quantidadeVitoria(time1.get_quantidadeVitoria()+1)
                        time2.set_quantidadeDerrota(time2.get_quantidadeDerrota()+1)

                        if(i == 0):
                            codigoTime1 = partida.get_codigoTime1()
                        else:
                            codigoTime2 = partida.get_codigoTime1()
                        if(quantidadePartidas == 1):
                            campeonatos_controller.atualiza_campeao(codigo_campeonato_atual, partida.get_codigoTime1())
                            time1.set_quantidadeTitulo(time1.get_quantidadeTitulo()+1)
                    else:
                        partida.set_codigoTimeVitoria(partida.get_codigoTime2())
                        partida.set_codigoTimeDerrota(partida.get_codigoTime1())

                        time2.set_quantidadeVitoria(time2.get_quantidadeVitoria()+1)
                        time1.set_quantidadeDerrota(time1.get_quantidadeDerrota()+1)

                        if(i == 0):
                            codigoTime1 = partida.get_codigoTime2()
                        else:
                            codigoTime2 = partida.get_codigoTime2()
                        if(quantidadePartidas == 1):
                            campeonatos_controller.atualiza_campeao(codigo_campeonato_atual, partida.get_codigoTime2())
                            time2.set_quantidadeTitulo(time2.get_quantidadeTitulo()+1)

                    partidas_controller.atualiza_resultado_partida(partida)
                    times_controller.atualizar_time(time1)
                    times_controller.atualizar_time(time2)

                    if(quantidadePartidas == 2 and partidas_controller.verifica_partida_ativa(codigo_campeonato_atual)):
                        partida = partidas_controller.consulta_proxima_partida(codigo_campeonato_atual)
                        parametro.set_partidaAtual(partida.get_numeroPartida())
                        parametro.set_rodadaAtual(partida.get_numeroRodada())
                    elif(quantidadePartidas == 2):
                        parametro.set_partidaAtual(1)
                        parametro.set_rodadaAtual(9)
                    else:
                        ano_atual = parametro.get_ano()
                        ano_atual += 1
                        parametro.set_ano(ano_atual)
                        parametro.set_trimestre(1)

                    parametros_controller.atualiza_parametros(parametro)
                else:
                    print('\033[1;31mNÃO EXISTEM PARTIDAS A SEREM JOGADAS, INICIE UM NOVO CAMPEONATO!\033[m')
                    break

            if(codigoTime1 != 0 and codigoTime2 != 0):
                rodadaAtual += 1
                ultima_partida = partidas_controller.consulta_ultima_partida()
                if(ultima_partida == 8 or ultima_partida == 4 or ultima_partida == 2 or ultima_partida == None):
                    ultima_partida = 1
                else:
                    ultima_partida += 1

                partidas_controller.inserir(Partida(codigoCampeonato=parametro.get_codigoCampeonatoAtual(),
                                                        numeroRodada=rodadaAtual,
                                                        numeroPartida=ultima_partida,
                                                        codigoTime1=codigoTime1,
                                                        codigoTime2=codigoTime2))
        
    print('\n')
    os.system('pause')


def exibir_tabela_pontos():
    lista_pontuacoes = pontuacao_controller.seleciona_pontuacao_ordenada()

    print('\033[1;34m           CLASSIFICAÇÃO CAMPEONATO PONTUAL\033[m\n')
    print('\033[1m#---------------------------------------------------#\033[m')
    print('\033[1m| # |TIME          |P  |J  |V  |E  |D  |SG  |GM |GS |\033[m')
    print('\033[1m|---|--------------|---|---|---|---|---|----|---|---|\033[m')
    for index, pontuacao in enumerate(lista_pontuacoes):
        print('\033[1m|{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}|\033[m'.format(' ',
                                                                index+1,
                                                                (' '*(2-len(str(index+1)))+'|'),
                                                                pontuacao[0],
                                                                (' '*(14-len(str(pontuacao[0])))+'|'),
                                                                pontuacao[1],
                                                                (' '*(3-len(str(pontuacao[1])))+'|'),
                                                                pontuacao[2],
                                                                (' '*(3-len(str(pontuacao[2])))+'|'),
                                                                pontuacao[3],
                                                                (' '*(3-len(str(pontuacao[3])))+'|'),
                                                                pontuacao[4],
                                                                (' '*(3-len(str(pontuacao[4])))+'|'),
                                                                pontuacao[5],
                                                                (' '*(3-len(str(pontuacao[5])))+'|'),
                                                                pontuacao[6],
                                                                (' '*(4-len(str(pontuacao[6])))+'|'),
                                                                pontuacao[7],
                                                                (' '*(3-len(str(pontuacao[7])))+'|'),
                                                                str(pontuacao[8]),
                                                                (' '*(3-len(str(pontuacao[8])))),
                                                                ))
        if(index == len(lista_pontuacoes)-1):
            print('\033[1m#---------------------------------------------------#\033[m')
        else:
            print('\033[1m|---|--------------|---|---|---|---|---|----|---|---|\033[m')

    print('\n\n\n')
    os.system('pause')


def exibir_tabelas_grupos():
    lista_pontuacoes = pontuacao_grupos_controller.seleciona_pontuacao_ordenada_grupo('A')

    print('\033[1m      CLASSIFICAÇÃO FASE DE GRUPOS - COPA FINAL\033[m\n')
    print('\033[1;31m#--------------------  GRUPO A  --------------------#\033[m')
    print('\033[1;31m| # |TIME          |P  |J  |V  |E  |D  |SG  |GM |GS |\033[m')
    print('\033[1;31m|---|--------------|---|---|---|---|---|----|---|---|\033[m')
    for index, pontuacao in enumerate(lista_pontuacoes):
        print('\033[1;31m|{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}|\033[m'.format(' ',
                                                                index+1,
                                                                (' '*(2-len(str(index+1)))+'|'),
                                                                pontuacao[0],
                                                                (' '*(14-len(str(pontuacao[0])))+'|'),
                                                                pontuacao[1],
                                                                (' '*(3-len(str(pontuacao[1])))+'|'),
                                                                pontuacao[2],
                                                                (' '*(3-len(str(pontuacao[2])))+'|'),
                                                                pontuacao[3],
                                                                (' '*(3-len(str(pontuacao[3])))+'|'),
                                                                pontuacao[4],
                                                                (' '*(3-len(str(pontuacao[4])))+'|'),
                                                                pontuacao[5],
                                                                (' '*(3-len(str(pontuacao[5])))+'|'),
                                                                pontuacao[6],
                                                                (' '*(4-len(str(pontuacao[6])))+'|'),
                                                                pontuacao[7],
                                                                (' '*(3-len(str(pontuacao[7])))+'|'),
                                                                str(pontuacao[8]),
                                                                (' '*(3-len(str(pontuacao[8])))),
                                                                ))
        if(index == len(lista_pontuacoes)-1):
            print('\033[1;31m#---------------------------------------------------#\033[m')
        else:
            print('\033[1;31m|---|--------------|---|---|---|---|---|----|---|---|\033[m')
    print('\n')
    lista_pontuacoes = pontuacao_grupos_controller.seleciona_pontuacao_ordenada_grupo('B')

    print('\033[1;32m#--------------------  GRUPO B  --------------------#\033[m')
    print('\033[1;32m| # |TIME          |P  |J  |V  |E  |D  |SG  |GM |GS |\033[m')
    print('\033[1;32m|---|--------------|---|---|---|---|---|----|---|---|\033[m')
    for index, pontuacao in enumerate(lista_pontuacoes):
        print('\033[1;32m|{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}|\033[m'.format(' ',
                                                                index+1,
                                                                (' '*(2-len(str(index+1)))+'|'),
                                                                pontuacao[0],
                                                                (' '*(14-len(str(pontuacao[0])))+'|'),
                                                                pontuacao[1],
                                                                (' '*(3-len(str(pontuacao[1])))+'|'),
                                                                pontuacao[2],
                                                                (' '*(3-len(str(pontuacao[2])))+'|'),
                                                                pontuacao[3],
                                                                (' '*(3-len(str(pontuacao[3])))+'|'),
                                                                pontuacao[4],
                                                                (' '*(3-len(str(pontuacao[4])))+'|'),
                                                                pontuacao[5],
                                                                (' '*(3-len(str(pontuacao[5])))+'|'),
                                                                pontuacao[6],
                                                                (' '*(4-len(str(pontuacao[6])))+'|'),
                                                                pontuacao[7],
                                                                (' '*(3-len(str(pontuacao[7])))+'|'),
                                                                str(pontuacao[8]),
                                                                (' '*(3-len(str(pontuacao[8])))),
                                                                ))
        if(index == len(lista_pontuacoes)-1):
            print('\033[1;32m#---------------------------------------------------#\033[m')
        else:
            print('\033[1;32m|---|--------------|---|---|---|---|---|----|---|---|\033[m')
    print('\n')
    lista_pontuacoes = pontuacao_grupos_controller.seleciona_pontuacao_ordenada_grupo('C')

    print('\033[1;33m#--------------------  GRUPO C  --------------------#\033[m')
    print('\033[1;33m| # |TIME          |P  |J  |V  |E  |D  |SG  |GM |GS |\033[m')
    print('\033[1;33m|---|--------------|---|---|---|---|---|----|---|---|\033[m')
    for index, pontuacao in enumerate(lista_pontuacoes):
        print('\033[1;33m|{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}|\033[m'.format(' ',
                                                                index+1,
                                                                (' '*(2-len(str(index+1)))+'|'),
                                                                pontuacao[0],
                                                                (' '*(14-len(str(pontuacao[0])))+'|'),
                                                                pontuacao[1],
                                                                (' '*(3-len(str(pontuacao[1])))+'|'),
                                                                pontuacao[2],
                                                                (' '*(3-len(str(pontuacao[2])))+'|'),
                                                                pontuacao[3],
                                                                (' '*(3-len(str(pontuacao[3])))+'|'),
                                                                pontuacao[4],
                                                                (' '*(3-len(str(pontuacao[4])))+'|'),
                                                                pontuacao[5],
                                                                (' '*(3-len(str(pontuacao[5])))+'|'),
                                                                pontuacao[6],
                                                                (' '*(4-len(str(pontuacao[6])))+'|'),
                                                                pontuacao[7],
                                                                (' '*(3-len(str(pontuacao[7])))+'|'),
                                                                str(pontuacao[8]),
                                                                (' '*(3-len(str(pontuacao[8])))),
                                                                ))
        if(index == len(lista_pontuacoes)-1):
            print('\033[1;33m#---------------------------------------------------#\033[m')
        else:
            print('\033[1;33m|---|--------------|---|---|---|---|---|----|---|---|\033[m')
    print('\n')
    lista_pontuacoes = pontuacao_grupos_controller.seleciona_pontuacao_ordenada_grupo('D')

    print('\033[1;34m#--------------------  GRUPO D  --------------------#\033[m')
    print('\033[1;34m| # |TIME          |P  |J  |V  |E  |D  |SG  |GM |GS |\033[m')
    print('\033[1;34m|---|--------------|---|---|---|---|---|----|---|---|\033[m')
    for index, pontuacao in enumerate(lista_pontuacoes):
        print('\033[1;34m|{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}|\033[m'.format(' ',
                                                                index+1,
                                                                (' '*(2-len(str(index+1)))+'|'),
                                                                pontuacao[0],
                                                                (' '*(14-len(str(pontuacao[0])))+'|'),
                                                                pontuacao[1],
                                                                (' '*(3-len(str(pontuacao[1])))+'|'),
                                                                pontuacao[2],
                                                                (' '*(3-len(str(pontuacao[2])))+'|'),
                                                                pontuacao[3],
                                                                (' '*(3-len(str(pontuacao[3])))+'|'),
                                                                pontuacao[4],
                                                                (' '*(3-len(str(pontuacao[4])))+'|'),
                                                                pontuacao[5],
                                                                (' '*(3-len(str(pontuacao[5])))+'|'),
                                                                pontuacao[6],
                                                                (' '*(4-len(str(pontuacao[6])))+'|'),
                                                                pontuacao[7],
                                                                (' '*(3-len(str(pontuacao[7])))+'|'),
                                                                str(pontuacao[8]),
                                                                (' '*(3-len(str(pontuacao[8])))),
                                                                ))
        if(index == len(lista_pontuacoes)-1):
            print('\033[1;34m#---------------------------------------------------#\033[m')
        else:
            print('\033[1;34m|---|--------------|---|---|---|---|---|----|---|---|\033[m')

    print('\n\n\n')
    os.system('pause')


def exibir_partidas():
    parametro = parametros_controller.seleciona_parametros()

    if(parametro.get_codigoCampeonatoAtual() == None):
        print('\033[1;31mNÃO EXISTEM PARTIDAS A SEREM LISTADAS, INICIE UM NOVO CAMPEONATO!\033[m')
    else:
        lista_partidas = partidas_controller.consulta_partidas_campeonato(parametro.get_codigoCampeonatoAtual())
        nomeCampeonato = campeonatos_controller.seleciona(parametro.get_codigoCampeonatoAtual()).get_nome()

        print('\033[1;34m'+nomeCampeonato+'\n\033[m')

        for index, partida in enumerate(lista_partidas):
            if(index == 0):
                print('\033[1;34m             {}ª RODADA\n\033[m'.format(partida[0]))
                rodada = partida[0]
            elif(rodada != partida[0]):
                print('\033[1;34m\n             {}ª RODADA\n\033[m'.format(partida[0]))
                rodada = partida[0]

            
            if(partida[5]): # Se a flagFinalizada for True
                print('\033[1m{}{} {} X {} {}\033[m'.format((' '*(14-len(str(partida[1])))),
                                        partida[1],
                                        partida[2],
                                        partida[4],
                                        partida[3]))
            else:
                print('\033[1m{}{}   X   {}\033[m'.format((' '*(14-len(str(partida[1])))),
                                        partida[1],
                                        partida[3]))
    print('\n\n\n')
    os.system('pause')


def iniciar_partida_amistosa():
    lista_times = times_controller.seleciona_todos()

    for time in lista_times:
        print(f'{time.get_codigo()}: {time.get_nome()}')

    print('\n')
    codigoTime1 = int(input('CÓDIGO DO TIME 1: '))
    codigoTime2 = int(input('CÓDIGO DO TIME 2: '))

    if(codigoTime1 != codigoTime2):
        partida = Partida()
        gols_time1 = randint(0,5)
        gols_time2 = randint(0,5)

        partida.set_codigoTime1(codigoTime1)
        partida.set_codigoTime2(codigoTime2)
        partida.set_golsTime1(gols_time1)
        partida.set_golsTime2(gols_time2)

        nomeTime1 = [time.get_nome() for time in lista_times if time.get_codigo() == codigoTime1][0]
        nomeTime2 = [time.get_nome() for time in lista_times if time.get_codigo() == codigoTime2][0]

        os.system('cls')
        print('PARTIDA AMISTOSA\n')
        print(f'{nomeTime1} {gols_time1} X {gols_time2} {nomeTime2}\n')

        if(gols_time1 == gols_time2):
            print('##### EMPATE ENTRE OS DOIS TIMES! #####')
        elif(gols_time1 > gols_time2):
            print(f'>>>>> {nomeTime1.upper()} É O VENCEDOR DO AMISTOSO! <<<<<')
        else:
            print(f'>>>>> {nomeTime2.upper()} É O VENCEDOR DO AMISTOSO! <<<<<')

        partidas_controller.atualiza_resultado_partida(partida, True)
    else:
        os.system('cls')
        print('\033[1;31mSELECIONE DOIS TIMES DIFERENTES PARA O CONFRONTO!\033[m')

    print('\n\n\n')
    os.system('pause')
