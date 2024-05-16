class Campeonato:
    def __init__(self, codigo=None, nome=None, divisao=None, ano=None, trimestre=None, formato=None, codigoVencedor=None):
        self._codigo = codigo
        self._nome = nome
        self._divisao = divisao
        self._ano = ano
        self._trimestre = trimestre
        self._formato=formato
        self._codigoVencedor=codigoVencedor

    def get_codigo(self):
        return self._codigo
    
    def set_codigo(self, valor):
        self._codigo = valor

    def get_nome(self):
        return self._nome
    
    def set_nome(self, valor):
        self._nome = valor

    def get_divisao(self):
        return self._divisao
    
    def set_divisao(self, valor):
        self._divisao = valor

    def get_ano(self):
        return self._ano
    
    def set_ano(self, valor):
        self._ano = valor

    def get_trimestre(self):
        return self._trimestre
    
    def set_trimestre(self, valor):
        self._trimestre = valor

    def get_formato(self):
        return self._formato
    
    def set_formato(self, valor):
        self._formato = valor

    def get_codigoVencedor(self):
        return self._codigoVencedor
    
    def set_codigoVencedor(self, valor):
        self._codigoVencedor = valor
