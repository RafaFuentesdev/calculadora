from simple_term_menu import TerminalMenu
from termcolor import colored
import cmath  # Para manejar raíces complejas
import math  # Para operaciones matemáticas
import time

historial = []  # Lista para almacenar el historial de operaciones


def obtener_numero():
    while True:
        try:
            num = input("Introduce un número (o 'menu' para volver al menú): ")
            if num.lower() == "menu":
                return None  # Regresar al menú si el usuario introduce 'menu'
            return float(num)
        except ValueError:
            print(colored("\nPor favor, introduce un número válido.", "red"))
            print("=" * 30)  # Línea separadora


def obtener_numeros():
    while True:
        try:
            num1 = input("Introduce el primer número (o 'menu' para volver al menú): ")
            if num1.lower() == "menu":
                return None, None  # Regresar al menú si el usuario introduce 'menu'
            num1 = float(num1)
            num2 = float(input("Introduce el segundo número: "))
            return num1, num2
        except ValueError:
            print(colored("\nPor favor, introduce números válidos.", "red"))
            print("=" * 30)  # Línea separadora


def obtener_coeficientes():
    while True:
        try:
            a = float(input("Introduce el coeficiente a: "))
            b = float(input("Introduce el coeficiente b: "))
            c = float(input("Introduce el coeficiente c: "))
            return a, b, c
        except ValueError:
            print(colored("\nPor favor, introduce números válidos.", "red"))
            print("=" * 30)  # Línea separadora


def sumar(num1, num2):
    return num1 + num2


def restar(num1, num2):
    return num1 - num2


def multiplicar(num1, num2):
    return num1 * num2


def dividir(num1, num2):
    if num2 == 0:
        print(colored("\nNo se puede dividir por cero. Inténtalo de nuevo.", "red"))
    else:
        return num1 / num2


def resolver_ecuacion_cuadratica(a, b, c):
    discriminante = cmath.sqrt(b**2 - 4 * a * c)
    root1 = (-b - discriminante) / (2 * a)
    root2 = (-b + discriminante) / (2 * a)
    return root1, root2


def calcular_raiz(num):
    return math.sqrt(num) if num >= 0 else cmath.sqrt(num)


def calcular_factorial(num):
    return math.factorial(int(num))


def calcular_exponente(base, exponente):
    return base**exponente


def mostrar_historial():
    print(colored("Historial de Operaciones:", "magenta"))
    for operacion in historial:
        print(operacion)
    print("=" * 30)  # Línea separadora


def borrar_historial():
    historial.clear()
    print(colored("Historial borrado.", "magenta"))
    print("=" * 30)  # Línea separadora


def salir():
    print("¡Hasta luego!")
    exit()


def main():
    print(colored("Bienvenido a la Calculadora", "green"))
    time.sleep(1)
    opciones = [
        "Sumar",
        "Restar",
        "Multiplicar",
        "Dividir",
        "Resolver Ecuación Cuadrática",
        "Calcular Raíz Cuadrada",
        "Calcular Factorial",
        "Calcular Exponente",
        "Ver Historial",
        "Borrar Historial",
        "Salir",
    ]
    funciones = [
        sumar,
        restar,
        multiplicar,
        dividir,
        resolver_ecuacion_cuadratica,
        calcular_raiz,
        calcular_factorial,
        calcular_exponente,
        mostrar_historial,
        borrar_historial,
        salir,
    ]

    while True:
        print("=" * 30)  # Línea separadora
        menu = TerminalMenu(
            opciones,
            clear_screen=True,
            title="Selecciona una operación:",
        )
        indice_seleccionado = menu.show()
        if indice_seleccionado != len(opciones) - 1:  # Si la opción no es 'Salir'
            print(colored(f"\n{opciones[indice_seleccionado]}", "blue"))
            print("=" * 30)  # Línea separadora
            if indice_seleccionado in [
                5,
                6,
            ]:  # Si la opción es 'Calcular Raíz Cuadrada' o 'Calcular Factorial'
                num = obtener_numero()
                if num is None:  # Verificar si el usuario decidió regresar al menú
                    continue
                funcion_seleccionada = funciones[indice_seleccionado]
                resultado = funcion_seleccionada(num)
                print(colored(f"\nEl resultado es: {resultado}", "green"))
                # Almacenar la operación en el historial
                historial.append(
                    f"{opciones[indice_seleccionado]}({num}) = {resultado}"
                )
                print("=" * 30)  # Línea separadora
                input(colored("Pulsa ENTER para continuar...", "yellow"))
            elif indice_seleccionado == 7:  # Si la opción es 'Calcular Exponente'
                base, exponente = obtener_numeros()
                if base is None:  # Verificar si el usuario decidió regresar al menú
                    continue
                resultado = calcular_exponente(base, exponente)
                print(colored(f"\nEl resultado es: {resultado}", "green"))
                # Almacenar la operación en el historial
                historial.append(
                    f"{opciones[indice_seleccionado]}({base}, {exponente}) = {resultado}"
                )
                print("=" * 30)  # Línea separadora
                input(colored("Pulsa ENTER para continuar...", "yellow"))
            elif (
                indice_seleccionado == 4
            ):  # Si la opción es 'Resolver Ecuación Cuadrática'
                a, b, c = obtener_coeficientes()
                resultado = resolver_ecuacion_cuadratica(a, b, c)
                print(colored(f"\nLas raíces son: {resultado}", "green"))
                # Almacenar la operación en el historial
                historial.append(
                    f"{opciones[indice_seleccionado]}: {a}x^2 + {b}x + {c} = 0, Raíces = {resultado}"
                )
                print("=" * 30)  # Línea separadora
                input(colored("Pulsa ENTER para continuar...", "yellow"))
            elif indice_seleccionado not in [
                8,
                9,
            ]:  # Si la opción no es 'Ver Historial' ni 'Borrar Historial'
                num1, num2 = obtener_numeros()
                if num1 is None:  # Verificar si el usuario decidió regresar al menú
                    continue
                funcion_seleccionada = funciones[indice_seleccionado]
                resultado = funcion_seleccionada(num1, num2)  # Almacenar el resultado
                if resultado is not None:
                    print(colored(f"\nEl resultado es: {resultado}", "green"))
                    # Almacenar la operación en el historial
                    historial.append(
                        f"{opciones[indice_seleccionado]}: {num1}, {num2} = {resultado}"
                    )
                print("=" * 30)  # Línea separadora
                input(colored("Pulsa ENTER para continuar...", "yellow"))
            else:
                funcion_seleccionada = funciones[indice_seleccionado]
                funcion_seleccionada()
                input(colored("Pulsa ENTER para continuar...", "yellow"))
        else:
            salir()


if __name__ == "__main__":
    main()
