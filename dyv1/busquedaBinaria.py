def busquedaBinariaRec(a, elem, ini, fin):
    if (ini == fin):
        if (a[ini] == elem):
            return ini
        else:
            return -1
    else:
        medio = (ini + fin) // 2
        if (a[medio] == elem):
            return medio
        elif (a[medio] > elem):
            return busquedaBinariaRec(a, elem, ini, medio)
        else:
            return busquedaBinariaRec(a, elem, medio + 1, fin)


def busquedaBinaria(a, elem):
    return busquedaBinariaRec(a, elem, 0, len(a) - 1)


a = [2, 5, 8, 10]
elem = int(input())

print(busquedaBinaria(a, elem))