from Conexion import *
import re

class CPeliculas:

    def mostrarPeliculas():
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor=cone.cursor()
            cursor.execute("select * from pelicula;")
            miresultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miresultado

        except mysql.connector.Error as error:
            print("Error de mostrar datos {}".format(error))


    def ingresarpeliculas(nombre,duracion,genero):
        #nombre=CPeliculas.verificarpeliculas(nombre)
        #duracion=CPeliculas.verificarpeliculas(duracion)
        #genero=CPeliculas.verificarpeliculas(genero)

        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor=cone.cursor()
            sql="insert into pelicula values(null,%s,%s,%s);"
            valores=(nombre,duracion,genero)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Ingresado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))

    def modificarpeliculas(idpelicula,nombre,duracion,genero):
        #idpelicula=CPeliculas.verificarpeliculas(idpelicula)
        #nombre=CPeliculas.verificarpeliculas(nombre)
        #duracion=CPeliculas.verificarpeliculas(duracion)
        #genero=CPeliculas.verificarpeliculas(genero)

        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor=cone.cursor()
            sql="UPDATE pelicula SET pelicula.nombre=%s,pelicula.duracion=%s,pelicula.genero=%s where pelicula.id=%s;"
            valores=(nombre,duracion,genero,idpelicula)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro Actualizado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de actualizacion {}".format(error))

    def eliminarpeliculas(idpelicula):
        #idpelicula=CPeliculas.verificarpeliculas(idpelicula)

        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor=cone.cursor()
            sql="DELETE from pelicula WHERE pelicula.id=%s;"
            valores=(idpelicula)
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro eliminado")
            cone.close()

        except mysql.connector.Error as error:
            print("Error de eliminacion {}".format(error))

    def limpiarPeliculas(cadena):
        cadena= cadena.strip()  # Elimina espacios al inicio y al final
        cadena= cadena.replace("\\", "")
        cadena = re.sub(r"(?i)SELECT\s+.*?\s+FROM", "", cadena)
        cadena = re.sub(r"(?i)DELETE\s+FROM", "", cadena)
        cadena = re.sub(r"(?i)INSERT\s+INTO", "", cadena)
        cadena = re.sub(r"(?i)DROP\s+TABLE", "", cadena)
        cadena = re.sub(r"(?i)DROP\s+DATABASE", "", cadena)
        cadena = re.sub(r"(?i)TRUNCATE\s+TABLE", "", cadena)
        cadena = re.sub(r"(?i)SHOW\s+TABLES", "", cadena)
        cadena = re.sub(r"(?i)SHOW\s+DATABASES", "", cadena)
        cadena = re.sub(r"(?i)--", "", cadena)
        cadena = re.sub(r"[<>;']", "", cadena)  # Elimina caracteres peligrosos
        return cadena

    def verificarpeliculas(atrpelicula):

        limpio_atrpelicula = CPeliculas.limpiarPeliculas(atrpelicula)
        if  limpio_atrpelicula  == "":
            print("Comando malicioso")
            return None
        return atrpelicula
            


