# 🧾 Sistema de Consola para uma Tabacaria

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)]()
[![Status](https://img.shields.io/badge/Status-Ativo-success.svg)]()
[![License](https://img.shields.io/badge/License-Educacional-lightgrey.svg)]()

Este repositório contém um sistema de consola desenvolvido para a disciplina  
**Ambientes de Desenvolvimento Colaborativo**. O projeto simula operações básicas de uma tabacaria com integração a uma base de dados SQL.

---

## 📘 Sobre o Projeto
O sistema permite gerir itens, vendas e consultas da tabacaria através de um menu em consola.  
Toda a documentação detalhada pode ser encontrada na **Wiki oficial do projeto**.

---

## ⚙️ Funcionalidades
- Gestão de produtos
- Pesquisa e filtros
- Carrinho de compras
- Sistema de vendas
- Relatórios simples
- Integração com base de dados SQL

---

## 🛠️ Tecnologias Utilizadas
- Python
- MySQL / HeidiSQL
- Git & GitHub
- Markdown

---

## 🚀 Como Usar

### 1️⃣ Clonar o Repositório
```git clone https://github.com/74joaomvm/ambientes.git```


### 2️⃣ Configurar a Base de Dados
1. Abra o arquivo main.py.
2. Vá até a linha 14 e altere o nome da base de dados conforme a sua
3. Abra o seu gestor de base de dados (ex.: HeidiSQL) e importe:
```database/database.sql```


### 3️⃣ Instalar Dependências
1. Certifique-se de ter Python 3.10+ instalado.
2. Abra a sua linha de comando e execute: ```pip install -r requirements.txt```


### 4️⃣ Executar o Sistema
Dentro da linha de comandos dentro do seu Diretório execute: ```python main.py``` ou ```python3 main.py``` consoante a sua versão python.


### 🎉 Pronto! 
O sistema inicia imediatamente no terminal.

--- 

## 🖥️ Screenshot do Repositório
*(Exemplo da visualização)*

![Execução do programa em cmd Windows](printscreen/cmd.png)


--- 

## 🗃️ Estrutura do Projeto
```
📁 ambientes
├── 📁 database
│ └── database.sql
├── 📁 printscreen
│ └── cmd.png
├── README.md
└── main.py
```

--- 

## ❓ FAQ

### ➡ Tenho erro de ligação ao MySQL?
Verifique se o usuário, senha e nome da base de dados no main.py estão corretos.

### ➡ É obrigatório usar HeidiSQL?
Não. Pode usar qualquer gestor como Workbench, Beekeeper, DBeaver, etc.

### ➡ O sistema tem interface gráfica?
Nesta versão ainda não. É totalmente em consola. Fique atento ao repositório que em breve haverá uma versão de aplicação web.


--- 

## 👨‍💻 Colaboradores

- [74joaomvm](https://github.com/74joaomvm)
- [DanielNascimentoo](https://github.com/DanielNascimentoo)
- [zezima000](https://github.com/zezima000)
- [Migueldc76](https://github.com/Migueldc76)

---

## 🗺️ Roadmap (Futuro do Projeto)
- [ ] Adicionar sistema de login
- [ ] Criar relatórios em PDF
- [ ] Melhorar gestão de stock
- [ ] Criar testes automáticos



---

## 📄 Licença

Este projeto é de uso exclusivamente educacional. Créditos aos autores e colaboradores.


---

## ⭐ Contribua!

**Gostou?** 
Dê uma ⭐ no repositório para apoiar o projeto!