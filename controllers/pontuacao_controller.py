import sys
sys.path.append("D:\\python_projetos\\futebol")
from database.conex import executa_query, consulta_query
from modelos.pontuacao_modelo import Pontuacao
import controllers.times_controller as times_controller


def limpa_tabela():
    comando = f"truncate table pontuacao"
    executa_query(comando)


def inserir_inicial(codigoTime):
    comando = f"insert into pontuacao (codigoTime) values ('{codigoTime}')"
    executa_query(comando)


def seleciona_pontuacao_time(codigoTime):
    comando = f"select * from pontuacao where codigoTime = '{codigoTime}'"
    time_query = consulta_query(comando)

    time_pontuacao = Pontuacao()
    for time in time_query:
        time_pontuacao.set_codigo(time[0])
        time_pontuacao.set_codigoTime(time[1])
        time_pontuacao.set_pontos(time[2])
        time_pontuacao.set_partidas(time[3])
        time_pontuacao.set_vitorias(time[4])
        time_pontuacao.set_empates(time[5])
        time_pontuacao.set_derrotas(time[6])
        time_pontuacao.set_golsMarcados(time[7])
        time_pontuacao.set_golsSofridos(time[8])
        time_pontuacao.set_saldoGols(time[9])

    return time_pontuacao


def seleciona_pontuacao_ordenada():
    comando = (f"select t.nome, p.pontos, p.partidas, p.vitorias, p.empates, p.derrotas, p.saldoGols, p.golsMarcados, p.golsSofridos, t.codigo "
               f"from pontuacao p inner join times t on t.codigo = p.codigoTime "
               f"order by pontos desc, vitorias desc, empates desc, derrotas, saldoGols desc, golsMarcados desc, golsSofridos")       
    pontuacao_query = consulta_query(comando)

    return pontuacao_query


def atualiza_divisao_times(divisao):
    if(divisao == 1):
        comando = (f"select codigoTime "
                   f"from pontuacao "
                   f"order by pontos desc, vitorias desc, empates desc, derrotas, saldoGols desc, golsMarcados desc, golsSofridos")       
        pontuacao_query = consulta_query(comando)
        lista_times_promovidos = pontuacao_query[:4]
        for time in lista_times_promovidos:
            times_controller.atualizar_divisao(time[0], 1)

        lista_times_rebaixados = times_controller.rebaixar_times()
    elif(divisao == 2):
        comando = (f"select codigoTime "
                   f"from pontuacao "
                   f"order by pontos desc, vitorias desc, empates desc, derrotas, saldoGols desc, golsMarcados desc, golsSofridos")       
        pontuacao_query = consulta_query(comando)
        lista_times_rebaixados = pontuacao_query[12:]
        for time in lista_times_rebaixados:
            times_controller.atualizar_divisao(time[0], 3)


def atualiza_pontuacoes(pontuacao_time1, pontuacao_time2):
    comando = (f"update pontuacao set pontos = '{pontuacao_time1.get_pontos()}', partidas = '{pontuacao_time1.get_partidas()}', "
               f"vitorias = '{pontuacao_time1.get_vitorias()}', empates = '{pontuacao_time1.get_empates()}', "
               f"derrotas = '{pontuacao_time1.get_derrotas()}', golsMarcados = '{pontuacao_time1.get_golsMarcados()}', "
               f"golsSofridos = '{pontuacao_time1.get_golsSofridos()}', saldoGols = '{pontuacao_time1.get_saldoGols()}' "
               f"where codigoTime = '{pontuacao_time1.get_codigoTime()}'")
    executa_query(comando)

    comando = (f"update pontuacao set pontos = '{pontuacao_time2.get_pontos()}', partidas = '{pontuacao_time2.get_partidas()}', "
               f"vitorias = '{pontuacao_time2.get_vitorias()}', empates = '{pontuacao_time2.get_empates()}', "
               f"derrotas = '{pontuacao_time2.get_derrotas()}', golsMarcados = '{pontuacao_time2.get_golsMarcados()}', "
               f"golsSofridos = '{pontuacao_time2.get_golsSofridos()}', saldoGols = '{pontuacao_time2.get_saldoGols()}' "
               f"where codigoTime = '{pontuacao_time2.get_codigoTime()}'")
    executa_query(comando)
