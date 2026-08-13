from database import conectar


def listar_libros():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM libros")
    libros = cursor.fetchall()

    cursor.close()
    conexion.close()

    return libros


def agregar_libro(id, titulo, autor, anio, genero, disponible):
    conexion = conectar()
    cursor = conexion.cursor()

    sql = """
        INSERT INTO libros (id, titulo, autor, anio, genero, disponible)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    valores = (id, titulo, autor, anio, genero, disponible)

    cursor.execute(sql, valores)

    conexion.commit()

    cursor.close()
    conexion.close()


def actualizar_libro(id, titulo, autor, anio, genero, disponible):
    conexion = conectar()
    cursor = conexion.cursor()

    sql = """
        UPDATE libros
        SET titulo = %s,
            autor = %s,
            anio = %s,
            genero = %s,
            disponible = %s
        WHERE id = %s
    """

    valores = (titulo, autor, anio, genero, disponible, id)

    cursor.execute(sql, valores)

    conexion.commit()

    cursor.close()
    conexion.close()




print("Libro agregado correctamente")


# Actualizar libro
actualizar_libro(
    3,
    "EL PRINCIPITO",
    "ANTOINE DE SAINT-EXUPÉRY",
    1943,
    "NOVELA",
    True
)

print("Libro actualizado correctamente")


# Mostrar libros
libros = listar_libros()

for libro in libros:
    print(libro)


def eliminar_libro(id):
    conexion = conectar()
    cursor = conexion.cursor()

    sql = "DELETE FROM libros WHERE id = %s"

    cursor.execute(sql, (id,))

    conexion.commit()

    cursor.close()
    conexion.close()


eliminar_libro(3)

print("Libro eliminado correctamente")


while True:
    print("\n================================")
    print("          BIBLIOTECA")
    print("================================")
    print("1. Listar libros")
    print("2. Agregar libro")
    print("3. Actualizar libro")
    print("4. Eliminar libro")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        libros = listar_libros()

        for libro in libros:
            print(libro)

    elif opcion == "2":
        id = int(input("ID del libro: "))
        titulo = input("Título: ")
        autor = input("Autor: ")
        anio = int(input("Año: "))
        genero = input("Género: ")
        disponible = True

        agregar_libro(
            id,
            titulo,
            autor,
            anio,
            genero,
            disponible
        )

        print("✅ Libro agregado correctamente")

    elif opcion == "3":
        id = int(input("ID del libro que quieres actualizar: "))
        titulo = input("Nuevo título: ")
        autor = input("Nuevo autor: ")
        anio = int(input("Nuevo año: "))
        genero = input("Nuevo género: ")
        disponible = True

        actualizar_libro(
            id,
            titulo,
            autor,
            anio,
            genero,
            disponible
        )

        print("✅ Libro actualizado correctamente")

    elif opcion == "4":
        id = int(input("ID del libro que quieres eliminar: "))

        eliminar_libro(id)

        print("✅ Libro eliminado correctamente")

    elif opcion == "5":
        print("👋 Programa finalizado")
        break

    else:
        print("❌ Opción no válida")

