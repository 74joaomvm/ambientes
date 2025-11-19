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
