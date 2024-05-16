class Parametro:
    def __init__(self, codigo=None, ano=None, trimestre=None, divisao=None, codigoCampeonatoAtual=None, rodadaAtual=None, partidaAtual=None):
        self._codigo = codigo
        self._ano = ano
        self._trimestre = trimestre
        self._divisao = divisao
        self._codigoCampeonatoAtual=codigoCampeonatoAtual
        self._rodadaAtual=rodadaAtual
        self._partidaAtual=partidaAtual

    def get_codigo(self):
        return self._codigo
    
    def set_codigo(self, valor):
        self._codigo = valor

    def get_ano(self):
        return self._ano
    
    def set_ano(self, valor):
        self._ano = valor

    def get_trimestre(self):
        return self._trimestre
    
    def set_trimestre(self, valor):
        self._trimestre = valor

    def get_divisao(self):
        return self._divisao
    
    def set_divisao(self, valor):
        self._divisao = valor

    def get_codigoCampeonatoAtual(self):
        return self._codigoCampeonatoAtual
    
    def set_codigoCampeonatoAtual(self, valor):
        self._codigoCampeonatoAtual = valor

    def get_rodadaAtual(self):
        return self._rodadaAtual
    
    def set_rodadaAtual(self, valor):
        self._rodadaAtual = valor

    def get_partidaAtual(self):
        return self._partidaAtual
    
    def set_partidaAtual(self, valor):
        self._partidaAtual = valor
