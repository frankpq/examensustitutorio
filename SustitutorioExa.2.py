import random
from datetime import datetime

def obtener_numero():
    return random.randint(1, 50)

def pedir_numero():
    while True:
        try:
            numero = int(input("Adivina el número que se encuentra entre 1 y 50: "))
            if 0 < numero < 100:
                return numero
            else:
                print("El número debe ser mayor a 0 y menor a 100.")
        except ValueError:
            print("Por favor ingresa un número entero válido.")

def adivina():
    numero_aleatorio = obtener_numero()
    print("Adivina el número secreto")

    while True:
        intento = pedir_numero()

        if intento == numero_aleatorio:
            print("Has ganadooo!!!!!")
            ahora = datetime.now()
            print("Fecha y hora de la victoria: {}".format(ahora.strftime('%Y-%m-%d %H:%M')))
            break
        elif intento < numero_aleatorio:
            print("El número secreto es mayor.")
        else:
            print("El número secreto es menor.")

def decorador_mensaje(func):
    def wrapper():
        print("---Comenzamos el juego---")
        func()
        print("--Fin del juego--")
    return wrapper

@decorador_mensaje
def main():
    adivina()

if __name__ == "__main__":
    main()
