CREATE TABLE fornecedor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT,
    email TEXT,
    morada TEXT
);

CREATE TABLE produto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    categoria TEXT,
    preco REAL NOT NULL,
    stock INTEGER DEFAULT 0,
    fornecedor_id INTEGER,
    ativo BOOLEAN DEFAULT 1,
    FOREIGN KEY (fornecedor_id) REFERENCES fornecedor(id)
);

CREATE TABLE funcionario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role TEXT DEFAULT 'funcionario'
);

CREATE TABLE cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT,
    email TEXT
);