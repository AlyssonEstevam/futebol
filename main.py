import os
import sys
sys.path.append("D:\\python_projetos\\futebol")
import funcoes

opcao = funcoes.menu_principal()

while(opcao != '0'):
    os.system('cls')
    if(opcao.isnumeric()):
        if(opcao == '1'):
            funcoes.listar_ranking_times()
        elif(opcao == '2'):
            funcoes.iniciar_proxima_partida()
        elif(opcao == '3'):
            funcoes.iniciar_proxima_partida(flagRodada=True)
        elif(opcao == '4'):
            funcoes.exibir_partidas()
        elif(opcao == '5'):
            funcoes.exibir_tabela_pontos()
        elif(opcao == '6'):
            funcoes.exibir_tabelas_grupos()
        elif(opcao == '7'):
            funcoes.iniciar_proximo_campeonato()
        elif(opcao == '8'):
            funcoes.exibir_parametros()
        elif(opcao == '9'):
            funcoes.iniciar_partida_amistosa()
        elif(opcao == '10'):
            funcoes.cadastrar_novo_time()
        else:
            print('\033[1;31mDIGITE UMA OPÇÃO VÁLIDA!\033[m')
            print('\n\n\n')
            os.system('pause')
    else:
        print('\033[1;31mDIGITE UMA OPÇÃO VÁLIDA!\033[m')
        print('\n\n\n')
        os.system('pause')

    os.system('cls')

    opcao = funcoes.menu_principal()
