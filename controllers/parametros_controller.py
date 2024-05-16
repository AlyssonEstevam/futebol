import sys
sys.path.append("D:\\python_projetos\\futebol")
from database.conex import consulta_query, executa_query
from modelos.parametro_modelo import Parametro


def atualiza_parametros(parametro):
    if(parametro.get_codigoCampeonatoAtual() == None):
        comando = (f"update parametros set ano = '{parametro.get_ano()}', trimestre = '{parametro.get_trimestre()}', "
               f"divisao = '{parametro.get_divisao()}', rodadaAtual = '{parametro.get_rodadaAtual()}', "
               f"partidaAtual = '{parametro.get_partidaAtual()}', codigoCampeonatoAtual = null "
               f"where codigo = '{parametro.get_codigo()}'")
    else:
        comando = (f"update parametros set ano = '{parametro.get_ano()}', trimestre = '{parametro.get_trimestre()}', "
               f"divisao = '{parametro.get_divisao()}', rodadaAtual = '{parametro.get_rodadaAtual()}', "
               f"partidaAtual = '{parametro.get_partidaAtual()}', codigoCampeonatoAtual = '{parametro.get_codigoCampeonatoAtual()}' "
               f"where codigo = '{parametro.get_codigo()}'")
    executa_query(comando)


def seleciona_parametros():
    comando = "select top 1 * from parametros"
    parametro_query = consulta_query(comando)

    parametro = Parametro()
    for parametro_item in parametro_query:
        parametro.set_codigo(parametro_item[0])
        parametro.set_ano(parametro_item[1])
        parametro.set_trimestre(parametro_item[2])
        parametro.set_divisao(parametro_item[3])
        parametro.set_codigoCampeonatoAtual(parametro_item[4])
        parametro.set_rodadaAtual(parametro_item[5])
        parametro.set_partidaAtual(parametro_item[6])

    return parametro
