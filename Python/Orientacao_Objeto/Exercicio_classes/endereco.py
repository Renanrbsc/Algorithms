class Endereco:
    def __init__(self, pais: str, estado: str, cidade: str, bairro: str, rua: str):
        self.pais = pais
        self.estado = estado
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua

    @property
    def pais(self) -> str:
        return self._pais
        
    @pais.setter
    def pais(self, pais: str) -> None:
        self._pais = pais
       
    @property
    def estado(self) -> str:
        return self._estado
    
    @estado.setter
    def estado(self, estado: str) -> None:
        self._estado = estado
    
    @property
    def cidade(self) -> str:
        return self._cidade
    
    @cidade.setter
    def cidade(self, cidade: str) -> None:
        self._cidade = cidade
       
    @property
    def bairro(self) -> str:
        return self._bairro
    
    @bairro.setter
    def bairro(self, bairro: str) -> None:
        self._bairro = bairro
        
    @property
    def rua(self) -> str:
        return self._rua
    
    @rua.setter
    def rua(self, rua: str) -> None:
        self._rua = rua

    def __str__(self):
        return f"Pais: {self.pais} \n" \
               f"Estado: {self.estado} \n" \
               f"Cidade: {self.cidade} \n" \
               f"Bairro: {self.bairro} \n" \
               f"Rua: {self.rua} \n"