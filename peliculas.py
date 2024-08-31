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

    def modificarpeliculas(idpelicula,nombre,duracion,genero):

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