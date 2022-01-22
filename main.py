from logic import add_vanzare, read_from_file
from user_interface import run_ui


def main():
    lista_vanzari = read_from_file()
    lista_vanzari = run_ui(lista_vanzari)

if __name__ == '__main__':
    main()