
def codificar(coordenadas):
    st = []
    if isinstance(eval(coordenadas),list):
        lista_coord = eval(coordenadas)
        for index, coord in enumerate(lista_coord):
            if(index!=len(lista_coord)-1):
                st.extend((str(coord[0]),'#',str(coord[1]),'@'))
            else:
                st.extend((str(coord[0]),'#',str(coord[1])))
    return ''.join(st)

def decodificar(coordenadas):
    list = []
    for coord in coordenadas.split('@'):
        lat,long = coord.split('#')
        list.append({'lat':lat,'long':long})

    return list