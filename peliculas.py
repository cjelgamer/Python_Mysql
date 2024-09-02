import mysql.connector
from mysql.connector import Error
from Conexion import CConexion
import re

class CPeliculas:

    @staticmethod
    def mostrarPeliculas():
        try:
            conn = CConexion.ConexionBaseDeDatos()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM pelicula;")
            miresultado = cursor.fetchall()
            conn.close()
            return miresultado
        except mysql.connector.Error as error:
            print("Error al mostrar datos: {}".format(error))
            return []

    @staticmethod
    def ingresarpeliculas(nombre, duracion, genero):
        nombre = CPeliculas.verificarpeliculas(nombre)
        duracion = CPeliculas.verificarpeliculas(duracion)
        genero = CPeliculas.verificarpeliculas(genero)

        if nombre is None or duracion is None or genero is None:
            print("Datos inválidos, no se puede insertar el registro.")
            return

        try:
            conn = CConexion.ConexionBaseDeDatos()
            cursor = conn.cursor()
            sql = "INSERT INTO pelicula (nombre, duracion, genero) VALUES (%s, %s, %s);"
            valores = (nombre, duracion, genero)
            cursor.execute(sql, valores)
            conn.commit()
            print(cursor.rowcount, "Registro insertado")
            conn.close()
        except mysql.connector.Error as error:
            print("Error al ingresar datos: {}".format(error))

    @staticmethod
    def modificarpeliculas(idpelicula, nombre, duracion, genero):
        idpelicula = CPeliculas.verificarpeliculas(idpelicula)
        nombre = CPeliculas.verificarpeliculas(nombre)
        duracion = CPeliculas.verificarpeliculas(duracion)
        genero = CPeliculas.verificarpeliculas(genero)

        if idpelicula is None or nombre is None or duracion is None or genero is None:
            print("Datos inválidos, no se puede actualizar el registro.")
            return

        try:
            conn = CConexion.ConexionBaseDeDatos()
            cursor = conn.cursor()
            sql = "UPDATE pelicula SET nombre = %s, duracion = %s, genero = %s WHERE id = %s;"
            valores = (nombre, duracion, genero, idpelicula)
            cursor.execute(sql, valores)
            conn.commit()
            print(cursor.rowcount, "Registro actualizado")
            conn.close()
        except mysql.connector.Error as error:
            print("Error al actualizar datos: {}".format(error))

    @staticmethod
    def eliminarpeliculas(idpelicula):
        idpelicula = CPeliculas.verificarpeliculas(idpelicula)

        if idpelicula is None:
            print("ID inválido, no se puede eliminar el registro.")
            return

        try:
            conn = CConexion.ConexionBaseDeDatos()
            cursor = conn.cursor()
            sql = "DELETE FROM pelicula WHERE id = %s;"
            cursor.execute(sql, (idpelicula,))
            conn.commit()
            print(cursor.rowcount, "Registro eliminado")
            conn.close()
        except mysql.connector.Error as error:
            print("Error al eliminar datos: {}".format(error))

    @staticmethod
    def limpiarPeliculas(cadena):
        cadena = cadena.strip()
        cadena = cadena.replace("\\", "")
        cadena = re.sub(r"(?i)SELECT\s+.*?\s+FROM", "", cadena)
        cadena = re.sub(r"(?i)DELETE\s+FROM", "", cadena)
        cadena = re.sub(r"(?i)INSERT\s+INTO", "", cadena)
        cadena = re.sub(r"(?i)DROP\s+TABLE", "", cadena)
        cadena = re.sub(r"(?i)DROP\s+DATABASE", "", cadena)
        cadena = re.sub(r"(?i)TRUNCATE\s+TABLE", "", cadena)
        cadena = re.sub(r"(?i)SHOW\s+TABLES", "", cadena)
        cadena = re.sub(r"(?i)SHOW\s+DATABASES", "", cadena)
        cadena = re.sub(r"(?i)--", "", cadena)
        cadena = re.sub(r"[<>;']", "", cadena)
        return cadena

    @staticmethod
    def verificarpeliculas(atrpelicula):
        limpio_atrpelicula = CPeliculas.limpiarPeliculas(atrpelicula)
        if limpio_atrpelicula == "":
            print("Comando malicioso detectado")
            return None
        return atrpelicula
