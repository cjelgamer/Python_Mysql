from Conexion import *

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