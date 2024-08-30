from produto import Produto
from cliente import Cliente
from transacao import Transacao

class Mercado:
    def __init__(self):
        self.produtos = []
        self.clientes = []
        self.transacoes = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def registrar_transacao(self, cliente, produto, quantidade):
        produto.reduzir_estoque(quantidade)
        transacao = Transacao(cliente, produto, quantidade)
        self.transacoes.append(transacao)

    def listar_transacoes(self):
        for transacao in self.transacoes:
            print(f"Data: {transacao.data}, Cliente: {transacao.cliente.nome}, Produto: {transacao.produto.nome}, Quantidade: {transacao.quantidade}")

    def __str__(self):
        produtos_str = '\n'.join([f"- {produto.nome}, Estoque: {produto.quantidade_em_estoque}" for produto in self.produtos])
        clientes_str = '\n'.join([f"- {cliente.nome}, Telefone: {cliente.telefone}" for cliente in self.clientes])
        transacoes_str = '\n'.join([f"Data: {transacao.data}, Cliente: {transacao.cliente.nome}, Produto: {transacao.produto.nome}, Quantidade: {transacao.quantidade}" for transacao in self.transacoes])

        return (f"Produtos no Mercado:\n{produtos_str}\n\n"
                f"Clientes no Mercado:\n{clientes_str}\n\n"
                f"Transações Registradas:\n{transacoes_str}")
