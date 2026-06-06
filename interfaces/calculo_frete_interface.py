from abc import ABC, abstractmethod

class CalculoFreteInterface(ABC):
    """Interface para cálculo de frete"""
    
    @abstractmethod
    def calcular_frete(self, distancia: float, peso: float) -> float:
        """Método abstrato que será implementado pelas classes de entrega"""
        pass