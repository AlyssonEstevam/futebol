class Partida:
    def __init__(self, codigo=None,codigoCampeonato=None,numeroRodada=None,numeroPartida=None,codigoTime1=None,
                 golsTime1=None,codigoTime2=None,golsTime2=None,flagEmpate=None,codigoTimeVitoria=None,
                 codigoTimeDerrota=None,flagPenalti=None,penaltisTime1=None,penaltisTime2=None,flagFinalizada=None):
        self._codigo = codigo
        self._codigoCampeonato = codigoCampeonato
        self._numeroRodada = numeroRodada
        self._numeroPartida = numeroPartida
        self._codigoTime1 = codigoTime1
        self._golsTime1 = golsTime1
        self._codigoTime2 = codigoTime2
        self._golsTime2 = golsTime2
        self._flagEmpate = flagEmpate
        self._codigoTimeVitoria = codigoTimeVitoria
        self._codigoTimeDerrota = codigoTimeDerrota
        self._flagPenalti = flagPenalti
        self._penaltisTime1 = penaltisTime1
        self._penaltisTime2 = penaltisTime2
        self._flagFinalizada = flagFinalizada

    def get_codigo(self):
            return self._codigo

    def set_codigo(self, valor):
            self._codigo = valor

    def get_codigoCampeonato(self):
            return self._codigoCampeonato

    def set_codigoCampeonato(self, valor):
            self._codigoCampeonato = valor

    def get_numeroRodada(self):
            return self._numeroRodada

    def set_numeroRodada(self, valor):
            self._numeroRodada = valor

    def get_numeroPartida(self):
            return self._numeroPartida

    def set_numeroPartida(self, valor):
            self._numeroPartida = valor

    def get_codigoTime1(self):
            return self._codigoTime1

    def set_codigoTime1(self, valor):
            self._codigoTime1 = valor

    def get_golsTime1(self):
            return self._golsTime1

    def set_golsTime1(self, valor):
            self._golsTime1 = valor

    def get_codigoTime2(self):
            return self._codigoTime2

    def set_codigoTime2(self, valor):
            self._codigoTime2 = valor

    def get_golsTime2(self):
            return self._golsTime2

    def set_golsTime2(self, valor):
            self._golsTime2 = valor

    def get_flagEmpate(self):
            return self._flagEmpate

    def set_flagEmpate(self, valor):
            self._flagEmpate = valor

    def get_codigoTimeVitoria(self):
            return self._codigoTimeVitoria

    def set_codigoTimeVitoria(self, valor):
            self._codigoTimeVitoria = valor

    def get_codigoTimeDerrota(self):
            return self._codigoTimeDerrota

    def set_codigoTimeDerrota(self, valor):
            self._codigoTimeDerrota = valor

    def get_flagPenalti(self):
            return self._flagPenalti

    def set_flagPenalti(self, valor):
            self._flagPenalti = valor

    def get_penaltisTime1(self):
            return self._penaltisTime1

    def set_penaltisTime1(self, valor):
            self._penaltisTime1 = valor

    def get_penaltisTime2(self):
            return self._penaltisTime2

    def set_penaltisTime2(self, valor):
            self._penaltisTime2 = valor

    def get_flagFinalizada(self):
            return self._flagFinalizada

    def set_flagFinalizada(self, valor):
            self._flagFinalizada = valor