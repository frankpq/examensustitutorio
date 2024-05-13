class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.__nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def imprimir_datos(self):
        print("Nombre: {}".format(self.__nombre))
        print("Edad: {}".format(self.edad))
        print("Ciudad: {}".format(self.ciudad))


class Empleado(Persona):
    def __init__(self, nombre, edad, ciudad):
        super().__init__(nombre, edad, ciudad)
        self.sueldo = float(input("Ingrese el sueldo del empleado: "))

    def impuesto(self):
        if self.sueldo > 5500:
            impuesto = self.sueldo * 0.09
            print("El empleado debe pagar impuestos.")
        else:
            impuesto = 0
            print("El empleado no debe pagar impuestos.")
        return impuesto


def manejo_diccionario(empleados):
    diccionario = {}
    for empleado in empleados:
        impuesto = empleado.impuesto()
        diccionario[empleado._Persona__nombre] = {
            'edad': empleado.edad,
            'sueldo': empleado.sueldo,
            'impuesto': impuesto
        }
    return diccionario


def mostrar_empleados(empleados):
    for nombre, datos in empleados.items():
        print("Nombre: {}, Edad: {}, Sueldo: {}, Impuesto: {}".format(nombre, datos['edad'], datos['sueldo'], datos['impuesto']))


def encontrar_empleado(empleados, nombre):
    if nombre in empleados:
        datos = empleados[nombre]
        print("El empleado {} tiene una remuneración de {} y un impuesto de {}".format(nombre, datos['sueldo'], datos['impuesto']))
    else:
        print("No se encontró al empleado {} en la lista.".format(nombre))


def main():
    empleados = {}
    while True:
        nombre = input("Ingrese el nombre del empleado (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        edad = int(input("Ingrese la edad del empleado: "))
        ciudad = input("Ingrese la ciudad del empleado: ")
        empleado = Empleado(nombre, edad, ciudad)
        empleados[nombre] = {
            'edad': empleado.edad,
            'sueldo': empleado.sueldo,
            'impuesto': empleado.impuesto()
        }

    mostrar_empleados(empleados)

    nombre_buscar = input("Ingrese el nombre del empleado que desea buscar: ")
    encontrar_empleado(empleados, nombre_buscar)


if __name__ == "__main__":
    main()
