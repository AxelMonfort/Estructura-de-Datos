from claseArbol import Arbol

if __name__ == '__main__':
    arbol = Arbol(70)
    arbol.Agregar(47)
    arbol.Agregar(92)
    arbol.Agregar(35)
    arbol.Agregar(68)
    arbol.Agregar(83)
    arbol.Agregar(100)
    arbol.Agregar(79)
    #arbol.InOrden()
    arbol.PreOrden()
    #arbol.PostOrden()
    dato = arbol.Buscar(6)
    if dato != None:
        print('\nSe encontro el dato ',dato)
    else:
        print('\nNo esta ese dato.')

    nivel = arbol.Nivel(100)
    if nivel != None:
        print('\nEl nivel es: ',nivel)
    else: print('\nÁrbol vacío.')

    arbol.Hoja(100)

    altura = arbol.Altura()
    print('\n'f"Altura: {altura}")

    arbol.Hijo(79,83)

    arbol.Camino(68)
    arbol.Suprimir(70)
    arbol.PreOrden()