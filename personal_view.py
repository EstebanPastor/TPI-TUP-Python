from tkinter import ttk
from tkinter import *
from models.Personal import Personal

# Iniciando Listas
personal_l = []

# Creando Objetos Iniciales
personal = Personal("1", "Carolina Lopez", "32182211",
                    "Toay 6262", "38333213", "Limpieza")
personal.crear_legajo()
personal_l.append(personal)


# Ventana Principal
def personalView(root):
    personal = Toplevel(root)
    personal.title("Modulo Personal")
    personal.geometry("800x600")

    # Marco
    marco = LabelFrame(personal, text="Listado del Personal")
    marco.place(x=20, y=20, width=750, height=550)

    # Tabla
    tablePersonal = ttk.Treeview(marco, height=20)
    tablePersonal.grid(column=1, row=1, columnspan=4, padx=10, pady=10)
    tablePersonal["columns"] = (
        "Legajo", "Nombre", "DNI", "Dirección", "Telefono", "Tarea")
    tablePersonal.column("#0", width=20, anchor=CENTER)
    tablePersonal.column("Legajo", width=100, anchor=CENTER)
    tablePersonal.column("Nombre", width=200, anchor=CENTER)
    tablePersonal.column("DNI", width=100, anchor=CENTER)
    tablePersonal.column("Dirección", width=100, anchor=CENTER)
    tablePersonal.column("Telefono", width=100, anchor=CENTER)
    tablePersonal.column("Tarea", width=100, anchor=CENTER)
    tablePersonal.heading("#0", text="#", anchor=CENTER)
    tablePersonal.heading("Legajo", text="Legajo", anchor=CENTER)
    tablePersonal.heading("Nombre", text="Nombre", anchor=CENTER)
    tablePersonal.heading("DNI", text="DNI", anchor=CENTER)
    tablePersonal.heading("Dirección", text="Dirección", anchor=CENTER)
    tablePersonal.heading("Telefono", text="Telefono", anchor=CENTER)
    tablePersonal.heading("Tarea", text="Tarea", anchor=CENTER)

    # Botones
    btnEliminar = Button(marco, text="Eliminar", width=20,
                         command=lambda: eliminarPersonal(tablePersonal))
    btnEliminar.grid(column=1, row=3, padx=10, pady=10)
    btnAgregar = Button(marco, text="Agregar", width=20,
                        command=lambda: agregarPersonalView(root, tablePersonal))
    btnAgregar.grid(column=3, row=3, padx=10, pady=10)

    cargarTabla(tablePersonal)


# Funciones
def cargarTabla(tablePersonal):
    rows = tablePersonal.get_children()
    for row in rows:
        tablePersonal.delete(row)

    for i, perso in enumerate(personal_l, start=1):
        id = i
        tablePersonal.insert("", END, id, text=id, values=(perso.legajo, perso.get_apeynom(
        ), perso.get_dni(), perso.get_direccion(), perso.get_telefono(), perso.get_tarea()))


def agregarPersonalView(root, tablePersonal):
    addPersonal = Toplevel(root)
    addPersonal.title("Agregar Personal")
    addPersonal.geometry("400x300")

    # Vars
    nombre = StringVar()
    dni = StringVar()
    direccion = StringVar()
    telefono = StringVar()
    tarea = StringVar()

    # Marco
    marco = LabelFrame(addPersonal, text="Formulario Agregar Personal")
    marco.place(x=10, y=10, width=350, height=280)

    # Entrys y labels
    lblnombre = Label(marco, text="Nombre: ").grid(column=0, row=0, padx=10, pady=10)
    txtnombre = Entry(marco, textvariable=nombre, width=30)
    txtnombre.grid(column=1, row=0, padx=10, pady=10)
    
    lbldni = Label(marco, text="DNI: ").grid(column=0, row=1, padx=10, pady=10)
    txtdni = Entry(marco, textvariable=dni, width=30)
    txtdni.grid(column=1, row=1, padx=10, pady=10)
    
    lbldireccion = Label(marco, text="Dirección: ").grid(column=0, row=2, padx=10, pady=10)
    txtdireccion = Entry(marco, textvariable=direccion, width=30)
    txtdireccion.grid(column=1, row=2, padx=10, pady=10)
    
    lbltelefono = Label(marco, text="Teléfono: ").grid(column=0, row=3, padx=10, pady=10)
    txtelefono = Entry(marco, textvariable=telefono, width=30)
    txtelefono.grid(column=1, row=3, padx=10, pady=10)
    
    lbltare = Label(marco, text="Tarea que realiza: ").grid(column=0, row=4, padx=10, pady=10)
    txtarea = Entry(marco, textvariable=tarea, width=30)
    txtarea.grid(column=1, row=4, padx=10, pady=10)
    
    # Botones
    btnConfirmar = Button(marco, text="Aceptar", width=10,
                         command=lambda: agregarPersonal())
    btnConfirmar.grid(column=0, row=5, padx=10, pady=10)
    
    btnCancelar = Button(marco, text="Cancelar", width=10,
                        command=addPersonal.destroy)
    btnCancelar.grid(column=1, row=5, padx=10, pady=10)
    
    def agregarPersonal():
        perso = Personal("", "", "", "", "", "")
        perso.set_apeynom(nombre.get())
        perso.set_dni(dni.get())
        perso.set_direccion(direccion.get())
        perso.set_telefono(telefono.get())
        perso.set_tarea(tarea.get())
        perso.crear_legajo()
        personal_l.append(perso)
        addPersonal.destroy()
        cargarTabla(tablePersonal)
    

def eliminarPersonal(tablePersonal):
    idx = tablePersonal.selection()[0]
    personal = tablePersonal.item(idx, 'values')

    b = False
    for x in personal_l:
        if x.get_dni() == personal[2]:
            print("\nPersonal encontrado \n")
            print(x)
            personal_l.remove(x)
            print("\nPersonal eliminado \n")
            b = True
    if not b:
        print("\nPersonal no encontrado \n")

    cargarTabla(tablePersonal)
