
def beker_a(i):
    szam:int=int(input(f"Kérek az {i}. páros számot!"))
    while szam % 2 != 0:
        szam:int=int(input(f"Ez nem páros szám!{i}. Páros számot kérek!"))
    return szam

def beker_b():
    lista=[]
    i:int=0
    while i < 3:
        kapott_szam=beker_a(i+1)
        lista.append(kapott_szam)
        i += 1
    legkisebb(lista)


def legkisebb(lista):
    i:int=0
    min:int=0
    while i < len(lista):
        if (lista[min]) > lista[i]:
            min=1
        i += 1

    print(f"{min+1}. lépésben adta meg a legkisebb páros számot, melynek érték: {lista[min]}")


