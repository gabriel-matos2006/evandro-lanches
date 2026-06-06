from modelos.cliente import Cliente
from util.validador import Validador

class ClienteService:
    """Serviço para gerenciar clientes"""
    
    def __init__(self):
        self.__clientes = []
    
    def cadastrar_cliente(self, nome: str, cpf: str, telefone: str, endereco: str) -> bool:
        """Cadastra um novo cliente"""
        if not Validador.validar_cpf(cpf):
            print("CPF inválido!")
            return False
        
        if self.buscar_cliente_por_cpf(cpf):
            print("Cliente já cadastrado!")
            return False
        
        cliente = Cliente(nome, cpf, telefone, endereco)
        self.__clientes.append(cliente)
        print(f"Cliente {nome} cadastrado com sucesso!")
        return True
    
    def listar_clientes(self):
        """Lista todos os clientes"""
        if not self.__clientes:
            print("Nenhum cliente cadastrado.")
            return
        
        for i, cliente in enumerate(self.__clientes, 1):
            print(f"{i}. {cliente}")
    
    def buscar_cliente_por_cpf(self, cpf: str):
        """Busca cliente por CPF"""
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return cliente
        return None
    
    def get_todos_clientes(self):
        return self.__clientes