

def BTTodas(solucion,x,y,k,mx,my,contadorSolucion):
    i=0
    while(i<8):
        #Sacamos la posicion a la que vamos segun donde estamos y el intento
        nueva_x=x+mx[i]
        nueva_y=y+my[i]
        #Puedo hacer esto solucion[nueva_x][nueva_y]=etapa???
        if (nueva_x>=0) and nueva_x<5 and nueva_y >=0 and nueva_y < 5 and solucion[nueva_x][nueva_y] == 0:
            solucion[nueva_x][nueva_y] = k
            if(k==25):
                print("solucion encontrada")
                imprimir(solucion)
                contadorSolucion[0]=contadorSolucion[0]+1
            else:
                BTTodas(solucion,nueva_x,nueva_y,k+1,mx,my,contadorSolucion)

            solucion[nueva_x][nueva_y] = 0
        i=i+1

def imprimir(solucion):
    for i in range (len(solucion)):
        for j in range (len(solucion[i])):
            print(solucion[i][j], end=" ")
        print("")

solucion=[]
dim=5
for i in range(dim):
    fila=[0]*dim
    solucion.append(fila)



solucion[2][2]=1
mx=[-2,2,-2,2,-1,1,-1,1]
my=[-1,-1,1,1,-2,-2,2,2]
contadorSolucion=[0]
BTTodas(solucion,2,1,2,mx,my,contadorSolucion)
print("Num de soluciones",contadorSolucion[0])