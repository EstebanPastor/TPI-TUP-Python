from models.Alumno import Alumno
from models.Docente import Docente
from models.Personal import Personal
from models.Directivo import Directivo
import os

# Iniciando Listas
almunos_l = []
docentes_l = []
personal_l = []
directivos_l = []

# Creando Objetos Iniciales
alumno = Alumno("1", "Esteban Pastor", "33333333", "Cordoba 1100", "3413629615", "estebanandrespastor@gmail.com", "Argentina", "Rosario", "1", "0", "0", "0")
alumno.crear_legajo()
almunos_l.append(alumno)

docente = Docente("1", "Agustina Dominguez", "341255423", "Zeballos 1372", "343144567", "No poseo", "Enginner", "Programacion")
docente.crear_legajo()
docentes_l.append(docente)

personal = Personal("1", "Carolina Lopez", "32182211", "Toay 6262", "38333213", "Limpieza")
personal.crear_legajo()
personal_l.append(personal)

directivo = Directivo("1", "Gerardo Rivas", "29888776", "Oroño 320", "341334552", "No poseo")
directivo.crear_legajo()
directivos_l.append(directivo)


def main():
    # Función Inicial y borrado de pantalla
    os.system('cls')
    print("""
Bienvenido al Sistema del colegio CHESTER
Por favor, seleccione una de las opciones del menú según la acción que desea realizar

[1] Modulo Alumnos
[2] Modulo Docentes
[3] Modulo Personal
[4] Modulo Directivo

""")
    
    # Solicitud de ingreso
    opc = input("Ingrese un número del 1 al 4: ")
    if opc == '1':
        alumnos()
    elif opc == '2':
        docentes()
    elif opc == '3':
        personal()
    elif opc == '4':
        directivos()
    else:
        print("Por favor, ingrese un número valido (del 1 al 4)")
        print("=-="*20)


def alumnos():
    os.system('cls')
    print("""
Modulo Alumnos

[1] Listar Alumnos
[2] Agregar Alumno
[3] Borrar Alumno
[4] Volver al Inicio

""")
    opc = input("Ingrese un número del 1 al 4: ")
    if opc == '1':
        os.system('cls')
        if not almunos_l:
            print("Lista Vacía...")
            os.system('pause')
            alumnos()
        print("\nListado de Alumnos\n")
        for i, alu in enumerate(almunos_l, start=1):
            print(i, alu)
        os.system('pause')       
        alumnos()
    elif opc == '2':
        alumno = Alumno("", "", "", "", "", "", "", "", "", "", "", "")
        os.system('cls')
        alumno.set_apeynom(input("Ingrese Nombre y Apellido: "))
        alumno.set_dni(input("Ingrese el DNI: "))
        alumno.set_direccion(input("Ingrese la dirección: "))
        alumno.set_telefono(input("Ingrese N. Teléfono: "))
        alumno.set_email(input("Ingrese el Correo: "))
        alumno.set_nacionalidad(input("Ingrese la Nacionalidad: "))
        alumno.set_residencia(input("Ingrese la residencia: "))
        alumno.set_canthnos(input("Ingrese la Cantida de Hermanos: "))
        alumno.set_telpadre(input("Ingrese Teléfono del Padre: "))
        alumno.set_telmadre(input("Ingrese Teléfono del la Madre: "))
        alumno.set_teladi(input("Ingrese Teléfono diccional: "))
        alumno.crear_legajo()
        almunos_l.append(alumno)
        os.system('pause')
        alumnos()
    elif opc == '3':
        os.system('cls')
        if not almunos_l:
            print("Lista Vacía, no hay alumnos para eliminar...")
            os.system('pause')
            alumnos()
            
        b = False
        dni = input("Ingrese el DNI del Alumno a eliminar: ")
        for x in almunos_l:
            if x.get_dni() == dni:
                print("\nAlumno encontrado \n")
                print(x)
                almunos_l.remove(x)              
                print("\nAlumno eliminado \n")
                b = True
        if not b:
            print("\nAlumno no encontrado \n")
            
        os.system("pause")
        alumnos()    
    elif opc == '4':
        main()
    else:
        print("Por favor, ingrese un número valido (del 1 al 4)")
        print("=-="*20)


def docentes():
    os.system('cls')
    print("""
Modulo Docentes

[1] Listar Docentes
[2] Agregar Docente
[3] Borrar Docente
[4] Volver al Inicio

""")
    opc = input("Ingrese un número del 1 al 4: ")
    if opc == '1':
        os.system('cls')
        if not almunos_l:
            print("Lista Vacía...")
            os.system('pause')
            docentes()
        print("\nListado de Docentes\n")
        for i, doc in enumerate(docentes_l, start=1):
            print(i, doc)
        os.system('pause')       
        docentes()
    elif opc == '2':
        docente = Docente("", "", "", "", "", "", "", "")
        os.system('cls')
        docente.set_apeynom(input("Ingrese Nombre y Apellido: "))
        docente.set_dni(input("Ingrese el DNI: "))
        docente.set_direccion(input("Ingrese la dirección: "))
        docente.set_telefono(input("Ingrese N. Teléfono: "))
        docente.set_telurgencia(input("Ingrese su telefono de urgencia: "))
        docente.set_titulo(input("Ingrese su titulo: "))
        docente.set_materia(input("Ingrese la materia que le fue asignada: "))
        docente.crear_legajo()
        docentes_l.append(docente)
        os.system('pause')
        docentes()
        
    elif opc == '3':
        os.system('cls')
        if not docentes_l:
            print("Lista Vacía, no hay docentes para eliminar...")
            os.system('pause')
            docentes()
        
        b = False
        dni = input("Ingrese el DNI del Docente a eliminar: ")
        for x in docentes_l:
            if x.get_dni() == dni:
                print("\nDocente encontrado \n")
                print(x)
                docentes_l.remove(x)
                print("\nDocente eliminado \n")
                b = True
        if not b:
            print("\nDocente no encontrado \n")
                
        os.system("pause")
        docentes()
    elif opc == '4':
        main()
    else:
        print("Por favor, ingrese un número valido (del 1 al 4)")
        print("=-="*20)


