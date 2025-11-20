import sqlite3
from datetime import datetime

# Nome da base de dados SQLite
DB = "tabacaria.db"


# --------------------------
# CONEXÃO
# --------------------------
def conectar():
    #Cria e retorna uma conexão com a base de dados SQLite
    return sqlite3.connect(DB)


# --------------------------
# PRODUTOS
# --------------------------
def menu_produtos():
    #Menu de produtos
    while True:
        print("\n--- MENU PRODUTOS ---")
        print("1 - Listar produtos")
        print("2 - Adicionar produto")
        print("3 - Procurar produto")
        print("4 - Alterar preço")
        print("0 - Voltar")

        op = input("Opção: ")

        #Chama a função correspondente à escolha
        if op == "1":
            listar_produtos()
        elif op == "2":
            adicionar_produto()
        elif op == "3":
            procurar_produto()
        elif op == "4":
            alterar_preco()
        elif op == "0":
            break
        else:
            print("Opção inválida!")


def listar_produtos():
    #Lista todos os produtos ativos na base de dados
    conn = conectar()
    cur = conn.cursor() # Ponte que permite executar comandos como o "SELECT; UPDATE ETC..."
    cur.execute("SELECT id, nome, categoria, preco, stock FROM produto WHERE ativo = 1")
    produtos = cur.fetchall()
    conn.close()

    print("\n--- LISTA DE PRODUTOS ---")
    for p in produtos:
        print(f"{p[0]} - {p[1]} | {p[2]} | {p[3]}€ | Stock: {p[4]}")


def adicionar_produto():
    # Adiciona um novo produto à base de dados
    nome = input("Nome: ")
    categoria = input("Categoria: ")
    preco = float(input("Preço: "))
    stock = int(input("Stock inicial: "))
    fornecedor = int(input("ID Fornecedor: "))

    conn = conectar()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO produto (nome, categoria, preco, stock, fornecedor_id)
        VALUES (?, ?, ?, ?, ?)
    """, (nome, categoria, preco, stock, fornecedor))
    conn.commit()
    conn.close()
    print("Produto adicionado com sucesso!")


def procurar_produto():
    # Procura produtos pelo nome ou parte do nome
    texto = input("Nome ou parte do nome: ")

    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT id, nome, preco, stock FROM produto WHERE nome LIKE ?", ("%" + texto + "%",))
    produtos = cur.fetchall()
    conn.close()

    print("\n--- RESULTADOS ---")
    for p in produtos:
        print(f"{p[0]} - {p[1]} | {p[2]}€ | Stock: {p[3]}")


def alterar_preco():
    #altera o preco de um produto especifiico
    pid = int(input("ID do produto: "))
    novo_preco = float(input("Novo preço: "))

    conn = conectar()
    cur = conn.cursor()
    cur.execute("UPDATE produto SET preco = ? WHERE id = ?", (novo_preco, pid))
    conn.commit()
    conn.close()
    print("Preço atualizado!")


# --------------------------
# STOCK
# --------------------------
def menu_stock():
    #Menu interativo para gerir o stock de produtos.
    while True:
        print("\n--- MENU STOCK ---")
        print("1 - Aumentar stock")
        print("2 - Diminuir stock")
        print("0 - Voltar")

        op = input("Opção: ")

        if op == "1":
            alterar_stock(True)  # Aumenta stock
        elif op == "2":
            alterar_stock(False)  # Diminui stock
        elif op == "0":
            break
        else:
            print("Opção inválida!")


def alterar_stock(aumentar=True):
    #Aumenta ou diminui o stock de um produto.
    pid = int(input("ID Produto: "))
    qtd = int(input("Quantidade: "))

    conn = conectar()
    cur = conn.cursor()

    if aumentar:
        cur.execute("UPDATE produto SET stock = stock + ? WHERE id = ?", (qtd, pid))
        print("Stock aumentado!")
    else:
        cur.execute("UPDATE produto SET stock = stock - ? WHERE id = ?", (qtd, pid))
        print("Stock diminuído!")

    conn.commit()
    conn.close()


# --------------------------
# CLIENTES
# --------------------------
def menu_clientes():
    #Menu interativo para clientes.
    while True:
        print("\n--- MENU CLIENTES ---")
        print("1 - Listar clientes")
        print("2 - Adicionar cliente")
        print("0 - Voltar")

        op = input("Opção: ")

        if op == "1":
            listar_clientes()
        elif op == "2":
            adicionar_cliente()
        elif op == "0":
            break
        else:
            print("Opção inválida!")


def listar_clientes():
    #Lista todos os clientes cadastrados.
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT id, nome, telefone FROM cliente")
    clientes = cur.fetchall()
    conn.close()

    print("\n--- CLIENTES ---")
    for c in clientes:
        print(f"{c[0]} - {c[1]} | {c[2]}")


def adicionar_cliente():
    #Adiciona um novo cliente à base de dados.
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")

    conn = conectar()
    cur = conn.cursor()
    cur.execute("INSERT INTO cliente (nome, telefone, email) VALUES (?, ?, ?)", (nome, telefone, email))
    conn.commit()
    conn.close()

    print("Cliente adicionado!")


# --------------------------
# FUNCIONÁRIOS
# --------------------------
def menu_funcionarios():
    #Menu interativo para funcionários.
    while True:
        print("\n--- MENU FUNCIONÁRIOS ---")
        print("1 - Listar funcionários")
        print("2 - Adicionar funcionário")
        print("0 - Voltar")

        op = input("Opção: ")

        if op == "1":
            listar_funcionarios()
        elif op == "2":
            adicionar_funcionario()
        elif op == "0":
            break
        else:
            print("Opção inválida!")


def adicionar_funcionario():
    # addiciona um funcionario à base de dados
    nome = input("Nome: ")
    user = input("Nome de utilizador: ")
    pw = input("Senha (sem hash): ")
    role = input("Função (admin/funcionario): ")
    conn = conectar()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO funcionario (nome, username, password_hash, role)
        VALUES (?, ?, ?, ?)
    """, (nome, user, pw, role))
    conn.commit()
    conn.close()

    print("funcionario adicionado!")


