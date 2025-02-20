import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('clientes.db')

# Crear un cursor
c = conn.cursor()

# Crear la tabla de clientes
c.execute('''CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY,
                nombre TEXT,
                apellido1 TEXT,
                apellido2 TEXT,
                edad INTEGER,
                correo TEXT,
                telefono TEXT
            )''')

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

