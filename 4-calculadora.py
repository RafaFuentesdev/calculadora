from simple_term_menu import TerminalMenu


def obtener_numeros():
    while True:
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            return num1, num2
        except ValueError:
            print("\nPor favor, introduce números válidos.\n")


def sumar(num1, num2):
    return num1 + num2


def restar(num1, num2):
    return num1 - num2


def multiplicar(num1, num2):
    return num1 * num2


def dividir(num1, num2):
    if num2 == 0:
        print("No se puede dividir por cero. Inténtalo de nuevo.")
    else:
        return num1 / num2


def salir():
    print("¡Hasta luego!")
    exit()


def main():
    opciones = ["Sumar", "Restar", "Multiplicar", "Dividir", "Salir"]
    funciones = [sumar, restar, multiplicar, dividir, salir]

    while True:
        menu = TerminalMenu(opciones, clear_screen=True)
        indice_seleccionado = menu.show()
        if indice_seleccionado != len(opciones) - 1:  # Si la opción no es 'Salir'
            print(f"{opciones[indice_seleccionado]}")
            num1, num2 = obtener_numeros()
            funcion_seleccionada = funciones[indice_seleccionado]
            resultado = funcion_seleccionada(num1, num2)  # Almacenar el resultado
            print(f"El resultado es: {resultado}")
            input("Pulsa ENTER para continuar...")
        else:
            salir()


if __name__ == "__main__":
    main()
