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
        cadena= re.sub("<script>", "", cadena, flags=re.IGNORECASE)
        cadena= re.sub("</script>", "", cadena, flags=re.IGNORECASE)
        cadena= re.sub("<script type=", "", cadena, flags=re.IGNORECASE)
        cadena= re.sub("SELECT * FROM", "", cadena, flags=re.IGNORECASE)
        cadena= re.sub("DELETE FROM", "", cadena, flags=re.IGNORECASE)
        cadena= re.sub("INSERT INTO", "", cadena, flags=re.IGNORECASE)
        cadena= re.sub("DROP TABLE", "", cadena, flags=re.IGNORECASE)
        cadena= re.sub("DROP DATABASE", "", cadena, flags=re.IGNORECASE)
        cadena= re.sub("TRUNCATE TABLE", "", cadena, flags=re.IGNORECASE)
        cadena= re.sub("SHOW TABLES", "", cadena, flags=re.IGNORECASE)
        cadena= re.sub("SHOW DATABASES", "", cadena, flags=re.IGNORECASE)
        cadena= re.sub("--", "", cadena, flags=re.IGNORECASE)
        cadena= re.sub("^", "", cadena, flags=re.IGNORECASE)
        cadena= re.sub("<", "", cadena, flags=re.IGNORECASE)
        cadena= re.sub("[", "", cadena, flags=re.IGNORECASE)
        cadena= re.sub("]", "", cadena, flags=re.IGNORECASE)
        cadena= re.sub("==", "", cadena, flags=re.IGNORECASE)
        cadena= re.sub(";", "", cadena, flags=re.IGNORECASE)
        cadena= re.sub("::", "", cadena, flags=re.IGNORECASE)
        return cadena

    def verificarpeliculas(atrpelicula):

        limpio_atrpelicula = CPeliculas.limpiarPeliculas(atrpelicula)
        if  limpio_atrpelicula  == "":
            print("Comando malicioso")
            return None
        return atrpelicula
            


