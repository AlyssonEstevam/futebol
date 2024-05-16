import sys
sys.path.append("D:\\python_projetos\\futebol")
from database.conex import executa_query, consulta_query
from modelos.time_modelo import Time


def inserir(nome):
    comando = f"insert into times (nome) values ('{nome}')"
    executa_query(comando)


def seleciona(codigo):
    comando = f"select * from times where codigo = '{codigo}'"
    time_query = consulta_query(comando)

    time = Time()
    for time_item in time_query:
        time.set_codigo(time_item[0])
        time.set_nome(time_item[1])
        time.set_divisao(time_item[2])
        time.set_quantidadeTitulo(time_item[3])
        time.set_quantidadeVitoria(time_item[4])
        time.set_quantidadeDerrota(time_item[5])
        time.set_quantidadeEmpate(time_item[6])
        time.set_quantidadeGols(time_item[7])

    return time


def seleciona_todos():
    comando = "select * from times"
    times = consulta_query(comando)

    lista_times = list()
    for time in times:
        lista_times.append(
            Time(codigo=time[0],
                 nome=time[1],
                 divisao=time[2],
                 quantidadeTitulo=time[3],
                 quantidadeVitoria=time[4],
                 quantidadeDerrota=time[5],
                 quantidadeEmpate=time[6],
                 quantidadeGols=time[7]
            )
        )

    return lista_times


def seleciona_todos_ranking():
    comando = (f"select top 10 * from times "
               f"order by quantidadeTitulo desc, quantidadeVitoria desc, quantidadeEmpate desc, quantidadeDerrota asc, quantidadeGols desc")
    times = consulta_query(comando)

    lista_times = list()
    for time in times:
        lista_times.append(
            Time(codigo=time[0],
                 nome=time[1],
                 divisao=time[2],
                 quantidadeTitulo=time[3],
                 quantidadeVitoria=time[4],
                 quantidadeDerrota=time[5],
                 quantidadeEmpate=time[6],
                 quantidadeGols=time[7]
            )
        )

    return lista_times


def seleciona_codigos(divisao):
    comando = f"select codigo from times where divisao = {divisao}"
    times = [linha[0] for linha in consulta_query(comando)]

    return times


def atualizar_time(time):
    comando = (f"update times set quantidadeTitulo = {time.get_quantidadeTitulo()}, quantidadeVitoria = {time.get_quantidadeVitoria()}, "
               f"quantidadeEmpate = {time.get_quantidadeEmpate()}, quantidadeDerrota = {time.get_quantidadeDerrota()}, "
               f"quantidadeGols = {time.get_quantidadeGols()} "
               f"where codigo = {time.get_codigo()}")
    executa_query(comando)


def atualizar_divisao(codigoTime, divisao):
    comando = (f"update times set divisao = {divisao} "
                f"where codigo = {codigoTime}")
    executa_query(comando)


def rebaixar_times():
    comando = "update times set divisao = 2 where divisao = 3"
    executa_query(comando)
    