class Time:
    def __init__(self, codigo=None, nome=None, divisao=None, quantidadeTitulo=None, quantidadeVitoria=None, 
                 quantidadeDerrota=None, quantidadeEmpate=None, quantidadeGols=None):
        self._codigo = codigo
        self._nome = nome
        self._divisao = divisao
        self._quantidadeTitulo=quantidadeTitulo
        self._quantidadeVitoria=quantidadeVitoria
        self._quantidadeDerrota=quantidadeDerrota
        self._quantidadeEmpate=quantidadeEmpate
        self._quantidadeGols=quantidadeGols

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

    def get_quantidadeVitoria(self):
        return self._quantidadeVitoria
    
    def set_quantidadeVitoria(self, valor):
        self._quantidadeVitoria = valor

    def get_quantidadeDerrota(self):
        return self._quantidadeDerrota
    
    def set_quantidadeDerrota(self, valor):
        self._quantidadeDerrota = valor

    def get_quantidadeEmpate(self):
        return self._quantidadeEmpate
    
    def set_quantidadeEmpate(self, valor):
        self._quantidadeEmpate = valor

    def get_quantidadeTitulo(self):
        return self._quantidadeTitulo
    
    def set_quantidadeTitulo(self, valor):
        self._quantidadeTitulo = valor

    def get_quantidadeGols(self):
        return self._quantidadeGols
    
    def set_quantidadeGols(self, valor):
        self._quantidadeGols = valor