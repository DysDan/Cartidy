from Carta import Carta
from DatosRandom import colores, mana, tipo, adjetivos, sustantivos
import time, random
def Menu():
    salir = False
    print(salir)
    while not salir:
        print("Bienvenido a Cartidy.")
        print("Ingrese la operación que quiere ejecutar (Señalada por el entero que le antecede):")
        print("1. Crear cartas.")
        print("2. Ordenar cartas.")
        print("3. Simular mazo cartas.")
        print("4. Cerrar menú.")
        n = input()
        if not siEntradaEntera(n):
            print("Por favor digíte una opción válida.")
        else:
            n = int(n)
        if n == 4:
            salir = True
        elif n == 1:
            crearCartasMenu()

def crearCartasMenu():
    bandera = 1
    while bandera != 0:
        print("Ingrese cuantas cartas quiere crear para el testeo:")
        print("1. 10 cartas")
        print("2. 10000 cartas")
        print("3. 1000000 cartas")
        print("4. 100000000 cartas")
        print("5. Menú anterior")
        n = input()
        cantidad = 0
        if not siEntradaEntera(n):
            print("Por favor digíte una opción válida.")
        elif n == 5:
            break
        elif n == 1:
            cantidad = 10
        elif n == 2:
            cantidad = 10000
        elif n == 3:
            cantidad = 1000000
        elif n == 4:
            cantidad = 100000000
        crearCartas(cantidad)

def crearCartas(cant):
    cartas = []
    inicio = time.time()
    for i in range(cant):
        cartas.append(Carta(random.choice(adjetivos) + random.choice(sustantivos),random.choice(colores),random.choice(tipo),random.choice(mana)))
    fin = time.time()
    print("El tiempo que tomó realizar la operación fue de: " + str(fin-inicio) + " segundos.")

def siEntradaEntera(num):   
    try:
        int(num)
        return True
    except ValueError:
        return False


Menu()

