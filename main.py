from tkinter import ttk
from tkinter import *


def main():
    # Creando vista
    root = Tk()

    # Creando Frame
    frame = Frame(root)

    # Creando Menú
    menu = Menu(root)
    barraArchivo = Menu(menu, tearoff="off")
    barraAgenda = Menu(menu, tearoff="off")

    # Menú Archivo
    barraArchivo.add_command(label="Salir", command=root.destroy)

    # Menú Agenda
    barraAgenda.add_command(label="Alumnos")
    barraAgenda.add_command(label="Docentes")
    barraAgenda.add_command(label="Personal")
    barraAgenda.add_command(label="Directivos")

    # Agregar menú a las barras
    menu.add_cascade(label="Archivo", menu=barraArchivo)
    menu.add_cascade(label="Agenda", menu=barraAgenda)

    boton = ttk.Button(text="¡Hola, mundo!")
    boton.place(x=50, y=50)

    # Loop de la vista y configuración
    root.geometry("1024x768")
    root.title("Colegio Chester")
    frame.pack()
    root.config(menu=menu)
    root.mainloop()


if __name__ == '__main__':
    main()
