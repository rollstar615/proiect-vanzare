from copy import deepcopy
from domain import create_vanzare, get_id, get_titlu, get_gen, get_pret, get_reducere, set_pret
import json

def save_to_file(lista_vanzari):
    with open('vanzari.txt', 'w') as f_out:
        f_out.write(json.dumps(lista_vanzari))

def read_from_file():
    try:
        with open('vanzari.txt', 'r')as f_in:
            return json.loads(f_in.read())
    except FileNotFoundError:
        return[]

def get_vanzare_by_id(lista_vanzari, id_vanzare):
    for vanzare in lista_vanzari:
        if get_id(vanzare)==id_vanzare:
            return vanzare
    return None


def add_vanzare(lista_vanzari, id_vanzare, titlu, gen, pret, tip_reducere):
    #adauga o vanzare pe baza de id verificand daca exista o vanzare cu idul respectiv
    #param in:lista_vanzari, id_vanzare, titlu, gen, pret, tip_reducere
    #param out: result
    if get_vanzare_by_id(lista_vanzari, id_vanzare) is not None:
        raise ValueError('Exista deja o vanzare cu id-ul {}'.format(id_vanzare))
    new_vanzare=create_vanzare(id_vanzare, titlu, gen, pret, tip_reducere)
    result=lista_vanzari +[new_vanzare]
    save_to_file(result)
    return result

def remove_vanzare(lista_vanzari, id_vanzare):
    #verifica in functie de id daca vanzarea corespunde cu idul dat prin input iar daca corespunde este omisa din salvare in lista vanzari
    #param in:lista_vanzari, id_vanzare
    #param out:new_list
    new_list = []
    for vanzare in lista_vanzari:
        if get_id(vanzare) != id_vanzare:
            new_list.append(vanzare)
    save_to_file(new_list)
    return new_list

def update_vanzare(lista_vanzari, id_vanzare, titlu, gen, pret, tip_reducere):
    #updateaza o vanzare cautand o dupa id, daca nu corespunde ca id atunci o adauga dara daca corspunde o modifica in functie de preferinte daca nu se vrea a se schimba un parametru se lasa gol
    #param in: lista_vanzari, id_vanzare, titlu, gen, pret, tip_reducere
    #param out: vanzari_noi
    vanzari_noi=[]
    for vanzare in lista_vanzari:
        if get_id(vanzare)!=id_vanzare:
            vanzari_noi.append(vanzare)
        else:
            new_vanzare=create_vanzare(
                get_id(vanzare),
                titlu if titlu != '' else get_titlu(vanzare),
                gen if gen != '' else get_gen(vanzare),
                pret if pret != '' else get_pret(vanzare),
                tip_reducere if tip_reducere !='' else get_reducere(vanzare)
                )
            vanzari_noi.append(new_vanzare)
    save_to_file(vanzari_noi)
    return vanzari_noi

def reduce_pret(lista_vanzari, search_str, search_str2):
    #prin 2 stringuri se cauta ce se afla in tip_reducere daca coincid pretul este modificat conform reducerii
    #param in: lista_vanzari, search_str, search_str2
    #param out:lista_vanzar
    lista_vanzar=[]
    for vanzare in lista_vanzari:
        if search_str in get_reducere(vanzare):
            change=get_pret(vanzare)*9/10
            new_vanzare=create_vanzare(get_id(vanzare), get_titlu(vanzare),get_gen(vanzare),change,get_reducere(vanzare) )
            lista_vanzar.append(new_vanzare)

        if search_str2 in get_reducere(vanzare):
            changed=get_pret(vanzare)*95/100
            new_vanzare=create_vanzare(get_id(vanzare), get_titlu(vanzare),get_gen(vanzare),changed,get_reducere(vanzare) )
            lista_vanzar.append(new_vanzare)
    save_to_file(lista_vanzar)
    return lista_vanzar


def pret_minim_pe_gen(lista_vanzari):
    #pentru toate genurile se gaseste pretul minim folosind undictionar care salveaza genul si pt gen pretul minim
    #param in:lista_vanzari
    #param out: pret_gen
    pret_gen={}
    for vanzare in lista_vanzari:
        gen=get_gen(vanzare)
        pret=get_pret(vanzare)
        if gen in pret_gen:
            if get_pret(pret_gen[gen]) > pret:
                pret_gen[gen]=vanzare
        else:
            pret_gen[gen]=vanzare

    return pret_gen

def sorted_by_price(lista_vanzari):
    #sorteaza folosind functia sorted in python
    #param in:lista_vanzari
    #param out:lista_vanzari sortata
    def my_key(vanzare):
        return get_pret(vanzare)
    return sorted(lista_vanzari,key=my_key)

def number_of_titles_by_gen(lista_vanzari):
    #verifica prin getgen genul si verifiva de cate ori apare si numara titlurile
    #param in:lista_vanzari
    #param out:dictionar
    dictionar={}

    for vanzare in lista_vanzari:
        count=0
        gen=get_gen(vanzare)
        for vanzare in lista_vanzari:
           if gen==get_gen(vanzare):
               count=count+1
        dictionar[gen]=count

    return dictionar

def modify_titlu(lista_vanzari, gen, titlu):
    #se cauta dupa gen iar dupa modifica titlul cu o procedura asemanatoare celei de update
    #param in:lista_vanzari,gen,titlu
    #param out:vanzari_noi
    vanzari_noi=[]
    for vanzare in lista_vanzari:
        if get_gen(vanzare) != gen:
            vanzari_noi.append(vanzare)
        else:
            new_vanzare = create_vanzare(
                get_id(vanzare),
                titlu if titlu !='' else get_titlu(vanzare),
                get_gen(vanzare),
                get_pret(vanzare),
                get_reducere(vanzare)
            )
            vanzari_noi.append(new_vanzare)
    save_to_file(vanzari_noi)
    return vanzari_noi



























