import sys
sys.path.append("D:\\python_projetos\\futebol")
from database.conex import executa_query, consulta_query
from modelos.pontuacao_grupos_modelo import PontuacaoGrupos
import controllers.times_controller as times_controller


def limpa_tabela():
    comando = f"truncate table pontuacao_grupos"
    executa_query(comando)


def inserir_inicial(codigoTime, grupo):
    comando = f"insert into pontuacao_grupos (codigoTime, grupo) values ('{codigoTime}','{grupo}')"
    executa_query(comando)


def seleciona_pontuacao_time(codigoTime):
    comando = f"select * from pontuacao_grupos where codigoTime = '{codigoTime}'"
    time_query = consulta_query(comando)

    time_pontuacao = PontuacaoGrupos()
    for time in time_query:
        time_pontuacao.set_codigo(time[0])
        time_pontuacao.set_codigoTime(time[1])
        time_pontuacao.set_grupo(time[2])
        time_pontuacao.set_pontos(time[3])
        time_pontuacao.set_partidas(time[4])
        time_pontuacao.set_vitorias(time[5])
        time_pontuacao.set_empates(time[6])
        time_pontuacao.set_derrotas(time[7])
        time_pontuacao.set_golsMarcados(time[8])
        time_pontuacao.set_golsSofridos(time[9])
        time_pontuacao.set_saldoGols(time[10])

    return time_pontuacao


def atualiza_pontuacoes(pontuacao_time1, pontuacao_time2):
    comando = (f"update pontuacao_grupos set pontos = '{pontuacao_time1.get_pontos()}', partidas = '{pontuacao_time1.get_partidas()}', "
               f"vitorias = '{pontuacao_time1.get_vitorias()}', empates = '{pontuacao_time1.get_empates()}', "
               f"derrotas = '{pontuacao_time1.get_derrotas()}', golsMarcados = '{pontuacao_time1.get_golsMarcados()}', "
               f"golsSofridos = '{pontuacao_time1.get_golsSofridos()}', saldoGols = '{pontuacao_time1.get_saldoGols()}' "
               f"where codigoTime = '{pontuacao_time1.get_codigoTime()}'")
    executa_query(comando)

    comando = (f"update pontuacao_grupos set pontos = '{pontuacao_time2.get_pontos()}', partidas = '{pontuacao_time2.get_partidas()}', "
               f"vitorias = '{pontuacao_time2.get_vitorias()}', empates = '{pontuacao_time2.get_empates()}', "
               f"derrotas = '{pontuacao_time2.get_derrotas()}', golsMarcados = '{pontuacao_time2.get_golsMarcados()}', "
               f"golsSofridos = '{pontuacao_time2.get_golsSofridos()}', saldoGols = '{pontuacao_time2.get_saldoGols()}' "
               f"where codigoTime = '{pontuacao_time2.get_codigoTime()}'")
    executa_query(comando)


def seleciona_pontuacao_ordenada_grupo(grupo):
    comando = (f"select t.nome, p.pontos, p.partidas, p.vitorias, p.empates, p.derrotas, p.saldoGols, p.golsMarcados, p.golsSofridos, t.codigo "
               f"from pontuacao_grupos p inner join times t on t.codigo = p.codigoTime "
               f"where p.grupo = '{grupo}' "
               f"order by pontos desc, vitorias desc, empates desc, derrotas, saldoGols desc, golsMarcados desc, golsSofridos")       
    pontuacao_query = consulta_query(comando)

    return pontuacao_query
