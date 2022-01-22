from domain import to_string, create_vanzare
from logic import add_vanzare, remove_vanzare, update_vanzare, reduce_pret, pret_minim_pe_gen, sorted_by_price, number_of_titles_by_gen, modify_titlu, read_from_file,save_to_file
from copy import deepcopy
def show_menu():
    print("1.Adauga vanzare")
    print("2.Sterge vanzare")
    print("3.Update vanzare")
    print("4.Aplicare discount")
    print("5.Modificare pentru gen")
    print("6.Determinare pret minim")
    print("8.Ordonare vanzari crescator")
    print("7.Numar de titluri distincte")
    print("x.Exit")

def ui_add_vanzare(lista_vanzari):
            try:
                id_vanzare=int(input("dati idul"))
                titlu=input("dati numele")
                gen=input("dati genul")
                pret=int(input("dati pretul"))
                tip_reducere=input("dati tipul de reducere")
                new_vanzari=add_vanzare(lista_vanzari, id_vanzare, titlu, gen, pret, tip_reducere)
                print("vanzare added")
                print (new_vanzari)
                return new_vanzari
            except ValueError as ve:
                print("Eroare",ve)
                return lista_vanzari


def ui_remove_vanzare(lista_vanzari):
    id_vanzare=int(input("dati id ul de sters"))
    print (remove_vanzare(lista_vanzari,id_vanzare))

def ui_update_vanzare(lista_vanzari):
    id_vanzare = int(input("dati id ul"))
    titlu = input("dati numele")
    gen = input("dati genul")
    pret = int(input("dati pretul"))
    tip_reducere = input("dati tipul de reducere")
    lista_vanzari=update_vanzare(
        lista_vanzari,
        id_vanzare,
        titlu,
        gen,
        pret,
        tip_reducere)
    print("vanzarea a fost actualizata")
    print (lista_vanzari)
    return lista_vanzari

def ui_reduce_pret(lista_vanzari):
    search_str1 =input("dati stringul de cautat")
    search_str2=input("dati stringul de cautat 2")
    lista_vanzari=reduce_pret(lista_vanzari, search_str1, search_str2)
    print("reducerea a fost facuta")
    print (lista_vanzari)
    return lista_vanzari


def ui_pret_minim_pe_gen(lista_vanzari):
    to_print=pret_minim_pe_gen(lista_vanzari)
    for k,v in to_print.items():
        print("Pentru genul:{} avem vanzarea: {} ".format(
            k,
            to_string(v)
        ))
    return lista_vanzari

def ui_titles_gen(lista_vanzari):
    lista=number_of_titles_by_gen(lista_vanzari)
    print(lista)
    return lista

def ui_modify_titlu(lista_vanzari):
    gen=input("dati genul")
    titlu=input("dati titlul")
    lista_vanzari=modify_titlu(lista_vanzari, gen, titlu)
    print(lista_vanzari)
    print("vanzarea a fost actualizata")
    return lista_vanzari

lista_vanza=read_from_file()

def run_ui(lista_vanzari):
    while True:
        show_menu()
        op=input("dati optiunile")
        opps=op.split(';')

        for opp in opps:
            lista_separata=opp.split(',')
            if lista_separata[0]=='add':
                lst=read_from_file()
                id_vanzare=lista_separata[1]
                titlu=lista_separata[2]
                gen=lista_separata[3]
                pret=int(lista_separata[4])
                tip_reducere=lista_separata[5]
                lista_vanzari=add_vanzare(lista_vanzari,id_vanzare,titlu,gen,pret,tip_reducere)
                print(lista_vanzari)
            if lista_separata[0]=='remove':
                lst=read_from_file()
                lista_vanzari=read_from_file()
                id_vanzare=lista_separata[1]
                print(remove_vanzare(lista_vanzari,id_vanzare))
            if lista_separata[0]=='update':
                lst=read_from_file()
                lista_vanzari=read_from_file()
                id_vanzare=lista_separata[1]
                titlu = lista_separata[2]
                gen = lista_separata[3]
                pret = lista_separata[4]
                tip_reducere = lista_separata[5]
                print(update_vanzare(lista_vanzari,id_vanzare,titlu,gen,pret,tip_reducere))
            if lista_separata[0]=='reduce':
                lst=read_from_file()
                search_str=lista_separata[1]
                search_str2=lista_separata[2]
                lista_vanzari=reduce_pret(lista_vanzari,search_str,search_str2)
                print(lista_vanzari)
            if lista_separata[0]=='modify':
                lst=read_from_file()
                lista_vanzari=read_from_file()
                gen=lista_separata[1]
                titlu=lista_separata[2]
                print(modify_titlu(lista_vanzari,gen, titlu))
            if lista_separata[0]=='minim':
                lista_vanzari=ui_pret_minim_pe_gen(lista_vanzari)
            if lista_separata[0]=='numar':
                lista_vanzari=read_from_file()
                lista_vanzari=ui_titles_gen(lista_vanzari)
            if lista_separata[0]=='sorteaza':
                lista_vanzari=read_from_file()
                print(sorted_by_price(lista_vanzari))
            if lista_separata[0]=='undo':
                lista_vanzari=lst
                print(lst)
            if op=="x":
                break
    return lista_vanzari












