import os

class Menu:
    """Classe utilitária para gerenciar menus"""
    
    @staticmethod
    def limpar_tela():
        """Limpa a tela do console"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def exibir_menu_principal():
        """Exibe o menu principal"""
        print("\n" + "="*50)
        print("        FASTDELIVERY EXPRESS")
        print("="*50)
        print("1.  Gerenciar Clientes")
        print("2.  Gerenciar Pedidos")
        print("3.  Gerenciar Entregadores")
        print("4.  Sair")
        print("="*50)
        return input("Escolha uma opção: ")
    
    @staticmethod
    def exibir_menu_clientes():
        """Exibe o menu de clientes"""
        print("\n--- MENU CLIENTES ---")
        print("1. Cadastrar Cliente")
        print("2. Listar Clientes")
        print("3. Buscar Cliente por CPF")
        print("4. Voltar")
        return input("Escolha uma opção: ")
    
    @staticmethod
    def exibir_menu_pedidos():
        """Exibe o menu de pedidos"""
        print("\n--- MENU PEDIDOS ---")
        print("1. Criar Pedido")
        print("2. Listar Pedidos")
        print("3. Atualizar Status")
        print("4. Voltar")
        return input("Escolha uma opção: ")
    
    @staticmethod
    def exibir_tipos_entrega():
        """Exibe os tipos de entrega disponíveis"""
        print("\n--- TIPOS DE ENTREGA ---")
        print("1. Comum (R$ 1.50/km)")
        print("2. Expressa (R$ 3.00/km)")
        print("3. Premium (R$ 5.00/km + R$ 20.00)")
        return input("Escolha o tipo de entrega: ")