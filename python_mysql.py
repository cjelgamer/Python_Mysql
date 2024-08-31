import tkinter as tk

#importar los modulos restantes de tkinter

from tkinter import *

from tkinter import ttk
from tkinter import messagebox

from peliculas import *
from Conexion import *

class FormularioPeliculas:
 
 global base
 base=None

 global textBoxId
 textBoxId=None

 global texBoxNombre
 texBoxNombre=None

 global texBoxDuracion
 texBoxDuracion=None

 global combo
 combo=None

 global groupBox 
 groupBox=None

 global tree 
 tree=None


def Formulario():
  global texBoxId
  global texBoxNombre
  global texBoxDuracion
  global combo
  global base
  global groupBox 
  global tree 


  try:      
        base = Tk()
        base.geometry("1200x300")
        base.title("Formulario Peliculas")
        
        
        #Primer group box para insertar datos   
        #panel que controla paneles mas pequeños 
        groupBox = LabelFrame(base,text = "Datos de las Peliculas", padx=5,pady=5)
        groupBox.grid(row=0,column=0,padx=10,pady=10)
        
        labelId=Label(groupBox,text="ID",width=13,font=("arial",12)).grid(row=0,column=0)
        texBoxId = Entry(groupBox)
        texBoxId.grid(row=0,column=1)
     
        labelNombre=Label(groupBox,text="Nombre :",width=13,font=("arial",12)).grid(row=1,column=0)
        texBoxNombre = Entry(groupBox)
        texBoxNombre.grid(row=1,column=1)   
            
            
        labelDuracion=Label(groupBox,text="Duracion :",width=13,font=("arial",12)).grid(row=2,column=0)
        texBoxDuracion = Entry(groupBox)
        texBoxDuracion.grid(row=2,column=1)   

            
        labelGenero=Label(groupBox,text="Genero :",width=13,font=("arial",12)).grid(row=3,column=0)
        seleccionGenero = tk.StringVar()
        combo= ttk.Combobox(groupBox,values=["Acción", "Aventura", "Comedia", "Drama", "Ciencia Ficción", 
    "Fantasía", "Terror", "Suspense (Thriller)", "Romance", 
    "Documental", "Musical", "Animación", "Western", 
    "Histórico", "Noir", "Deportes", "Bélico"],textvariable=seleccionGenero)
        combo.grid(row=3,column=1)
        seleccionGenero.set("Acción")
         
        Button(groupBox,text="Insertar",width=10,command=guardarRegistros).grid(row=4,column=0)
        Button(groupBox,text="Editar",width=10,command=modificarRegistros).grid(row=4,column=1)
        Button(groupBox,text="Eliminar",width=10,command=eliminarRegistros).grid(row=4,column=2)
        
        
        #Segundo group box para mostrar datos
        
        groupBox = LabelFrame(base,text="Lista de Peliculas",padx=5,pady=5)
        groupBox.grid(row=0,column=1,padx=5,pady=5)
        #Crear un Treeview
        
        #configurar las columnas
        tree = ttk.Treeview(groupBox,columns=("ID","Nombre","Duracion","Genero"),show='headings',height=5,)
        tree.column("# 1",anchor=CENTER)
        tree.heading("# 1",text="ID")
            
        tree.column("# 2",anchor=CENTER)
        tree.heading("# 2",text="Nombre")
            
        tree.column("# 3",anchor=CENTER)
        tree.heading("# 3",text="Duracion")    
        
        tree.column("# 4",anchor=CENTER)
        tree.heading("# 4",text="Genero")   

        for row in CPeliculas.mostrarPeliculas():
             tree.insert("","end",values=row) 


        #selecciona run registro de la tabla

        tree.bind("<<TreeviewSelect>>",seleccionarRegistro)
            
        tree.pack()
        
            
        base.mainloop()
            
            
  except ValueError as error:
            print("Error al mostrar la interfaz, el error es: {}".format(error))
                
def guardarRegistros():
      global texBoxNombre,texBoxDuracion,combo,groupBox

      try:
           if texBoxNombre is None or texBoxDuracion is None or combo is None:
                print("Los widgedts de la sinterfaces no estan inicializados")
                return
           nombre = texBoxNombre.get()
           duracion = texBoxDuracion.get()
           genero = combo.get()

           CPeliculas.ingresarpeliculas(nombre,duracion,genero)
           messagebox.showinfo("Información, los mensajes fueron guardados")

           actualizarTreeView()

           texBoxNombre.delete(0,END)
           texBoxDuracion.delete(0,END)
      except ValueError as error:
           print("Error al ingresar los datos {}".format(error))

def actualizarTreeView():
     global tree
     
     try:
          #eliminamos el contenido, mas no los id
          tree.delete(*tree.get_children())
          datos = CPeliculas.mostrarPeliculas()
          for row in CPeliculas.mostrarPeliculas():
             tree.insert("","end",values=row)
     except ValueError as error:
          print("Error al actualizar tabla {}".format(error))

def seleccionarRegistro(event):
     try:
          itemselec=tree.focus()

          if itemselec:#obtenemos valores
               valor = tree.item(itemselec)['values']
               texBoxId.delete(0,END)
               texBoxId.insert(0,valor[0])
               texBoxNombre.delete(0,END)
               texBoxNombre.insert(0,valor[1])
               texBoxDuracion.delete(0,END)
               texBoxDuracion.insert(0,valor[2])
               combo.set(valor[3])
     except ValueError as error:
          print("Error al editar registro{}".format(error))

def modificarRegistros():
      global texBoxId,texBoxNombre,texBoxDuracion,combo,groupBox

      try:
           if texBoxId is None or texBoxNombre is None or texBoxDuracion is None or combo is None:
                print("Los widgedts de la sinterfaces no estan inicializados")
                return
           idpelicula=texBoxId.get()
           nombre = texBoxNombre.get()
           duracion = texBoxDuracion.get()
           genero = combo.get()

           CPeliculas.modificarpeliculas(idpelicula,nombre,duracion,genero)
           messagebox.showinfo("Información, los datos fueron actualizados")

           actualizarTreeView()

           texBoxId.delete(0,END)
           texBoxNombre.delete(0,END)
           texBoxDuracion.delete(0,END)
      except ValueError as error:
           print("Error al editar los datos {}".format(error))

def eliminarRegistros():
      global texBoxId,texBoxDuracion,texBoxNombre

      try:
           if texBoxId is None:
                print("Los widgedts de la sinterfaces no estan inicializados")
                return
           idpelicula=texBoxId.get()


           CPeliculas.eliminarpeliculas((idpelicula,))
           messagebox.showinfo("Información, los datos fueron eliminados")

           actualizarTreeView()

           texBoxId.delete(0,END)
           texBoxNombre.delete(0,END)
           texBoxDuracion.delete(0,END)
      except ValueError as error:
           print("Error al ingresar los datos {}".format(error))


Formulario()          