# ------------------------------------
# MENU VENDAS
# ------------------------------------
def menu_vendas():
    while True:
        print("\n--- MENU VENDAS ---")
        print("1 - Nova venda")
        print("2 - Listar vendas")
        print("0 - Voltar")

        op = input("Opção: ")

        if op == "1":
            nova_venda()
        elif op == "2":
            listar_vendas()
        elif op == "0":
            break
        else:
            print("Opção inválida!")


def nova_venda():
    funcionario = int(input("ID Funcionário: "))
    cliente = int(input("ID Cliente: "))

    itens = []

    while True:
        pid = int(input("Produto ID (0 para terminar): "))
        if pid == 0:
            break
        qtd = int(input("Quantidade: "))
        itens.append((pid, qtd))

    total = 0
    conn = conectar()
    cur = conn.cursor()

    for pid, qtd in itens:
        cur.execute("SELECT preco FROM produto WHERE id = %s", (pid,))
        preco = cur.fetchone()[0]
        total += preco * qtd

    cur.execute("INSERT INTO venda (total, funcionario_id, cliente_id) VALUES (%s, %s, %s)",
                (total, funcionario, cliente))
    venda_id = cur.lastrowid

    for pid, qtd in itens:
        cur.execute("SELECT preco FROM produto WHERE id = %s", (pid,))
        preco = cur.fetchone()[0]
        subtotal = preco * qtd

        cur.execute("""
            INSERT INTO item_venda (venda_id, produto_id, quantidade, preco_unitario, subtotal)
            VALUES (%s, %s, %s, %s, %s)
        """, (venda_id, pid, qtd, preco, subtotal))

        cur.execute("UPDATE produto SET stock = stock - %s WHERE id = %s", (qtd, pid))

    conn.commit()
    conn.close()

    print(f"Venda registada! ID: {venda_id}")
