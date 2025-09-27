estudiantes = []
afirmacion = True
mensaje = '''
___________________________________________
|                                         |
|          Sistema de Gestion de          |
|          Estudiantes - Edutech          |
|_________________________________________|
|                                         |
| 1. Regristar estudiante                 |
| 2. Listar estudiantes                   |
| 3. Buscar estudiante por nombre         |
| 4. Calcular promedio de calificaciones  |
| 5. salir                                |
|_________________________________________|
'''
def menu():
    while afirmacion:
        print(mensaje)
    
        opt = int(input('seleccione una opción (1-5): '))     
        if opt == 1:
            registrar_estudiante(estudiantes)
        elif opt == 2:
            listar_estudiantes(estudiantes)
        elif opt == 3:
            buscar_estudiante(estudiantes)
        elif opt == 4:
            calcular_promedio(estudiantes)
        elif opt == 5:
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor ingrese un número del 1 al 5.\n")
            
        if afirmacion:
            input("\nPresione Enter para continuar...")
            print("\n" * 2)    
                
def registrar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ").strip()
    asignatura = input("Ingrese la asignatura inscrita: ").strip()
    while True:
        try:
            calificacion = float(input("Ingrese la calificación: "))
            if 0 <= calificacion <= 5:
                break
            else:
                print("Error: La calificación debe estar entre 0 y 5.")
        except ValueError:
            print("Error: Debe ingresar un número válido para la calificación.")
    estudiante = (nombre, asignatura, calificacion)
    estudiantes.append(estudiante)
    print(f"Estudiante {nombre} registrado correctamente.\n")

def listar_estudiantes(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.\n")
    else:
        print("Lista de estudiantes registrados:")
        for i, (nombre, asignatura, calificacion) in enumerate(estudiantes, start=1):
            print(f"{i}. Nombre: {nombre}, Asignatura: {asignatura}, Calificación: {calificacion}")
        print()

def buscar_estudiante(estudiantes):
    nombre_buscar = input("Ingrese el nombre del estudiante a buscar: ").strip()
    encontrados = [est for est in estudiantes if est[0].lower() == nombre_buscar.lower()]
    if encontrados:
        for nombre, asignatura, calificacion in encontrados:
            print(f"Estudiante encontrado - Nombre: {nombre}, Asignatura: {asignatura}, Calificación: {calificacion}")
        print()
    else:
        print(f"No existe ningún estudiante registrado con el nombre '{nombre_buscar}'.\n")

def calcular_promedio(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados para calcular el promedio.\n")
    else:
        suma = sum(est[2] for est in estudiantes)
        promedio = suma / len(estudiantes)
        print(f"El promedio de calificaciones del curso es: {promedio:.2f}\n")
        

if __name__ == "__main__":
    menu()