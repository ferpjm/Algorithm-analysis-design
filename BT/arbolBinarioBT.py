# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 14:21:00 2023

@author: Fernando
"""
def lee_lista(n):
    a = []
    if n > 0:
        cadenaEntrada = input()
        for i in range(0, n):
            elemento = int(cadenaEntrada.split(" ")[i])
            a.append(elemento)

    return a


def genera_subconjuntos_wrapper(elementos, m):
    sol = [None] * (len(elementos))
    contador = genera_subconjuntos(0, sol,[], elementos, 0, m)
    return contador


def es_divisible(subconjunto, elementos):
    # Comprueba si el menor elemento de la subcolección es un divisor de los m-1 elementos restantes
    subcoleccion = [elementos[i] for i in range(len(subconjunto)) if subconjunto[i] == 1]
    menor = min(subcoleccion)
    for num in subcoleccion:
        if num != menor and num % menor != 0:
            return False
    return True



def elementos_en_subconjunto(subconjunto, elementos):
    indices = [i for i in range(len(subconjunto)) if subconjunto[i] == 1]
    nueva_lista = [elementos[i] for i in indices]
    return nueva_lista


def genera_subconjuntos(i, sol,sol_parcial, elementos, contador, m):
    # Caso base: solución parcial completa
    if i == len(elementos):
        if sum(1 for x in sol if x == 1) == m:
            if es_divisible(sol, elementos):
                contador += 1
    else:
        for k in range(0, 2):
            if sol_parcial == [] or sol:
                sol[i] = k
                sol_parcial = elementos_en_subconjunto(sol, elementos)
                contador = genera_subconjuntos(i+1, sol,sol_parcial, elementos, contador, m)
    return contador






n = int(input())
elementos = lee_lista(n)
m = int(input())
print(genera_subconjuntos_wrapper(elementos,m))