from simple_term_menu import TerminalMenu


def sumar():
    pass


def restar():
    pass


def multiplicar():
    pass


def dividir():
    pass


def salir():
    pass


def main():
    opciones = {
        "Sumar": sumar,
        "Restar": restar,
        "Multiplicar": multiplicar,
        "Dividir": dividir,
        "Salir": salir,
    }

    menu = TerminalMenu(opciones, clear_screen=True)

    opcion_seleccionada = menu.show()

    print(opcion_seleccionada)

if __name__ == "__main__":
    main()
