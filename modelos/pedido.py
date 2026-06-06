from enum import Enum
from modelos.cliente import Cliente
from modelos.entrega import EntregaComum, EntregaExpressa, EntregaPremium

class StatusPedido(Enum):
    EM_PREPARACAO = "Em preparação"
    SAIU_PARA_ENTREGA = "Saiu para entrega"
    ENTREGUE = "Entregue"
    CANCELADO = "Cancelado"

class Pedido:
    """Classe que representa um pedido"""
    
    def __init__(self, codigo: str, cliente: Cliente, peso: float, 
                 distancia: float, tipo_entrega: str):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__peso = peso
        self.__distancia = distancia
        self.__status = StatusPedido.EM_PREPARACAO
        self.__tipo_entrega = tipo_entrega
        self.__frete = self._calcular_frete()
    
    def _calcular_frete(self) -> float:
        """Calcula o frete baseado no tipo de entrega (polimorfismo)"""
        if self.__tipo_entrega == "comum":
            entrega = EntregaComum()
        elif self.__tipo_entrega == "expressa":
            entrega = EntregaExpressa()
        elif self.__tipo_entrega == "premium":
            entrega = EntregaPremium()
        else:
            raise ValueError("Tipo de entrega inválido")
        
        return entrega.calcular_frete(self.__distancia, self.__peso)
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, novo_status: StatusPedido):
        self.__status = novo_status
    
    @property
    def frete(self):
        return self.__frete
    
    def __str__(self):
        return f"Pedido: {self.__codigo} | Cliente: {self.__cliente.nome} | Status: {self.__status.value} | Frete: R${self.__frete:.2f}"