def esFactible(tablero,etapaX,etapaY,intento):
    #vamos a comprobar que no hay otro numero igual a intento en la misma fila
    for i in range(N):
        if(tablero[etapaX][i]==intento):
            return False
        if (tablero[i][etapaY] == intento):
            return False
    return True


def imprimir(solucion):
    for i in range (len(solucion)):
        for j in range (len(solucion[i])):
            print(solucion[i][j], end="  ")
        print("")

def dameCuadrantePosicion(etapaX,etapaY):
    if (etapaX<3):
        if(etapaY<3):
            return 0
        elif(etapaY<6):
            return 1
        else:
            return 2
    elif(etapaX<6):
        if (etapaY < 3):
            return 3
        elif (etapaY < 6):
            return 4
        else:
            return 5
    else:
        if (etapaY < 3):
            return 6
        elif (etapaY < 6):
            return 7
        else:
            return 8

def BTSudoku(tablero,etapaX,etapaY,usadosEnFila,usadosEnColumna,usadosEnCuadrante):
    if(tablero[etapaX][etapaY]!=0):
        if (etapaX == N - 1) and (etapaY == N - 1):
            exito = True
        else:
            if (etapaY < N - 1):
                nuevaEtapaX = etapaX
                nuevaEtapaY = etapaY + 1
            else:
                nuevaEtapaX = etapaX + 1
                nuevaEtapaY = 0
            exito = BTSudoku(tablero, nuevaEtapaX, nuevaEtapaY, usadosEnFila, usadosEnColumna, usadosEnCuadrante)
        return exito
    else:
        exito=False
        intento=1
        while(intento<=N) and not exito:
            #tablero[etapaX][etapaY]=intento????
            cuadrante = dameCuadrantePosicion(etapaX,etapaY)

            if not usadosEnFila[etapaX][intento-1] and not usadosEnColumna[etapaY][intento-1] and not usadosEnCuadrante[cuadrante][intento-1]:
                tablero[etapaX][etapaY] = intento
                usadosEnFila[etapaX][intento-1]=True
                usadosEnColumna[etapaY][intento - 1] = True
                usadosEnCuadrante[cuadrante][intento-1]=True

                if(etapaX==N-1) and (etapaY==N-1):
                    exito=True
                else:
                    if(etapaY<N-1):
                        nuevaEtapaX=etapaX
                        nuevaEtapaY=etapaY+1
                    else:
                        nuevaEtapaX=etapaX+1
                        nuevaEtapaY=0
                    exito=BTSudoku(tablero,nuevaEtapaX,nuevaEtapaY,usadosEnFila,usadosEnColumna,usadosEnCuadrante)
                if not exito:
                    tablero[etapaX][etapaY]=0
                    usadosEnFila[etapaX][intento - 1] = False
                    usadosEnColumna[etapaY][intento - 1] = False
                    usadosEnCuadrante[cuadrante][intento - 1] = False
            intento=intento+1
        return exito



N=9

tablero=[]
for i in range(N):
    fila=[0]*N
    tablero.append(fila)

usadosEnFila=[]
usadosEnColumna=[]
usadosEnCuadrante=[]
for i in range(N):
    fila=[False]*N
    usadosEnFila.append(fila)

for i in range(N):
    fila=[False]*N
    usadosEnColumna.append(fila)
for i in range(N):
    fila=[False]*N
    usadosEnCuadrante.append(fila)

exito=BTSudoku(tablero,0,0,usadosEnFila,usadosEnColumna,usadosEnCuadrante)

if exito:
    imprimir(tablero)