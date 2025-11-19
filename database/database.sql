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


CREATE TABLE venda (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATETIME DEFAULT CURRENT_TIMESTAMP,
    total REAL NOT NULL,
    funcionario_id INTEGER,
    cliente_id INTEGER,
    FOREIGN KEY (funcionario_id) REFERENCES funcionario(id),
    FOREIGN KEY (cliente_id) REFERENCES cliente(id)
);

REATE TABLE item_venda (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    venda_id INTEGER NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    preco_unitario REAL NOT NULL,
    subtotal REAL NOT NULL,
    FOREIGN KEY (venda_id) REFERENCES venda(id),
    FOREIGN KEY (produto_id) REFERENCES produto(id)
);


INSERT INTO fornecedor (nome, telefone, email, morada) VALUES
('Tabacos Lisboa SA', '213456789', 'contacto@tabacoslisboa.pt', 'Rua da Fábrica 12, Lisboa'),
('Distribuidora FumoNobre', '222345678', 'info@fumonobre.pt', 'Av. Central 45, Porto'),
('Silver Tobacco Imports', '934567890', 'silver@tobaccoimports.com', 'Rua do Mercado 81, Faro');