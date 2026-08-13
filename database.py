
import mysql.connector

def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="xkevkx2007$",
        database="universidad"
    )

    return conexion

