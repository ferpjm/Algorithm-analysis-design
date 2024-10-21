def imprimir(solucion):
    for i in range (len(solucion)):
        for j in range (len(solucion[i])):
            print(solucion[i][j], end="  ")
        print("")




def BT(solucion,etapaX,etapaY,usados,sumaFilas,sumaColumnas):
   exito=False
   intento=1
   while (intento<=9) and not exito:
       if not usados[intento-1] and ((etapaY<2) or (etapaY==2 and sumaFilas[etapaX]+intento==15))\
               and ((etapaX<2) or (etapaX==2 and sumaColumnas[etapaY]+intento==15)):
           solucion[etapaX][etapaY] = intento
           usados[intento-1]=True
           sumaFilas[etapaX]=sumaFilas[etapaX] + intento
           sumaColumnas[etapaY]=sumaColumnas[etapaY] + intento
           if (etapaX == 2) and (etapaY == 2):
               exito = True
           else:
               if (etapaY < 2):
                   nuevaEtapaX = etapaX
                   nuevaEtapaY = etapaY + 1
               else:
                   nuevaEtapaX = etapaX + 1
                   nuevaEtapaY = 0
               exito = BT(solucion,nuevaEtapaX,nuevaEtapaY,usados,sumaFilas,sumaColumnas)
           if not exito:
               solucion[etapaX][etapaY] = 0
               usados[intento-1]=False
               sumaFilas[etapaX] = sumaFilas[etapaX] - intento
               sumaColumnas[etapaY] = sumaColumnas[etapaY] - intento
       intento=intento+1
   return exito


solucion=[]
for i in range(3):
    fila=[0]*3
    solucion.append(fila)

usados=[False]*9
sumaFilas=[0]*3
sumaColumnas=[0]*3


exito=BT(solucion,0,0,usados,sumaFilas,sumaColumnas)

if exito:
    imprimir(solucion)
