def imprimir(solucion):
    for i in range (len(solucion)):
        for j in range (len(solucion[i])):
            print(solucion[i][j], end="  ")
        print("")

def BT(tablero,x,y,n,numMagico,sumaFilas,sumaColumnas,sumaDiagonales,usados):
    exito=False
    intento=1
    while (intento<=n*n) and not exito:
        if(not usados[intento-1] and
                ((y==n-1 and sumaFilas[x]+intento==numMagico) or (y<n-1 and sumaFilas[x]+intento<numMagico))and
                ((x==n-1 and sumaColumnas[y]+intento==numMagico) or (x<n-1 and sumaColumnas[y]+intento<numMagico)) and
                ((x!=y) or (x==y and y!=n-1) or(x==y and y==n-1 and sumaDiagonales[0]+intento==numMagico)) and
                ((x+y!=n-1) or (x+y==n-1 and y!=0) or ( x + y ==n-1 and y == 0 and sumaDiagonales[1] + intento == numMagico))
        ):
            usados[intento - 1]=True
            tablero[x][y]= intento
            sumaFilas[x]=sumaFilas[x]+intento
            sumaColumnas[y]=sumaColumnas[y]+intento
            if(x==y):
                sumaDiagonales[0]=sumaDiagonales[0]+ intento

            if(x+y==n-1):
                sumaDiagonales[1] = sumaDiagonales[1] + intento

            if(x==n-1) and (y==n-1):
                exito=True
            else:
                if (y < n - 1):
                    nuevaX = x
                    nuevaY = y + 1
                else:
                    nuevaX = x + 1
                    nuevaY = 0
                exito=BT(tablero,nuevaX,nuevaY,n,numMagico,sumaFilas,sumaColumnas,sumaDiagonales,usados)
            if not exito:
                usados[intento - 1] = False
                tablero[x][y] = 0
                sumaFilas[x] = sumaFilas[x] - intento
                sumaColumnas[y] = sumaColumnas[y] - intento
                if (x == y):
                    sumaDiagonales[0] = sumaDiagonales[0] - intento
                if (x + y == n - 1):
                    sumaDiagonales[1] = sumaDiagonales[1] - intento
        intento=intento+1
    return exito


n=int(input())
numMagico= int(n*(((n*n)+1)/2))
print(numMagico)
tablero=[]
for i in range(n):
    fila=[0]*n
    tablero.append(fila)

usados=[False]*(n*n)
sumaFilas=[0]*n
sumaColumnas=[0]*n
sumaDiagonales=[0,0]


exito=BT(tablero,0,0,n,numMagico,sumaFilas,sumaColumnas,sumaDiagonales,usados)

if exito:
    imprimir(tablero)