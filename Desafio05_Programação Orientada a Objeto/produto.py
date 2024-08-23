class Produto:
    def __init__(self, nome, categorias, quantidade_em_estoque):
        self._nome = nome
        self._categorias = categorias
        self._quantidade_em_estoque = quantidade_em_estoque
        self.fornecedores = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def categorias(self):
        return self._categorias

    @categorias.setter
    def categorias(self, categorias):
        self._categorias = categorias

    @property
    def quantidade_em_estoque(self):
        return self._quantidade_em_estoque
    
    @quantidade_em_estoque.setter
    def quantidade_em_estoque(self, quantidade):
        if quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa.")
        self._quantidade_em_estoque = quantidade

    def adicionar_fornecedor(self, fornecedor):
        self.fornecedores.append(fornecedor)

    def reduzir_estoque(self, quantidade): # Garante que o estoque não fique negativo
        if quantidade > self._quantidade_em_estoque:
            raise ValueError("Quantidade insuficiente em estoque.")
        self._quantidade_em_estoque -= quantidade

    def __str__(self):
        fornecedores_str = ', '.join([fornecedor.nome for fornecedor in self.fornecedores])
        return (f"Nome: {self.nome}, Categorias: {self.categorias}, "
                f"Quantidade em estoque: {self.quantidade_em_estoque}, Fornecedores: {fornecedores_str}")
