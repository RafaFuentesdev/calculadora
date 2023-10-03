from simple_term_menu import TerminalMenu
from termcolor import colored


def obtener_numeros():
    while True:
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            return num1, num2
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


def salir():
    print("¡Hasta luego!")
    exit()


def main():
    print(colored("Bienvenido a la Calculadora", "green"))
    opciones = ["Sumar", "Restar", "Multiplicar", "Dividir", "Salir"]
    funciones = [sumar, restar, multiplicar, dividir, salir]

    while True:
        menu = TerminalMenu(
            opciones,
            clear_screen=True,
            title="Selecciona una operación:",
        )
        indice_seleccionado = menu.show()
        if indice_seleccionado != len(opciones) - 1:  # Si la opción no es 'Salir'
            print(colored(f"\n{opciones[indice_seleccionado]}", "blue"))
            print("=" * 30)  # Línea separadora
            num1, num2 = obtener_numeros()
            funcion_seleccionada = funciones[indice_seleccionado]
            resultado = funcion_seleccionada(num1, num2)  # Almacenar el resultado
            if resultado is not None:
                print(colored(f"\nEl resultado es: {resultado}", "green"))
            print("=" * 30)  # Línea separadora
            input(colored("Pulsa ENTER para continuar...", "yellow"))
        else:
            salir()


if __name__ == "__main__":
    main()
