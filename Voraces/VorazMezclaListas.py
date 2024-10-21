def voraz(tamListas):
    contadorOperaciones = 0
    while(len(tamListas)!=1):
        e1 = tamListas.pop(0)
        e2 = tamListas.pop(0)
        n=e1+e2
        contadorOperaciones=contadorOperaciones+n
        tamListas.append(n)
        tamListas=sorted(tamListas)
    return contadorOperaciones

numListas =  int(input(""))

tamListas=[]

linea = input("")
trozos = linea.split(" ")
for trozo in trozos:
    tamListas.append(int(trozo))


tamListas = sorted(tamListas)

print(tamListas)

numOperaciones = voraz(tamListas)

print(numOperaciones)