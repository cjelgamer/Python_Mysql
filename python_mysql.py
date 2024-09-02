import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from peliculas import *
from Conexion import *

class FormularioPeliculas:

    global base
    base = None

    global texBoxId
    texBoxId = None

    global texBoxNombre
    texBoxNombre = None

    global texBoxDuracion
    texBoxDuracion = None

    global combo
    combo = None

    global groupBox
    groupBox = None

    global tree
    tree = None

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
        base.geometry("1200x400")
        base.title("Formulario Películas")
        base.configure(bg="#FFF")  # Fondo de la ventana principal

        # Estilos personalizados
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 12), background="#2C3E50", foreground="white")
        style.configure("TEntry", font=("Arial", 12))
        style.configure("TCombobox", font=("Arial", 12))

        # Estilo para los botones
        style.configure("TButton", font=("Arial", 10, "bold"), foreground="black", background="#D3D3D3", padding=6)
        style.map("TButton",
                  foreground=[('active', 'black'), ('pressed', 'black')],
                  background=[('active', '#B0B0B0'), ('pressed', '#A0A0A0')])

        # Group box para insertar datos
        groupBox = LabelFrame(base, text="Datos de las Películas", padx=5, pady=5, bg="#34495E", fg="white", font=("Arial", 14, "bold"))
        groupBox.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        labelId = ttk.Label(groupBox, text="ID")
        labelId.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        texBoxId = ttk.Entry(groupBox)
        texBoxId.grid(row=0, column=1, padx=5, pady=5)

        labelNombre = ttk.Label(groupBox, text="Nombre")
        labelNombre.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        texBoxNombre = ttk.Entry(groupBox)
        texBoxNombre.grid(row=1, column=1, padx=5, pady=5)

        labelDuracion = ttk.Label(groupBox, text="Duración")
        labelDuracion.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        texBoxDuracion = ttk.Entry(groupBox)
        texBoxDuracion.grid(row=2, column=1, padx=5, pady=5)

        labelGenero = ttk.Label(groupBox, text="Género")
        labelGenero.grid(row=3, column=0, sticky=W, padx=5, pady=5)
        seleccionGenero = tk.StringVar()
        combo = ttk.Combobox(groupBox, values=[
            "Acción", "Aventura", "Comedia", "Drama", "Ciencia Ficción", 
            "Fantasía", "Terror", "Suspense (Thriller)", "Romance", 
            "Documental", "Musical", "Animación", "Western", 
            "Histórico", "Noir", "Deportes", "Bélico"], 
            textvariable=seleccionGenero, state="readonly")
        combo.grid(row=3, column=1, padx=5, pady=5)
        seleccionGenero.set("Acción")

        buttonInsertar = ttk.Button(groupBox, text="Insertar", command=guardarRegistros, style="TButton")
        buttonInsertar.grid(row=4, column=0, padx=5, pady=10)

        buttonEditar = ttk.Button(groupBox, text="Editar", command=modificarRegistros, style="TButton")
        buttonEditar.grid(row=4, column=1, padx=5, pady=10)

        buttonEliminar = ttk.Button(groupBox, text="Eliminar", command=eliminarRegistros, style="TButton")
        buttonEliminar.grid(row=4, column=2, padx=5, pady=10)

        # Segundo group box para mostrar datos
        groupBox = LabelFrame(base, text="Lista de Películas", padx=5, pady=5, bg="#34495E", fg="white", font=("Arial", 14, "bold"))
        groupBox.grid(row=0, column=1, padx=10, pady=10, sticky="nw")

        # Crear un Treeview
        tree = ttk.Treeview(groupBox, columns=("ID", "Nombre", "Duración", "Género"), show='headings', height=10)
        tree.column("#1", anchor=CENTER, width=50)
        tree.heading("#1", text="ID")
        tree.column("#2", anchor=CENTER, width=200)
        tree.heading("#2", text="Nombre")
        tree.column("#3", anchor=CENTER, width=100)
        tree.heading("#3", text="Duración")
        tree.column("#4", anchor=CENTER, width=150)
        tree.heading("#4", text="Género")

        for row in CPeliculas.mostrarPeliculas():
            tree.insert("", "end", values=row)

        tree.bind("<<TreeviewSelect>>", seleccionarRegistro)
        tree.pack(padx=5, pady=5)

        # Cargar la imagen
        imagen = Image.open("cineplanet.png")
        imagen = imagen.resize((190, 150), Image.Resampling.LANCZOS)  # Cambia el tamaño de la imagen si es necesario
        imagen_tk = ImageTk.PhotoImage(imagen)

        # Crear un Label para mostrar la imagen
        label_imagen = Label(base, image=imagen_tk, bg="#fff")
        label_imagen.image = imagen_tk  # Guardar una referencia de la imagen para evitar que sea recolectada por el garbage collector
        label_imagen.grid(row=0, column=2, padx=10, pady=10, sticky="nw")

        base.mainloop()

    except ValueError as error:
        print("Error al mostrar la interfaz, el error es: {}".format(error))

