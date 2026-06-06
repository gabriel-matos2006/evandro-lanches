from modelos.pedido import Pedido, StatusPedido
from services.cliente_service import ClienteService

class PedidoService:
    """Serviço para gerenciar pedidos"""
    
    def __init__(self, cliente_service: ClienteService):
        self.__pedidos = []
        self.__cliente_service = cliente_service
        self.__contador_codigo = 1
    
    def criar_pedido(self, cpf_cliente: str, peso: float, distancia: float, tipo_entrega: str):
        """Cria um novo pedido"""
        cliente = self.__cliente_service.buscar_cliente_por_cpf(cpf_cliente)
        
        if not cliente:
            print("Cliente não encontrado!")
            return None
        
        codigo = f"PED-{self.__contador_codigo:04d}"
        pedido = Pedido(codigo, cliente, peso, distancia, tipo_entrega)
        self.__pedidos.append(pedido)
        self.__contador_codigo += 1
        
        print(f"Pedido {codigo} criado com sucesso! Frete: R${pedido.frete:.2f}")
        return pedido
    
    def listar_pedidos(self):
        """Lista todos os pedidos"""
        if not self.__pedidos:
            print("Nenhum pedido cadastrado.")
            return
        
        for i, pedido in enumerate(self.__pedidos, 1):
            print(f"{i}. {pedido}")
    
    def atualizar_status(self, codigo: str, novo_status: str):
        """Atualiza o status de um pedido"""
        pedido = self.buscar_pedido_por_codigo(codigo)
        
        if not pedido:
            print("Pedido não encontrado!")
            return False
        
        status_map = {
            "1": StatusPedido.EM_PREPARACAO,
            "2": StatusPedido.SAIU_PARA_ENTREGA,
            "3": StatusPedido.ENTREGUE,
            "4": StatusPedido.CANCELADO
        }
        
        if novo_status in status_map:
            pedido.status = status_map[novo_status]
            print(f"Status do pedido {codigo} atualizado para {pedido.status.value}")
            return True
        else:
            print("Status inválido!")
            return False
    
    def buscar_pedido_por_codigo(self, codigo: str):
        """Busca pedido pelo código"""
        for pedido in self.__pedidos:
            if pedido.codigo == codigo:
                return pedido
        return None