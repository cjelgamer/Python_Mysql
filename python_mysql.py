import tkinter as tk

#importar los modulos restantes de tkinter

from tkinter import *

from tkinter import ttk
from tkinter import messagebox

class FormularioPeliculas:
    
 def Formulario():
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
         
        Button(groupBox,text="Insertar",width=10).grid(row=4,column=0)
        Button(groupBox,text="Editar",width=10).grid(row=4,column=1)
        Button(groupBox,text="Eliminar",width=10).grid(row=4,column=2)
        
        
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
            
        tree.pack()
        
        
        
            
        base.mainloop()
            
            
    except ValueError as error:
            print("Error al mostrar la interfaz, el error es: {}".format(error))
                
 Formulario()          