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


# ------------------------------------
# MENU PRINCIPAL
# ------------------------------------
def menu_principal():
    while True:
        print(r"""
 /$$$$$$$$ /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$  /$$$$$$  /$$$$$$ 
|__  $$__//$$__  $$| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$| $$__  $$|_  $$_/ /$$__  $$
   | $$  | $$  \ $$| $$  \ $$| $$  \ $$| $$  \__/| $$  \ $$| $$  \ $$  | $$  | $$  \ $$
   | $$  | $$$$$$$$| $$$$$$$ | $$$$$$$$| $$      | $$$$$$$$| $$$$$$$/  | $$  | $$$$$$$$
   | $$  | $$__  $$| $$__  $$| $$__  $$| $$      | $$__  $$| $$__  $$  | $$  | $$__  $$
   | $$  | $$  | $$| $$  \ $$| $$  | $$| $$    $$| $$  | $$| $$  \ $$  | $$  | $$  | $$
   | $$  | $$  | $$| $$$$$$$/| $$  | $$|  $$$$$$/| $$  | $$| $$  | $$ /$$$$$$| $$  | $$
   |__/  |__/  |__/|_______/ |__/  |__/ \______/ |__/  |__/|__/  |__/|______/|__/  |__/
        """)
        print("1 - Produtos")
        print("2 - Stock")
        print("3 - Vendas")
        print("4 - Clientes")
        print("5 - Funcionários")
        print("0 - Sair")

        op = input("Opção: ")

        if op == "1":
            menu_produtos()
        elif op == "2":
            menu_stock()
        elif op == "3":
            menu_vendas()
        elif op == "4":
            menu_clientes()
        elif op == "5":
            menu_funcionarios()
        elif op == "0":
            print("A sair...")
            break
        else:
            print("Opção inválida!")


# EXECUTAR
menu_principal()


def listar_produtos():
    try:
        #Lista todos os produtos ativos na base de dados
        conn = conectar()
        cur = conn.cursor() # Ponte que permite executar comandos como o "SELECT; UPDATE ETC..."
        cur.execute("SELECT id, nome, categoria, preco, stock FROM produto WHERE ativo = 1")
        produtos = cur.fetchall()
        conn.close()

        print("\n--- LISTA DE PRODUTOS ---")
        if not produtos:
            print("Nenhum produto encontrado.")
            return

        for p in produtos:
            print(f"{p[0]} - {p[1]} | {p[2]} | {p[3]}€ | Stock: {p[4]}")

    except Exception as e:
        print("Erro ao listar produtos:", e)



def adicionar_produto():
    try:
        # Adiciona um novo produto à base de dados
        nome = input("Nome: ")
        categoria = input("Categoria: ")

        try:
            preco = float(input("Preço: "))
            stock = int(input("Stock inicial: "))
            fornecedor = int(input("ID Fornecedor: "))
        except ValueError:
            print("Erro: valores inválidos.")
            return

        conn = conectar()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO produto (nome, categoria, preco, stock, fornecedor_id)
            VALUES (?, ?, ?, ?, ?)
        """, (nome, categoria, preco, stock, fornecedor))
        conn.commit()
        conn.close()
        print("Produto adicionado com sucesso!")

    except Exception as e:
        print("Erro ao adicionar produto:", e)


def procurar_produto():
    try:
        # Procura produtos pelo nome ou parte do nome
        texto = input("Nome ou parte do nome: ")

        conn = conectar()
        cur = conn.cursor()
        cur.execute("SELECT id, nome, preco, stock FROM produto WHERE nome LIKE ?", ("%" + texto + "%",))
        produtos = cur.fetchall()
        conn.close()

        print("\n--- RESULTADOS ---")
        if not produtos:
            print("Nenhum produto encontrado.")
            return

        for p in produtos:
            print(f"{p[0]} - {p[1]} | {p[2]}€ | Stock: {p[3]}")

    except Exception as e:
        print("Erro ao procurar produto:", e)



def alterar_preco():
    try:
        #altera o preco de um produto especifiico
        try:
            pid = int(input("ID do produto: "))
            novo_preco = float(input("Novo preço: "))
        except ValueError:
            print("Erro: valores inválidos.")
            return

        conn = conectar()
        cur = conn.cursor()
        cur.execute("UPDATE produto SET preco = ? WHERE id = ?", (novo_preco, pid))
        conn.commit()
        conn.close()
        print("Preço atualizado!")

    except Exception as e:
        print("Erro ao alterar preço:", e)



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
    try:
        #Aumenta ou diminui o stock de um produto.
        try:
            pid = int(input("ID Produto: "))
            qtd = int(input("Quantidade: "))
        except ValueError:
            print("Erro: valores inválidos.")
            return

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

    except Exception as e:
        print("Erro ao alterar stock:", e)


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

