
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import conectar

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Libro(BaseModel):
    titulo: str
    autor: str
    anio: int
    genero: str
    disponible: bool

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando correctamente"}


@app.get("/libros")
def listar_libros():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM libros")
    libros = cursor.fetchall()

    cursor.close()
    conexion.close()

    return libros


@app.post("/libros")


def agregar_libro(libro: Libro):
    conexion = conectar()
    cursor = conexion.cursor()

    sql = """
        INSERT INTO libros
        (titulo, autor, anio, genero, disponible)
        VALUES (%s, %s, %s, %s, %s)
    """

    valores = (
        libro.titulo,
        libro.autor,
        libro.anio,
        libro.genero,
        libro.disponible
    )

    cursor.execute(sql, valores)

    conexion.commit()

    id_generado = cursor.lastrowid

    cursor.close()
    conexion.close()

    return {
        "mensaje": "Libro agregado correctamente",
        "id": id_generado,
        "libro": libro
    }



@app.get("/libros/{id}")
def obtener_libro(id: int):
    conexion = conectar()
    cursor = conexion.cursor()

    sql = "SELECT * FROM libros WHERE id = %s"

    cursor.execute(sql, (id,))

    libro = cursor.fetchone()

    cursor.close()
    conexion.close()

    if libro is None:
        raise HTTPException(
            status_code=404,
            detail="Libro no encontrado"
        )

    return {
        "id": libro[0],
        "titulo": libro[1],
        "autor": libro[2],
        "anio": libro[3],
        "genero": libro[4],
        "disponible": bool(libro[5])
    }

@app.put("/libros/{id}")
def actualizar_libro(id: int, libro: Libro):
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

    valores = (
        libro.titulo,
        libro.autor,
        libro.anio,
        libro.genero,
        libro.disponible,
        id
    )

    cursor.execute(sql, valores)

    if cursor.rowcount == 0:
        cursor.close()
        conexion.close()

        raise HTTPException(
            status_code=404,
            detail="Libro no encontrado"
        )

    conexion.commit()

    cursor.close()
    conexion.close()

    return {
        "mensaje": "Libro actualizado correctamente",
        "id": id
    }
    
@app.delete("/libros/{id}")
def eliminar_libro(id: int):
    conexion = conectar()
    cursor = conexion.cursor()

    sql = "DELETE FROM libros WHERE id = %s"

    cursor.execute(sql, (id,))

    if cursor.rowcount == 0:
        cursor.close()
        conexion.close()

        raise HTTPException(
            status_code=404,
            detail="Libro no encontrado"
        )

    conexion.commit()

    cursor.close()
    conexion.close()

    return {
        "mensaje": "Libro eliminado correctamente",
        "id": id
    }
    
@app.get("/buscar")
def buscar_libros(titulo: str):

    conexion = conectar()
    cursor = conexion.cursor()

    sql = """
        SELECT * FROM libros
        WHERE titulo LIKE %s
    """

    valor = f"%{titulo}%"

    cursor.execute(sql, (valor,))

    libros = cursor.fetchall()

    cursor.close()
    conexion.close()

    return libros