
def BT(bienes,solucion,etapa,valor1,valor2,totalValor):

    intento=1
    while intento<=2:
        #solucion[etapa]=intento??
        if (intento==1 and valor1[0] + bienes[etapa] <= totalValor//2) or (intento==2 and valor2[0] + bienes[etapa] <= totalValor//2):
            solucion[etapa]=intento
            if intento==1:
                valor1[0]=valor1[0]+bienes[etapa]

            if intento==2:
                valor2[0]=valor2[0]+bienes[etapa]

            if(etapa==len(bienes)-1):
                print(solucion)
            else:
                exito=BT(bienes,solucion,etapa+1,valor1,valor2,totalValor)

            solucion[etapa]= 0
            if intento == 1:
                    valor1[0] = valor1[0] - bienes[etapa]
            if intento == 2:
                    valor2[0] = valor2[0] - bienes[etapa]
        intento=intento+1



bienes=[40,20,25,5,10]
solucion=[0]*len(bienes)
valor1=[0]
valor2=[0]
totalValor=0
for bien in bienes:
      totalValor=totalValor +  bien

BT(bienes,solucion,0,valor1,valor2,totalValor)

