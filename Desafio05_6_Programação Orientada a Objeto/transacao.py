from datetime import datetime

class Transacao:
    def __init__(self, cliente, produto, quantidade):
        self._cliente = cliente
        self._produto = produto
        self._quantidade = quantidade
        self._data = datetime.now()

    @property
    def cliente(self):
        return self._cliente

    @property
    def produto(self):
        return self._produto

    @property
    def quantidade(self):
        return self._quantidade

    @property
    def data(self):
        return self._data
