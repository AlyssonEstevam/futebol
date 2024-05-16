import sys
sys.path.append("D:\\python_projetos\\futebol")
from database.conex import executa_query, consulta_query
from modelos.campeonato_modelo import Campeonato


def inserir(campeonato):
    comando = (f"insert into campeonatos ([nome],[divisao],[ano],[trimestre],[formato])"
               f" values ('{campeonato.get_nome()}','{campeonato.get_divisao()}','{campeonato.get_ano()}',"
               f"'{campeonato.get_trimestre()}','{campeonato.get_formato()}')")
    executa_query(comando)


def seleciona(codigo):
    comando = f"select * from campeonatos where codigo = '{codigo}'"
    campeonato_query = consulta_query(comando)

    campeonato = Campeonato()
    for campeonato_item in campeonato_query:
        campeonato.set_codigo(campeonato_item[0])
        campeonato.set_nome(campeonato_item[1])
        campeonato.set_divisao(campeonato_item[2])
        campeonato.set_ano(campeonato_item[3])
        campeonato.set_trimestre(campeonato_item[4])
        campeonato.set_formato(campeonato_item[5])
        campeonato.set_codigoVencedor(campeonato_item[6])

    return campeonato


def seleciona_atual(ano, trimestre, divisao):
    comando = f"select codigo from campeonatos where ano = '{ano}' and trimestre = '{trimestre}' and divisao = '{divisao}'"
    campeonato_query = consulta_query(comando)
    
    if(len(campeonato_query) == 0):
        return 0
    else:
        return campeonato_query[0][0]


def seleciona_todos():
    comando = "select * from campeonatos"
    campeonatos = consulta_query(comando)

    lista_campeonatos = list()
    for campeonato in campeonatos:
        lista_campeonatos.append(
            Campeonato(codigo=campeonato[0],
                 nome=campeonato[1],
                 divisao=campeonato[2],
                 ano=campeonato[3],
                 trimestre=campeonato[4],
                 formato=campeonato[5],
                 codigoVencedor=campeonato[6]
            )
        )

    return lista_campeonatos


def atualiza_campeao(codigo, codigoTime):
    comando = (f"update campeonatos set codigoVencedor = {codigoTime} "
               f"where codigo = {codigo}")
    executa_query(comando)
    