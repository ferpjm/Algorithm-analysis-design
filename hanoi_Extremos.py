# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 11:21:41 2023

@author: Fernando
"""
def hanoi_Extremos(n, torreIzq=1, torreMed=2, torreDer=3):
   
    if n == 1:
        print("Mueve disco 1 desde torre", torreIzq, "a torre", torreMed)
        print("Mueve disco 1 desde torre", torreMed, "a torre", torreDer)
    else:
        hanoi_Extremos(n-1, torreIzq, torreMed, torreDer)
        print("Mueve disco", n, "desde torre", torreIzq, "a torre", torreMed)
        hanoi_Extremos(n-1, torreDer, torreMed, torreIzq)
        print("Mueve disco", n, "desde torre", torreMed, "a torre", torreDer)
        hanoi_Extremos(n-1, torreIzq, torreMed, torreDer)

n = int(input())
if(n<=9):
    hanoi_Extremos(n)

