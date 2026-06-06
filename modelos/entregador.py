from modelos.pessoa import Pessoa

class Entregador(Pessoa):
    """Classe Entregador que herda de Pessoa"""
    
    def __init__(self, nome: str, telefone: str, veiculo: str, cnh: str):
        super().__init__(nome, telefone)
        self.__veiculo = veiculo
        self.__cnh = cnh
    
    @property
    def veiculo(self):
        return self.__veiculo
    
    @veiculo.setter
    def veiculo(self, veiculo: str):
        self.__veiculo = veiculo
    
    @property
    def cnh(self):
        return self.__cnh
    
    @cnh.setter
    def cnh(self, cnh: str):
        self.__cnh = cnh
    
    def __str__(self):
        return f"{super().__str__()} | Veículo: {self.__veiculo} | CNH: {self.__cnh}"