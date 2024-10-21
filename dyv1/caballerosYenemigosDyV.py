def DyV(enemigos, ini, fin, miFuerza):
    if ini > fin:
        return -1, 0

    if ini == fin:
        if enemigos[ini] <= miFuerza:
            return ini, enemigos[ini]
        else:
            return -1, 0

    mitad = (ini + fin) // 2
    pos1, suma1 = DyV(enemigos, ini, mitad, miFuerza)
    pos2, suma2 = DyV(enemigos, mitad + 1, fin, miFuerza)

    if pos1 == -1 and pos2 == -1:
        return -1, 0
    elif pos1 == -1:
        return pos2, suma2
    elif pos2 == -1:
        return pos1, suma1
    else:
        return pos2, suma1 + suma2


nenemigos = 7
enemigos = [1, 2, 3, 4, 5, 6, 7]
miFuerza = 10
ultimoIndiceAlQueGanamos, sumaGanados = DyV(enemigos, 0, len(enemigos) - 1, miFuerza)
print('Ganamos a', ultimoIndiceAlQueGanamos + 1, 'personajes')
print('La suma de los personajes a los que ganamos es:', sumaGanados)
