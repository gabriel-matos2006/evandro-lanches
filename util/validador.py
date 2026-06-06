import re

class Validador:
    """Classe utilitária para validações"""
    
    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        """Valida CPF (formato simplificado)"""
        cpf = re.sub(r'[^0-9]', '', cpf)
        
        if len(cpf) != 11:
            return False
        
        # Verifica se todos os dígitos são iguais
        if cpf == cpf[0] * 11:
            return False
        
        # Validação simplificada (apenas formato)
        return True
    
    @staticmethod
    def validar_telefone(telefone: str) -> bool:
        """Valida telefone"""
        telefone = re.sub(r'[^0-9]', '', telefone)
        return len(telefone) >= 10 and len(telefone) <= 11
    
    @staticmethod
    def validar_peso(peso: float) -> bool:
        """Valida peso do pedido"""
        return peso > 0 and peso <= 100
    
    @staticmethod
    def validar_distancia(distancia: float) -> bool:
        """Valida distância"""
        return distancia > 0 and distancia <= 1000