import sqlite3

# 1. Conectar 
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# 2. Crear tablas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS images (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT NOT NULL,
        width INTEGER,
        height INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS labels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        image_id INTEGER,
        class_id INTEGER,
        x_center REAL,
        y_center REAL,
        width REAL,
        height REAL,
        FOREIGN KEY (image_id) REFERENCES images(id)
    )
''')

# 3. Guardar cambios y cerrar 
conn.commit()