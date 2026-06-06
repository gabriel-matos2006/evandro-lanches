from services.cliente_service import ClienteService
from services.pedido_service import PedidoService
from util.menu import Menu

def main():
    """Função principal do sistema"""
    
    # Inicialização dos serviços
    cliente_service = ClienteService()
    pedido_service = PedidoService(cliente_service)
    
    while True:
        Menu.limpar_tela()
        opcao = Menu.exibir_menu_principal()
        
        if opcao == "1":  # Gerenciar Clientes
            gerenciar_clientes(cliente_service)
        
        elif opcao == "2":  # Gerenciar Pedidos
            gerenciar_pedidos(pedido_service)
        
        elif opcao == "3":  # Gerenciar Entregadores
            print("\n🚧 Funcionalidade em desenvolvimento...")
            input("Pressione Enter para continuar...")
        
        elif opcao == "4":  # Sair
            print("\nObrigado por usar o FastDelivery Express!")
            break
        
        else:
            print("\nOpção inválida!")
            input("Pressione Enter para continuar...")


def gerenciar_clientes(cliente_service):
    """Gerencia as operações de cliente"""
    while True:
        Menu.limpar_tela()
        opcao = Menu.exibir_menu_clientes()
        
        if opcao == "1":  # Cadastrar cliente
            print("\n--- CADASTRO DE CLIENTE ---")
            nome = input("Nome: ")
            cpf = input("CPF: ")
            telefone = input("Telefone: ")
            endereco = input("Endereço: ")
            
            cliente_service.cadastrar_cliente(nome, cpf, telefone, endereco)
            input("\nPressione Enter para continuar...")
        
        elif opcao == "2":  # Listar clientes
            print("\n--- LISTA DE CLIENTES ---")
            cliente_service.listar_clientes()
            input("\nPressione Enter para continuar...")
        
        elif opcao == "3":  # Buscar cliente
            print("\n--- BUSCAR CLIENTE ---")
            cpf = input("Digite o CPF do cliente: ")
            cliente = cliente_service.buscar_cliente_por_cpf(cpf)
            
            if cliente:
                print(f"\nCliente encontrado:\n{cliente}")
            else:
                print("\nCliente não encontrado!")
            
            input("\nPressione Enter para continuar...")
        
        elif opcao == "4":  # Voltar
            break
        
        else:
            print("\nOpção inválida!")
            input("Pressione Enter para continuar...")


def gerenciar_pedidos(pedido_service):
    """Gerencia as operações de pedido"""
    while True:
        Menu.limpar_tela()
        opcao = Menu.exibir_menu_pedidos()
        
        if opcao == "1":  # Criar pedido
            print("\n--- CRIAR PEDIDO ---")
            cpf = input("CPF do cliente: ")
            
            try:
                peso = float(input("Peso do pacote (kg): "))
                distancia = float(input("Distância (km): "))
            except ValueError:
                print("Valor inválido!")
                input("Pressione Enter para continuar...")
                continue
            
            tipo_opcao = Menu.exibir_tipos_entrega()
            
            tipo_map = {
                "1": "comum",
                "2": "expressa",
                "3": "premium"
            }
            
            if tipo_opcao in tipo_map:
                pedido_service.criar_pedido(cpf, peso, distancia, tipo_map[tipo_opcao])
            else:
                print("Tipo de entrega inválido!")
            
            input("\nPressione Enter para continuar...")
        
        elif opcao == "2":  # Listar pedidos
            print("\n--- LISTA DE PEDIDOS ---")
            pedido_service.listar_pedidos()
            input("\nPressione Enter para continuar...")
        
        elif opcao == "3":  # Atualizar status
            print("\n--- ATUALIZAR STATUS ---")
            codigo = input("Código do pedido: ")
            
            print("\nStatus disponíveis:")
            print("1. Em preparação")
            print("2. Saiu para entrega")
            print("3. Entregue")
            print("4. Cancelado")
            
            status_opcao = input("Escolha o novo status: ")
            pedido_service.atualizar_status(codigo, status_opcao)
            input("\nPressione Enter para continuar...")
        
        elif opcao == "4":  # Voltar
            break
        
        else:
            print("\nOpção inválida!")
            input("Pressione Enter para continuar...")


if __name__ == "__main__":
    main()