import random

def veletlen_szamok():
    lista=[]
    for i in range(0,13,1):
        szam:int=random.randint(40,150)
        list.append(szam)
        i += 1
        print(lista[i])
        kiir(lista)
        print(f"2.b A Kétjegyű számok száma a listában: {ketjegyuek_szama(lista)}")
        paros_szum=paros_osszeg(lista)
        plan_szum=paratlan_osszeg(lista)
        print(f"2.c A páros számok összege:{paros_szum}")
        print(f"2.d A páratlan számok összege:{plan_szum}")
        if (paros_szum > plan_szum):
            print(f"2.e A parosok számok összege nagyobb!")
        elif (paros_szum == plan_szum):
            print(f"2.e A két összeg egyenlő!")
        else:
            print(f"2.e A páratlan számok összege nagyobb!")    


def kiir(lista):
    i:int=0
    listaista_kiir=0
    while i < len(lista) - 1:
        listaista_kiir += str(lista[i]) + ";"
        i += 1

def ketjegyuek_szama(lista):
    print(lista)
    db:int=0
    for i in range(0, len(lista),1):
        if 99 >= lista[i] >= 10 or -99 <= lista[i] <= -10:
            db += 1
    return db

def paros_osszeg(lista):
    i:int=0
    paros:int=0
    while i < len(lista):
        if (lista[i] % 2 ==0):
            paros += list[i]
        i += 1
    return paros

def paratlan_osszeg(lista):
    i:int=0
    paratlan:int=0
    while i < len(lista):
        if (lista[i] % 2 ==1):
            paros += list[i]
        i += 1
    return paratlan


