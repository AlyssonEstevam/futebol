import sys
sys.path.append("D:\\python_projetos\\futebol")
from database.conex import executa_query, consulta_query
from modelos.partida_modelo import Partida


def inserir(partida):
    comando = (f"insert into [dbo].[partidas] ([codigoCampeonato],[numeroRodada],[numeroPartida],[codigoTime1],[codigoTime2])"
               f"values('{partida.get_codigoCampeonato()}','{partida.get_numeroRodada()}','{partida.get_numeroPartida()}','{partida.get_codigoTime1()}','{partida.get_codigoTime2()}')")
    executa_query(comando)


def verifica_partida_ativa(codigo_campeonato):
    codigo_campeonato = 0 if(codigo_campeonato == None) else codigo_campeonato
    comando = f"select top 1 codigo from partidas where codigoCampeonato = '{codigo_campeonato}' and flagFinalizada = 0"
    resultado = consulta_query(comando)
    if(len(resultado) == 0):
        return False
    else:
        return True
    

def consulta_proxima_partida(codigo_campeonato_atual):
    comando = (f"select top 1 * from partidas where codigoCampeonato = '{codigo_campeonato_atual}' "
               f"and flagFinalizada = 0 order by codigo")
    partida_query = consulta_query(comando)

    partida = Partida()
    for partida_item in partida_query:
        partida.set_codigo(partida_item[0])
        partida.set_codigoCampeonato(partida_item[1])
        partida.set_numeroRodada(partida_item[2])
        partida.set_numeroPartida(partida_item[3])
        partida.set_codigoTime1(partida_item[4])
        partida.set_golsTime1(partida_item[5])
        partida.set_codigoTime2(partida_item[6])
        partida.set_golsTime2(partida_item[7])
        partida.set_flagEmpate(partida_item[8])
        partida.set_codigoTimeVitoria(partida_item[9])
        partida.set_codigoTimeDerrota(partida_item[10])
        partida.set_flagPenalti(partida_item[11])
        partida.set_penaltisTime1(partida_item[12])
        partida.set_penaltisTime2(partida_item[13])
        partida.set_flagFinalizada(partida_item[14])

    return partida
    

def atualiza_resultado_partida(partida, amistoso=False):
    if(amistoso):
        comando = (f"insert into amistosos ([codigoTime1],[golsTime1],[codigoTime2],[golsTime2])" 
                   f"values('{partida.get_codigoTime1()}','{partida.get_golsTime1()}','{partida.get_codigoTime2()}','{partida.get_golsTime2()}')")
    elif(partida.get_flagPenalti()):
        print('Funcionalidade ainda não finalizada')
    elif(partida.get_flagEmpate()):
        comando = (f"update partidas set golsTime1 = '{partida.get_golsTime1()}', golsTime2 = '{partida.get_golsTime2()}', "
                   f"flagEmpate = '{partida.get_flagEmpate()}', flagFinalizada = '{partida.get_flagFinalizada()}' "
                   f"where codigo = '{partida.get_codigo()}'")
    else:
        comando = (f"update partidas set golsTime1 = '{partida.get_golsTime1()}', golsTime2 = '{partida.get_golsTime2()}', "
                   f"codigoTimeVitoria = '{partida.get_codigoTimeVitoria()}', codigoTimeDerrota = '{partida.get_codigoTimeDerrota()}', "
                   f"flagFinalizada = '{partida.get_flagFinalizada()}' "
                   f"where codigo = '{partida.get_codigo()}'")
    executa_query(comando)


def consulta_ultima_partida():
    comando = "select top 1 numeroPartida from partidas where flagFinalizada = 0 order by codigo desc"
    partida_query = consulta_query(comando)

    if(len(partida_query) == 0):
        return None
    else:
        return partida_query[0][0]

def consulta_partidas_restantes():
    comando = "select count(*) from partidas where flagFinalizada = 0"
    partida_query = consulta_query(comando)

    if(len(partida_query) == 0):
        return None
    else:
        return partida_query[0][0]


def consulta_partidas_campeonato(codigo_campeonato_atual):
    comando = (f"select p.numeroRodada, t1.nome, p.golsTime1, t2.nome, p.golsTime2, p.flagFinalizada "  
               f"from partidas p inner join times t1 on t1.codigo = p.codigoTime1 " 
               f"inner join times t2 on t2.codigo = p.codigoTime2 "
               f"where codigoCampeonato = '{codigo_campeonato_atual}' "
               f"order by p.codigo")
    partida_query = consulta_query(comando)

    if(len(partida_query) == 0):
        return None
    else:
        return partida_query
