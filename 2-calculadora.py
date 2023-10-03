from simple_term_menu import TerminalMenu


def sumar():
    print("Sumar")


def restar():
    print("Restar")


def multiplicar():
    print("Multiplicar")


def dividir():
    print("Dividir")


def salir():
    print("Salir")
    exit()


def main():
    opciones = ["Sumar", "Restar", "Multiplicar", "Dividir", "Salir"]
    funciones = [sumar, restar, multiplicar, dividir, salir]

    while True:
        menu = TerminalMenu(opciones, clear_screen=False)
        indice_seleccionado = menu.show()
        funcion_seleccionada = funciones[indice_seleccionado]
        funcion_seleccionada()


if __name__ == "__main__":
    main()
