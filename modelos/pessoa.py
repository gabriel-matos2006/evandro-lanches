from abc import ABC, abstractmethod

class Pessoa(ABC):
    """Superclasse abstrata que representa uma pessoa no sistema"""
    
    def __init__(self, nome: str, telefone: str):
        self.__nome = nome
        self.__telefone = telefone
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
    
    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone: str):
        self.__telefone = telefone
    
    def __str__(self):
        return f"Nome: {self.__nome} | Telefone: {self.__telefone}"