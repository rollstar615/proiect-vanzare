from domain import get_id, get_titlu, get_gen, get_pret, get_reducere, create_vanzare
from logic import add_vanzare, remove_vanzare, get_vanzare_by_id, update_vanzare, reduce_pret, pret_minim_pe_gen, sorted_by_price, number_of_titles_by_gen,modify_titlu



def test_add():
    lista_vanzari = []
    params = [3, 'jdshfjsbj', 'abc', 24, 'gold']
    lista_vanzari= add_vanzare(lista_vanzari, *params)
    assert get_id(lista_vanzari[-1]) == params[0]
    assert get_titlu(lista_vanzari[-1]) == params[1]
    assert get_gen(lista_vanzari[-1]) == params[2]
    assert get_pret(lista_vanzari[-1]) == params[3]

def test_update():
    p1 = create_cake(1, 'a', 'b', 200, 'gold')
    p2 = create_cake(13, 'b', 'd', 300, 'silver')
    p3 = create_cake(6, 'c', 'e', 400, 'gold')
    update_id = get_id(p3)
    update_name = 'cristi'
    update_desc = ''
    update_price = '149'
    vanzari = [p1, p2, p3]
    new_vanzare = update_vanzare(vanzari, update_id, update_name, update_desc, update_price, 'gold')
    updated_vanzare = get_vanzare_by_id(new_vanzare, update_id)
    assert get_titlu(updated_vanzare) == update_name
    assert get_gen(updated_vanzare) == get_gen(p3)
    assert get_pret(updated_vanzare) == int(update_price)


def test_domain():
    c1 = create_vanzare(4, 'asdf', 'asdff', 30, 'silver')
    assert get_id(c1) == 4
    assert get_titlu(c1) == 'asdf'
    assert get_gen(c1) == 'asdff'


def test_titluri_vanzare():
    p1 = create_vanzare(1, 'a', 'b', 200, 'gold')
    p2 = create_vanzare(13, 'b', 'd', 300, 'silver')
    p3 = create_vanzare(6, 'c', 'e', 400, 'gold')
    update_id = get_id(p3)
    update_name = 'a'
    update_desc = ''
    update_price = '149'
    vanzari = [p1, p2, p3]
    new_vanzare = update_vanzare(vanzari, update_id, update_name, update_desc, update_price, 'gold')
    updated_vanzare = get_vanzare_by_id(new_vanzare, update_id)
    assert get_titlu(updated_vanzare) == update_name
    assert get_gen(updated_vanzare) == get_gen(p3)
    assert get_pret(updated_vanzare) == int(update_price)



def test_reduce_pret():
    p1 = create_vanzare(1, 'a', 'b', 200, 'gold')
    p2 = create_vanzare(13, 'b', 'b', 200,'silver')
    p3 = create_vanzare(6, 'c', 'e', 200, 'gold')
    search_str=gold
    search_str2=silver
    vanzari = [p1, p2, p3]
    assert reduce_pret(vanzari, search_str,search_str2) == [(1,'a','b',180,'gold'),(13,'b','b',190,'silver'),(6,'c','e',180,'gold')]

def test_pret_minim_gen():
    p1 = create_vanzare(1, 'a', 'b', 200, 'gold')
    p2 = create_vanzare(13, 'b', 'b', 150, 'silver')
    p3 = create_vanzare(6, 'c', 'b', 100, 'gold')
    gen='b'
    vanzari=[p1,p2,p3]
    assert pret_minim_pe_gen(vanzari, gen)==[p3]

def test_sortare():
    p1 = create_vanzare(1, 'a', 'b', 200, 'gold')
    p2 = create_vanzare(13, 'b', 'b', 150, 'silver')
    p3 = create_vanzare(6, 'c', 'b', 100, 'gold')
    vanzari=[p1,p2,p3]
    assert sorted_by_price(vanzari)==[p3,p2,p1]

def test_modify():
    p1 = create_vanzare(1, 'a', 'b', 200, 'gold')
    p2 = create_vanzare(13, 'b', 'w', 150, 'silver')
    p3 = create_vanzare(6, 'c', 'd', 100, 'gold')
    vanzari=[p1,p2,p3]
    gen='b'
    titlu='eu'
    assert modify_titlu(vanzari,gen,titlu)==[(1,'eu','b',200,'gold'),(13,'b','w',150,'silver'),(6,'c','d',100,'gold')]

test_add()
test_reduce_pret()
test_update()
test_titluri_vanzare()
test_pret_minim_gen()
test_sortare()
test_modify()
test_domain()

