def imprimir(tablero):
    for i in range(len(tablero)):
        for j in range (len(tablero[i])):
            print(tablero[i][j],end=' ')
        print("")

def esFactible(solucion,etapa,intento):
    #Columna intento no tengamos otra X
    for fila in range(etapa):
        if(solucion[fila][intento]=='X'):
            return False
    #Comprobar diagonal 1
    fila=etapa-1
    columna=intento-1
    while(fila>=0) and (columna>=0):
        if(solucion[fila][columna]=='X'):
            return False
        fila=fila-1
        columna=columna-1

    #Comprobar diagonal 2
    fila = etapa - 1
    columna = intento + 1
    while (fila >= 0) and (columna <= 7):
        if (solucion[fila][columna] == 'X'):
            return False
        fila = fila - 1
        columna = columna + 1
    return True


def BT(solucion,etapa):
    exito=False
    intento=0
    while(intento<8) and not exito:
        if esFactible(solucion,etapa,intento):
            solucion[etapa][intento]='X'

            if(etapa==7):
                exito=True
            else:
                exito=BT(solucion,etapa+1)
            if not exito:
                solucion[etapa][intento] = '-'
        intento=intento+1
    return exito

solucion=[]

for i in range(8):
    fila=['-']*8
    solucion.append(fila)

exito=BT(solucion,0)
if(exito):
    imprimir(solucion)
else:
    print("No hay solucion")