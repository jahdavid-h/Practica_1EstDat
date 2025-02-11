class Estudiante:
    def __init__(self, nombre, calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones  # Se espera una lista de 4 calificaciones

    @property
    def promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones) if len(self.calificaciones) > 0 else 0

    def modificar_calificacion(self, parcial, calificacion):
        if 0 <= parcial < 4:
            self.calificaciones[parcial] = calificacion
        else:
            print("Parcial no válido. Debe ser entre 1er y 4to.")

    def __str__(self):
        return f"Nombre: {self.nombre}, Calificaciones: {self.calificaciones},\n Promedio: {self.promedio:.2f}"


class RegistroEstudiantes:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, nombre, calificaciones):
        estudiante = Estudiante(nombre, calificaciones)
        self.estudiantes.append(estudiante)

    def borrar_estudiante(self, nombre):
        self.estudiantes = [est for est in self.estudiantes if est.nombre != nombre]

    def modificar_calificacion(self, nombre, parcial, calificacion):
        for est in self.estudiantes:
            if est.nombre == nombre:
                est.modificar_calificacion(parcial, calificacion)
                return
        print("Estudiante no encontrado.")

    def mostrar_estudiantes(self):
        for est in self.estudiantes:
            print(est)

def main():
    registro = RegistroEstudiantes()
    while True:
        print("\nMenú de Operaciones:")
        print("1. Agregar Estudiante")
        print("2. Borrar Estudiante")
        print("3. Modificar Calificación")
        print("4. Mostrar Estudiantes")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del estudiante: ")
            calificaciones = []
            for i in range(4):
                calificacion = float(input(f"Ingrese la calificación del parcial {i + 1}: "))
                calificaciones.append(calificacion)
            registro.agregar_estudiante(nombre, calificaciones)
        elif opcion == '2':
            nombre = input("Ingrese el nombre del estudiante a borrar: ")
            registro.borrar_estudiante(nombre)
        elif opcion == '3':
            nombre = input("Ingrese el nombre del estudiante: ")
            parcial = int(input("Ingrese el número del parcial (1er-4to): "))
            calificacion = float(input("Ingrese la nueva calificación: "))
            registro.modificar_calificacion(nombre, parcial, calificacion)
        elif opcion == '4':
            registro.mostrar_estudiantes()
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()