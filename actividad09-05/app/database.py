import sqlite3

# Función para obtener la conexión a la base de datos
def get_db_connection():
    conn = sqlite3.connect('app/database/escuela.db')
    conn.row_factory = sqlite3.Row  # Permite acceder a las columnas por nombre
    return conn

# Función para crear las tablas en la base de datos
def crear_tablas():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Crear la tabla de estudiantes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS estudiantes (
            id_estudiante INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL
        )
    ''')

    # Crear la tabla de cursos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cursos (
            id_curso INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        )
    ''')

    # Crear la tabla de notas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notas (
            id_nota INTEGER PRIMARY KEY AUTOINCREMENT,
            id_estudiante INTEGER,
            id_curso INTEGER,
            nota REAL,
            FOREIGN KEY(id_estudiante) REFERENCES estudiantes(id_estudiante),
            FOREIGN KEY(id_curso) REFERENCES cursos(id_curso)
        )
    ''')

    conn.commit()
    conn.close()

# Función para insertar datos de ejemplo en las tablas
def insertar_datos_prueba():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Insertar estudiantes
    cursor.execute("INSERT INTO estudiantes (nombre, apellido) VALUES ('Juan', 'Pérez')")
    cursor.execute("INSERT INTO estudiantes (nombre, apellido) VALUES ('Ana', 'Gómez')")

    # Insertar cursos
    cursor.execute("INSERT INTO cursos (nombre) VALUES ('Matemáticas')")
    cursor.execute("INSERT INTO cursos (nombre) VALUES ('Física')")

    # Insertar notas
    cursor.execute("INSERT INTO notas (id_estudiante, id_curso, nota) VALUES (1, 1, 9.5)")  # Juan en Matemáticas
    cursor.execute("INSERT INTO notas (id_estudiante, id_curso, nota) VALUES (1, 2, 7.0)")  # Juan en Física
    cursor.execute("INSERT INTO notas (id_estudiante, id_curso, nota) VALUES (2, 1, 8.0)")  # Ana en Matemáticas
    cursor.execute("INSERT INTO notas (id_estudiante, id_curso, nota) VALUES (2, 2, 9.0)")  # Ana en Física

    conn.commit()
    conn.close()

# Crear las tablas y insertar datos de prueba
crear_tablas()
insertar_datos_prueba()

import sqlite3

# Función para obtener las notas de un estudiante específico
def obtener_notas_estudiante(id_estudiante):
    conn = sqlite3.connect('app/database/escuela.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT estudiantes.nombre, estudiantes.apellido, cursos.nombre AS curso, notas.nota
        FROM notas
        JOIN estudiantes ON estudiantes.id_estudiante = notas.id_estudiante
        JOIN cursos ON cursos.id_curso = notas.id_curso
        WHERE estudiantes.id_estudiante = ?
    ''', (id_estudiante,))
    notas = cursor.fetchall()
    conn.close()
    return notas

# Función para obtener las notas por curso
def obtener_notas_por_curso(id_curso):
    conn = sqlite3.connect('app/database/escuela.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT estudiantes.nombre, estudiantes.apellido, cursos.nombre AS curso, notas.nota
        FROM notas
        JOIN estudiantes ON estudiantes.id_estudiante = notas.id_estudiante
        JOIN cursos ON cursos.id_curso = notas.id_curso
        WHERE cursos.id_curso = ?
    ''', (id_curso,))
    notas = cursor.fetchall()
    conn.close()
    return notas