def personal():
    os.system('cls')
    print("""
Modulo Personal

[1] Listar Personal
[2] Agregar Personal
[3] Borrar Personal
[4] Volver al Inicio

""")
    opc = input("Ingrese un número del 1 al 4: ")
    if opc == '1':
        os.system('cls')
        if not personal_l:
            print("Lista Vacía...")
            os.system('pause')
            personal()
        print("\nListado del Personal\n")
        for i, perso in enumerate(personal_l, start=1):
            print(i, perso)
        os.system('pause')       
        personal()  
    elif opc == '2':
        perso = Personal("", "", "", "", "", "")
        os.system('cls')
        perso.set_apeynom(input("Ingrese Nombre y Apellido: "))
        perso.set_dni(input("Ingrese el DNI: "))
        perso.set_direccion(input("Ingrese la dirección: "))
        perso.set_telefono(input("Ingrese N. Teléfono: "))
        perso.set_tarea(input("Ingrese la tarea que realiza en la institución: "))
        perso.crear_legajo()
        personal_l.append(perso)
        os.system('pause')
        personal()
    elif opc == '3':
        os.system('cls')
        if not personal_l:
            print("Lista vacía, no hay personal para eliminar...")
            os.system('pause')
            personal()
        
        b = False
        dni = input("Ingrese el DNI del personal a eliminar: ")
        for x in personal_l:
            if x.get_dni() == dni:
                print("\nPersonal encontrado \n")
                print(x)
                personal_l.remove(x)
                print("\nPersonal eliminado \n")
                b = True
        if not b:
            print("\nPersonal no encontrado \n")
                
        os.system("pause")
        personal()
    elif opc == '4':
        main()
    else:
        print("Por favor, ingrese un número valido (del 1 al 4)")
        print("=-="*20)


def directivos():
    os.system('cls')
    print("""
Modulo Directivo

[1] Listar Directivos
[2] Agregar Directivo
[3] Borrar Directivo
[4] Volver al Inicio

""")
    opc = input("Ingrese un número del 1 al 4: ")
    if opc == '1':
        os.system('cls')
        if not directivos_l:
            print("Lista vacía...")
            os.system('pause')
            directivos()
        print("\nListado de los directivos\n")
        for i, dirc in enumerate(directivos_l, start=1):
            print(i, dirc)
        os.system('pause')       
        directivos()  
    elif opc == '2':
        dirc = Directivo("", "", "", "", "", "")
        os.system('cls')
        dirc.set_apeynom(input("Ingrese Nombre y Apellido: "))
        dirc.set_dni(input("Ingrese el DNI: "))
        dirc.set_direccion(input("Ingrese la dirección: "))
        dirc.set_telefono(input("Ingrese N. Teléfono: "))
        dirc.set_telurgencia(input("Ingrese su telefono de urgencia: "))
        dirc.crear_legajo()
        directivos_l.append(dirc)
        
        opx = input("\nEl Directivo es Docente? (Si/No): ")
        if opx == 'Si' or opx == 'si':
            docente = Docente("", "", "", "", "", "", "", "")
            os.system('cls')
            docente.set_apeynom(dirc.get_apeynom())
            docente.set_dni(dirc.get_dni())
            docente.set_direccion(dirc.get_direccion())
            docente.set_telefono(dirc.get_telefono())
            docente.set_telurgencia(dirc.get_telurgencia())
            docente.set_titulo(input("Ingrese el titulo: "))
            docente.set_materia(input("Ingrese la materia que le fue asignada: "))
            docente.crear_legajo()
            docentes_l.append(docente)
            print("\nDirectivo agregado a la lista de docentes")
        else:
            print("\nDirectivo no agregado a la lista de docentes")
        os.system('pause')
        directivos()
    elif opc == '3':
        os.system('cls')
        if not directivos_l:
            print("Lista vacía, no hay directivos para eliminar...")
            os.system('pause')
            directivos()
        
        b = False
        dni = input("Ingrese el DNI del directivo a eliminar: ")
        for x in directivos_l:
            if x.get_dni() == dni:
                print("\nDirectivo encontrado \n")
                print(x)
                directivos_l.remove(x)
                print("\nDirectivo eliminado \n")
                b = True
        if not b:
            print("\nDirectivo no encontrado \n")
                
        os.system("pause")
        directivos()
    elif opc == '4':
        main()
    else:
        print("Por favor, ingrese un número valido (del 1 al 4)")
        print("=-="*20)


if __name__ == '__main__':
    main()
