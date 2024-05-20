import sqlite3, datetime
# Conectarse a la base de datos
conn = sqlite3.connect("database.db")

# Crear una tabla de entradas
conn.execute("CREATE TABLE IF NOT EXISTS entradas (id INTEGER PRIMARY KEY, concepto TEXT, cantidad REAL, fecha DATETIME)")

# Agregar una entrada a la tabla
def entradas(concepto, cantidad):
    conn.execute("""
    INSERT INTO entradas (concepto, cantidad, fecha)
    VALUES (?, ?, ?)
    """, (concepto, cantidad, datetime.datetime.now()))
    # Guardar los cambios
    conn.commit()

    # Cerrar la conexión
    conn.close()

# Agregar las salidas a la tabla
def salidas(concepto, cantidad):
    conn.execute("""INSERT INTO salidas (concepto,cantidad,fecha)
                 VALUES (?,?,?)
                 """,(concepto,cantidad,datetime.datetime.now()))
    conn.commit()
    conn.close()
    
def inicializacion_registros():
    cursor.execute("""CREATE TABLE MOV_ENTRADAS
                   (    ID INTEGER PRIMARY KEY,
                        CANTIDAD NUMERIC,
                        CONCEPTO TEXT  NOT NULL,
                        FECHA DATE); """)