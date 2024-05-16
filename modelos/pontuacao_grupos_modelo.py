class PontuacaoGrupos:
    def __init__(self, codigo=None, codigoTime=None, grupo=None, pontos=None, partidas=None, vitorias=None, empates=None, derrotas=None,
                 golsMarcados=None, golsSofridos=None, saldoGols=None):
        self._codigo = codigo 
        self._codigoTime = codigoTime
        self._grupo = grupo 
        self._pontos = pontos 
        self._partidas = partidas 
        self._vitorias = vitorias 
        self._empates = empates 
        self._derrotas = derrotas
        self._golsMarcados = golsMarcados 
        self._golsSofridos = golsSofridos 
        self._saldoGols = saldoGols

    def get_codigo(self):
        return self._codigo

    def set_codigo(self, valor):
            self._codigo = valor

    def get_codigoTime(self):
            return self._codigoTime

    def set_codigoTime(self, valor):
            self._codigoTime = valor

    def get_grupo(self):
            return self._grupo

    def set_grupo(self, valor):
            self._grupo = valor

    def get_pontos(self):
            return self._pontos

    def set_pontos(self, valor):
            self._pontos = valor

    def get_partidas(self):
            return self._partidas

    def set_partidas(self, valor):
            self._partidas = valor

    def get_vitorias(self):
            return self._vitorias

    def set_vitorias(self, valor):
            self._vitorias = valor

    def get_empates(self):
            return self._empates

    def set_empates(self, valor):
            self._empates = valor

    def get_derrotas(self):
            return self._derrotas

    def set_derrotas(self, valor):
            self._derrotas = valor

    def get_golsMarcados(self):
            return self._golsMarcados

    def set_golsMarcados(self, valor):
            self._golsMarcados = valor

    def get_golsSofridos(self):
            return self._golsSofridos

    def set_golsSofridos(self, valor):
            self._golsSofridos = valor

    def get_saldoGols(self):
            return self._saldoGols

    def set_saldoGols(self, valor):
            self._saldoGols = valor
            