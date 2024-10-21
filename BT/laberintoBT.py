def contadorDeX(tablero):
    cont = 0
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if (tablero[i][j]=='X'):
                cont = cont +1
    return cont

def copiar(origen,destino):
    for i in range(len(origen)):
        for j in range(len(origen[i])):
            destino[i][j]=origen[i][j]


def BT(tablero,x,y,mx,my,tableroMejor,contadoresDeX):
    intento=0
    while(intento<=3) :
        nueva_x=x+mx[intento]
        nueva_y=y+my[intento]
        if nueva_x>= 0  and nueva_x < 10 and nueva_y>=0 and nueva_y<10 and (tablero[nueva_x][nueva_y]== ' ' or tablero[nueva_x][nueva_y]== 'S') and contadoresDeX[0]<contadoresDeX[1]:
            if(tablero[nueva_x][nueva_y]=='S'):
                #Comparo la solucion tablero con tableroMejor y si es mejor la cambio
                if(contadoresDeX[0]<contadoresDeX[1]):
                    print("Actualizamos solucion",contadoresDeX[0])
                    copiar(tablero,tableroMejor)
                    contadoresDeX[1] = contadoresDeX[0]


            else:
                tablero[nueva_x][nueva_y] = 'X'
                contadoresDeX[0]=contadoresDeX[0]+1
                BT(tablero, nueva_x, nueva_y, mx, my,tableroMejor,contadoresDeX)
                tablero[nueva_x][nueva_y] = ' '
                contadoresDeX[0] = contadoresDeX[0] - 1
        intento=intento+1


def imprimir(solucion):
    for i in range (len(solucion)):
        for j in range (len(solucion[i])):
            print(solucion[i][j], end="  ")
        print("")

tablero=[]
for i in range(10):
    fila=[' ']*10
    tablero.append(fila)
tableroMejor=[]
for i in range(10):
    fila=['X']*10
    tableroMejor.append(fila)

tablero[0][0]='E'
tablero[9][9]='S'
tablero[3][2]='M'
tablero[3][3]='M'
tablero[3][4]='M'
tablero[3][5]='M'
tablero[4][2]='M'
tablero[5][2]='M'
tablero[6][2]='M'
tablero[7][2]='M'

#La primera posición es el contador de X de tablero y la segunda es el contador de X de tableroMejor
contadoresDeX=[0,100]

mx=[0,0,1,-1]
my=[1,-1,0,0]
BT(tablero,0,0,mx,my,tableroMejor,contadoresDeX)

imprimir(tableroMejor)