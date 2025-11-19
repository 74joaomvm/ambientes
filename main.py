import mysql.connector
from datetime import datetime



# ------------------------------------
# CONEXÃO COM MYSQL
# ------------------------------------
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",        # coloca o teu utilizador
        password="",        # coloca a tua password
        database="git"      # base de dados que aparece no HeidiSQL
    )
