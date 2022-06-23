from tkinter import ttk
from tkinter import *
from models.Docente import Docente

# Iniciando Listas
docentes_l = []

# Creando Objetos Iniciales
docente = Docente("1", "Agustina Dominguez", "341255423", "Zeballos 1372", "343144567", "No poseo", "Enginner", "Programacion")
docente.crear_legajo()
docentes_l.append(docente)

# Ventana Principal
def docView(root):
    docenteV = Toplevel(root)
    docenteV.title("Modulo de docentes")
    docenteV.geometry("800x600")

    # Marco
    marco = LabelFrame(docenteV, text="Listado de los docentes")
    marco.place(x=20, y=20, width=750, height=550)

    # Tabla
    tableDocentes = ttk.Treeview(marco, height=20)
    tableDocentes.grid(column=1, row=1, columnspan=4, padx=10, pady=10)
    tableDocentes["columns"] = (
        "Legajo", "Nombre", "DNI", "Dirección", "Telefono", "Tel. Urgencia", "Titulo", "Materia")
    tableDocentes.column("#0", width=20, anchor=CENTER)
    tableDocentes.column("Legajo", width=50, anchor=CENTER)
    tableDocentes.column("Nombre", width=100, anchor=CENTER)
    tableDocentes.column("DNI", width=50, anchor=CENTER)
    tableDocentes.column("Dirección", width=100, anchor=CENTER)
    tableDocentes.column("Telefono", width=100, anchor=CENTER)
    tableDocentes.column("Tel. Urgencia", width=100, anchor=CENTER)
    tableDocentes.column("Titulo", width=100, anchor=CENTER)
    tableDocentes.column("Materia", width=100, anchor=CENTER)

    tableDocentes.heading("#0", text="#", anchor=CENTER)
    tableDocentes.heading("Legajo", text="Legajo", anchor=CENTER)
    tableDocentes.heading("Nombre", text="Nombre", anchor=CENTER)
    tableDocentes.heading("DNI", text="DNI", anchor=CENTER)
    tableDocentes.heading("Dirección", text="Dirección", anchor=CENTER)
    tableDocentes.heading("Telefono", text="Telefono", anchor=CENTER)
    tableDocentes.heading("Tel. Urgencia", text="Tel. Urgencia", anchor=CENTER)
    tableDocentes.heading("Titulo", text="Titulo", anchor=CENTER)
    tableDocentes.heading("Materia", text="Materia", anchor=CENTER)

    # Botones
    btnEliminar = Button(marco, text="Eliminar", width=20,
                         command=lambda: eliminarDocente(tableDocentes))
    btnEliminar.grid(column=1, row=3, padx=10, pady=10)
    btnAgregar = Button(marco, text="Agregar", width=20,
                        command=lambda: agregarDocenteView(root, tableDocentes))
    btnAgregar.grid(column=3, row=3, padx=10, pady=10)

    cargarTabla(tableDocentes)


# Funciones
def cargarTabla(tableDocentes):
    rows = tableDocentes.get_children()
    for row in rows:
        tableDocentes.delete(row)

    for i, doce in enumerate(docentes_l, start=1):
        id = i
        tableDocentes.insert("", END, id, text=id, values=(doce.legajo, doce.get_apeynom(
        ), doce.get_dni(), doce.get_direccion(), doce.get_telefono(), doce.get_telurgencia(), doce.get_titulo(), doce.get_materia()))


def agregarDocenteView(root, tableDocentes):
    addDocente = Toplevel(root)
    addDocente.title("Agregar docente")
    addDocente.geometry("400x400")

    # Vars
    nombre = StringVar()
    dni = StringVar()
    direccion = StringVar()
    telefono = StringVar()
    telurgencia = StringVar()
    titulo = StringVar()
    materia = StringVar()

    # Marco
    marco = LabelFrame(addDocente, text="Formulario Agregar Docente")
    marco.place(x=10, y=10, width=350, height=380)

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
    
    lbltelur = Label(marco, text="Telefono de urgencia: ").grid(column=0, row=4, padx=10, pady=10)
    txtelur = Entry(marco, textvariable=telurgencia, width=30)
    txtelur.grid(column=1, row=4, padx=10, pady=10)
    
    lbltitulo = Label(marco, text="Titulo: ").grid(column=0, row=5, padx=10, pady=10)
    txtitulo = Entry(marco, textvariable=titulo, width=30)
    txtitulo.grid(column=1, row=5, padx=10, pady=10)

    lblmateria = Label(marco, text="Materia: ").grid(column=0, row=6, padx=10, pady=10)
    txtmateria = Entry(marco, textvariable=materia, width=30)
    txtmateria.grid(column=1, row=6, padx=10, pady=10)
    
    # Botones
    btnConfirmar = Button(marco, text="Aceptar", width=10,
                         command=lambda: agregarDocente())
    btnConfirmar.grid(column=0, row=7, padx=10, pady=10)
    
    btnCancelar = Button(marco, text="Cancelar", width=10,
                        command=addDocente.destroy)
    btnCancelar.grid(column=1, row=7, padx=10, pady=10)
    
    def agregarDocente():
        docente = Docente("", "", "", "", "", "", "", "")
        docente.set_apeynom(nombre.get())
        docente.set_dni(dni.get())
        docente.set_direccion(direccion.get())
        docente.set_telefono(telefono.get())
        docente.set_telurgencia(telurgencia.get())
        docente.set_titulo(titulo.get())
        docente.set_materia(materia.get())
        docente.crear_legajo()
        docentes_l.append(docente)
        addDocente.destroy()
        cargarTabla(tableDocentes)
    

def eliminarDocente(tableDocentes):
    idx = tableDocentes.selection()[0]
    docenteV = tableDocentes.item(idx, 'values')

    b = False
    for x in docentes_l:
        if x.get_dni() == docenteV[2]:
            print("\nDocente encontrado \n")
            print(x)
            docentes_l.remove(x)
            print("\nDocente eliminado \n")
            b = True
    if not b:
        print("\nDocente no encontrado \n")

    cargarTabla(tableDocentes)
