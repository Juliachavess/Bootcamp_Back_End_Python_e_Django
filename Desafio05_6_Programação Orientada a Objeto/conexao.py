import sqlite3

conexao =sqlite3.connect('banco')
cursor = conexao.cursor()

"""cursor.execute('''
    CREATE TABLE cliente (
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL,
        telefone VARCHAR(20),
        endereco VARCHAR(255)
    );
''')


cursor.execute('''
    CREATE TABLE Fornecedores (
        id_fornecedor INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL,
        telefone VARCHAR(20),
        endereco VARCHAR(255)
);
''')

cursor.execute('''
    CREATE TABLE Produtos (
        id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL,
        quantidade_estoque INT NOT NULL
);
''')

cursor.execute('''
    CREATE TABLE Transacoes (
        id_transacao INTEGER PRIMARY KEY AUTOINCREMENT,
        id_cliente INT,
        id_produto INT,
        quantidade_comprada INT NOT NULL,
        data_compra DATETIME NOT NULL,
        FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
        FOREIGN KEY (id_produto) REFERENCES Produtos(id_produto)
);
''')

# Inserindo dados
cursor.execute('''
INSERT INTO cliente (nome, telefone, endereco) VALUES
    ('Bruna Ribeiro', '123456789', 'Rua A, 123'),
    ('Junior Duarte', '987654321', 'Avenida B, 456')
''')

cursor.execute('''
INSERT INTO Fornecedores (nome, telefone, endereco) VALUES
    ('Uniao', '111111111', 'Rua C, 789'),
    ('Camil', '222222222', 'Avenida D, 101')
''')

cursor.execute('''
INSERT INTO Produtos (nome, quantidade_estoque) VALUES
    ('Acucar', 50),
    ('Arroz', 100)
''')

cursor.execute('''
INSERT INTO Transacoes (id_cliente, id_produto, quantidade_comprada, data_compra) VALUES
    (1, 1, 2, datetime('now')),
    (2, 2, 1, datetime('now'))
''')
"""
#cursor.execute("DELETE FROM Produtos WHERE id_produto > 2")
#cursor.execute('DROP TABLE mercado') 

# consulta SQL
cursor.execute('''
    SELECT P.nome, SUM(T.quantidade_comprada) AS total_vendido
    FROM Transacoes T
    JOIN Produtos P ON T.id_produto = P.id_produto
    GROUP BY P.nome
    ORDER BY total_vendido DESC;
''')

resultados = cursor.fetchall()

# resultados
print("Produto | Total Vendido")
print("-" * 30)
for row in resultados:
    nome_produto, total_vendido = row
    print(f"{nome_produto} | {total_vendido}")

conexao.commit()
conexao.close