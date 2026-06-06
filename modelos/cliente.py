from modelos.pessoa import Pessoa

class Cliente(Pessoa):
    """Classe Cliente que herda de Pessoa"""
    
    def __init__(self, nome: str, cpf: str, telefone: str, endereco: str):
        super().__init__(nome, telefone)
        self.__cpf = cpf
        self.__endereco = endereco
    
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf
    
    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco: str):
        self.__endereco = endereco
    
    def __str__(self):
        return f"{super().__str__()} | CPF: {self.__cpf} | Endereço: {self.__endereco}"