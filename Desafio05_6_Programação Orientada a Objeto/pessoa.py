from abc import ABC, abstractmethod

# Classe abstrata Pessoa
class Pessoa(ABC):
    def __init__(self, nome, telefone, endereco):
        self._nome = nome
        self._telefone = telefone
        self._endereco = endereco

    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Endereço: {self.endereco}"

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @abstractmethod
    def get_tipo(self):
        pass
