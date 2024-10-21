def imprimir(tiposDeMoneda,solucion):
    for i in range(len(tiposDeMoneda)):
        print(solucion[i],"Unidades de valor:", tiposDeMoneda[i])

def voraz(tiposDeMoneda, cambio, solucion):
    index=0
    while(cambio>0) and index<len(tiposDeMoneda):
        if cambio>=tiposDeMoneda[index]:
            solucion[index]+=1
            cambio=cambio-tiposDeMoneda[index]
        else:
            index=index+1
linea= input("")
trozos = linea.split(" ")
tiposDeMoneda= []
for trozo in trozos:
    tiposDeMoneda.append(int(trozo))
cambio = int(input(""))
solucion = [0]*len(tiposDeMoneda)

voraz(tiposDeMoneda,cambio,solucion)

imprimir(tiposDeMoneda,solucion)


#100 50 20 10 5 2 1