def guardarRegistros():
    global texBoxNombre, texBoxDuracion, combo, groupBox

    try:
        if texBoxNombre is None or texBoxDuracion is None or combo is None:
            print("Los widgets de la interfaz no están inicializados")
            return
        nombre = texBoxNombre.get()
        duracion = texBoxDuracion.get()
        genero = combo.get()

        CPeliculas.ingresarpeliculas(nombre, duracion, genero)
        messagebox.showinfo("Información", "Los datos fueron guardados")

        actualizarTreeView()

        texBoxNombre.delete(0, END)
        texBoxDuracion.delete(0, END)
    except ValueError as error:
        print("Error al ingresar los datos: {}".format(error))

def actualizarTreeView():
    global tree

    try:
        tree.delete(*tree.get_children())
        datos = CPeliculas.mostrarPeliculas()
        for row in datos:
            tree.insert("", "end", values=row)
    except ValueError as error:
        print("Error al actualizar la tabla: {}".format(error))

def seleccionarRegistro(event):
    global texBoxId, texBoxNombre, texBoxDuracion, combo, tree

    try:
        itemselec = tree.focus()

        if itemselec:
            valor = tree.item(itemselec)['values']
            texBoxId.delete(0, END)
            texBoxId.insert(0, valor[0])
            texBoxNombre.delete(0, END)
            texBoxNombre.insert(0, valor[1])
            texBoxDuracion.delete(0, END)
            texBoxDuracion.insert(0, valor[2])
            combo.set(valor[3])
    except ValueError as error:
        print("Error al seleccionar registro: {}".format(error))

def modificarRegistros():
    global texBoxId, texBoxNombre, texBoxDuracion, combo

    try:
        if texBoxId is None or texBoxNombre is None or texBoxDuracion is None or combo is None:
            print("Los widgets de la interfaz no están inicializados")
            return
        idpelicula = texBoxId.get()
        nombre = texBoxNombre.get()
        duracion = texBoxDuracion.get()
        genero = combo.get()

        CPeliculas.modificarpeliculas(idpelicula, nombre, duracion, genero)
        messagebox.showinfo("Información", "Los datos fueron actualizados")

        actualizarTreeView()

        texBoxId.delete(0, END)
        texBoxNombre.delete(0, END)
        texBoxDuracion.delete(0, END)
    except ValueError as error:
        print("Error al editar los datos: {}".format(error))

def eliminarRegistros():
    global texBoxId, texBoxDuracion, texBoxNombre

    try:
        if texBoxId is None:
            print("Los widgets de la interfaz no están inicializados")
            return
        idpelicula = texBoxId.get()

        CPeliculas.eliminarpeliculas((idpelicula,))
        messagebox.showinfo("Información", "Los datos fueron eliminados")

        actualizarTreeView()

        texBoxId.delete(0, END)
        texBoxNombre.delete(0, END)
        texBoxDuracion.delete(0, END)
    except ValueError as error:
        print("Error al eliminar los datos: {}".format(error))

Formulario()
