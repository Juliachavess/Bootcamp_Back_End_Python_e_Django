from fornecedor import Fornecedor
from cliente import Cliente
from produto import Produto
from mercado import Mercado

# Criando fornecedores
fornecedor1 = Fornecedor("Fornecedor A", "123-4567", "Rua A, 123")
fornecedor2 = Fornecedor("Fornecedor B", "987-6543", "Rua B, 456")

# Exibindo os fornecedores criados
print(f"Fornecedor 1: {fornecedor1}")
print(f"Fornecedor 2: {fornecedor2}")

# Criando produtos
produto1 = Produto("Arroz", ["Alimento", "Grãos"], 100)
produto1.adicionar_fornecedor(fornecedor1)
produto1.adicionar_fornecedor(fornecedor2)

# Exibindo os produtos e seus fornecedores
print(f"Produto: {produto1}")
print("Fornecedores do produto:")
for fornecedor in produto1.fornecedores:
    print(f"- {fornecedor}")

# Criando clientes
cliente1 = Cliente("João Silva", "555-5555", "Rua X, 789")

# Exibindo o cliente criado
print(f"Cliente: {cliente1}")

# Criando mercado
mercado = Mercado()
mercado.adicionar_produto(produto1)
mercado.adicionar_cliente(cliente1)

# Exibindo os produtos e clientes do mercado
print("Produtos no mercado:")
for produto in mercado.produtos:
    print(f"- {produto}")
print("Clientes no mercado:")
for cliente in mercado.clientes:
    print(f"- {cliente}")

# Realizando uma transação
mercado.registrar_transacao(cliente1, produto1, 10)

# Listando transações
print("Transações registradas:")
mercado.listar_transacoes()
