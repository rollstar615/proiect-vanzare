def create_vanzare(id_vanzare, titlu, gen, pret, tip_reducere):
   # return{
    #    'id':id_vanzare,
     #   'titlu':titlu,
      #  'gen':gen,
      #  'pret':int(pret),
      #  'tip_reducere':tip_reducere
   # }
   return'{},{},{},{},{}'.format(id_vanzare,titlu,gen,float(pret),tip_reducere)

def get_id(vanzare):
    # gets the id of vanzare
    strVanzare=vanzare.split(",")
    return strVanzare[0]

def get_titlu(vanzare):
    #gets the titlu of vanzare
    strVanzare = vanzare.split(",")
    return strVanzare[1]

def get_gen(vanzare):
    #gets the gen of vanzare
    strVanzare = vanzare.split(",")
    return strVanzare[2]

def get_pret(vanzare):
    #gets the pret of vanzare
    strVanzare = vanzare.split(",")
    return float(strVanzare[3])

def get_reducere(vanzare):
    #gets the reducere of vanzare
    strVanzare = vanzare.split(",")
    return strVanzare[4]

def set_pret(vanzare, pretul):
    #sets the pret of vanzare
    vanzare= vanzare.split(",")
    vanzare[3]= float(pretul)
    return vanzare

def to_string(vanzare):
    #returns to string
    return '{}. {}: {} - pret: {} , {}'.format(
        get_id(vanzare),
        get_titlu(vanzare),
        get_gen(vanzare),
        get_pret(vanzare),
        get_reducere(vanzare),
    )



