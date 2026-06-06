from interfaces.calculo_frete_interface import CalculoFreteInterface

class EntregaComum(CalculoFreteInterface):
    """Entrega comum - taxa simples"""
    
    def calcular_frete(self, distancia: float, peso: float) -> float:
        # Polimorfismo: implementação específica para entrega comum
        return distancia * 1.5


class EntregaExpressa(CalculoFreteInterface):
    """Entrega expressa - taxa maior"""
    
    def calcular_frete(self, distancia: float, peso: float) -> float:
        # Polimorfismo: implementação específica para entrega expressa
        return distancia * 3.0


class EntregaPremium(CalculoFreteInterface):
    """Entrega premium - taxa VIP"""
    
    def calcular_frete(self, distancia: float, peso: float) -> float:
        # Polimorfismo: implementação específica para entrega premium
        return (distancia * 5.0) + 20.0