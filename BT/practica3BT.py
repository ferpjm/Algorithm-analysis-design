def lee_lista(n):
    a = []
    if n > 0:
        cadenaEntrada = input()
        for i in range(0, n):
            elemento = int(cadenaEntrada.split(" ")[i])
            a.append(elemento)

    return a


def divisores(guardados, etapa, elementos):
    menor = min(guardados)
    for i in range(len(guardados)):
        if guardados[i] != menor and guardados[i] % menor != 0:
            return False
    return True


def BT(elementos, solucion, etapa, m, guardados, contadorSolucion):

    for i in range (0,2):
        if len(guardados) < m:
            solucion[etapa] = i
            if i == 1:
                guardados.append(elementos[etapa])

            if len(guardados) == m and divisores(guardados, etapa, elementos):
                contadorSolucion[0] = contadorSolucion[0] + 1
            if etapa < len(elementos) - 1:
                BT(elementos, solucion, etapa + 1, m, guardados,
                   contadorSolucion)  # Llamada recursiva en cada iteración del bucle
            solucion[etapa] = 0
            if i == 1:
                guardados.pop()
        i += 1


guardados = []

n = int(input())
elementos = lee_lista(n)
m = int(input())
solucion = [None] * len(elementos)
contadorSolucion = [0]
BT(elementos, solucion, 0, m, guardados, contadorSolucion)
print(str(contadorSolucion[0]))
