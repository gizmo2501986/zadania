# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 07:56:04 2020

@author: Ewa Figielska
"""
import time
from operator import itemgetter
from copy import deepcopy
from random import randrange

def procedura_generowania_wszystkich_podzbiorow(b, a, c):
    # tworzenie pozbiorow za pomoca kodu Grey'a
    # patrz Lipski, "Kombinatoryka dla programistow"
    t1 = time.time()
    n = len(c)
    zysk = 0  # calkowity zysk
    tmp_zysk, tmp_naklady = 0, 0  # zmienne pomocnicze
    podzbior = [0 for i in range(n)]

    p, k = 0, 0  #k =liczba dotychczas wygenerowanych podzbiorow
    while True:
        
        if k:  #jezeli podzbior nie jest pusty
            if podzbior[p]:  # jezeli projekt p zostal dodany do podzbioru
                tmp_naklady += a[p]
                tmp_zysk += c[p]
            else:  # jeżeli projet p zostal wylaczony z podzbioru
                tmp_naklady -= a[p]
                tmp_zysk -= c[p]
    
            if tmp_naklady <= b:  #czy stworzony podzbior jest dopuszczalny?
                if tmp_zysk > zysk:  #czy calkowity zysk dla tego podzbioru > najwiekszego zysku znalezionego do tej pory? 
                    zysk  = tmp_zysk  # aktualizacja calkowitego zysku

        p, k = 0, k+1
        j = k
        while j%2 == 0:
            j, p = j // 2, p + 1
        if p<n:
            podzbior[p] = 1-podzbior[p]
        if p >= n:
            break
    t2 = time.time()
    return zysk, t2 - t1


def procedura_programowania_dynamicznego(b, a, c):
    t1 = time.time()
    n = len(c)
    zysk = [[0 for i in range(b+1)] for p in range(n)]
    for i in range(a[0], b+1):
        zysk[0][i] = c[0]
    for p in range(1, n):  # p - indeks projektu
        for i in range(1, b+1):
            zysk[p][i] = zysk[p-1][i]
            if a[p] <= i:
                if zysk[p-1][i-a[p]] + c[p] > zysk[p][i]:
                    zysk[p][i] = zysk[p-1][i-a[p]] + c[p]
    t2 = time.time()
    return zysk[n-1][b], t2 - t1


def procedura_zachlanna(b, a, c):
    t1 = time.time()
    n = len(c)
    zysk, naklady = 0, 0
    podzbior = []
    lista = [(i, c[i]/a[i]) for i in range(n)]
    lista = sorted(lista, key = itemgetter(1), reverse = True)
    for elem in lista:
        if naklady + a[elem[0]] <= b:  #sprawdzenie, czy po dolaczeniu nowego projektu bedzie spelnione ograniczenie na budzet
            naklady += a[elem[0]]
            zysk += c[elem[0]]
            podzbior.append(elem[0]+1)
    t2 = time.time()
    return zysk, t2 - t1

a = [4, 4, 4, 2]
c = [2, 7, 9, 5]
b = 8


zysk, czas = procedura_generowania_wszystkich_podzbiorow(b, a, c)
print(zysk, czas)
zysk, czas = procedura_programowania_dynamicznego(b, a, c)
print(zysk, czas)
zysk, czas = procedura_zachlanna(b, a, c)
print(zysk, czas)

