from simple_term_menu import TerminalMenu


def main():
    opciones = ["Sumar", "Restar", "Multiplicar", "Dividir", "Salir"]

    menu = TerminalMenu(opciones, clear_screen=True)

    indice_seleccionado = menu.show()

    print(indice_seleccionado)


if __name__ == "__main__":
    main()
