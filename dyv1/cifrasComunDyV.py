def extraerCifras(numero):
    solucion = [False] * 10
    while (numero > 0):
        cifra = numero % 10
        numero = numero // 10
        solucion[cifra] = True
    return solucion
def combinar(sol1, sol2):
    solucion = [False] * 10
    for i in range(len(sol1)):
        if (sol1[i] == True) and (sol2[i] == True):
            solucion[i] = True
    return solucion
def DyV(numeros, ini, fin):
    if (ini == fin):
        # CONQUISTA
        solucion = extraerCifras(numeros[ini])
        return solucion
    else:
        # DIVISION
        medio = (ini + fin) // 2
        solucion1 = DyV(numeros, ini, medio)
        solucion2 = DyV(numeros, medio + 1, fin)
        # COMBINACION
        solucion = combinar(solucion1, solucion2)
        return solucion


numeros = [2348,1349,7523,3215]
solucion = DyV(numeros, 0, len(numeros) - 1)

for i in range(len(solucion)):
    if(solucion[i]):
        print("Cifra en comun:", i)

