from random import *

def getRandomList(nb : int, mn : int, mx : int) -> list:
    return [ randint(mn, mx) for i in range(nb)]

def __compare__(l:list, s:set) -> bool:
    return len(l)==len(s) and len([ v for v in l if not v in s])==0


    def getRegularArray2d (nl:int, nc:int, mn:int, mx:int)->list:
    lst=[]
    for i in range(nl):
        ligne=[]
        for j in range (nc):
            ligne.append(randint(mn,mx))
        lst.append(ligne)
    return lst
    print(getRegularArray2d(3,5,2,100))

#verif du code#
    for i in range (10000):
    	nl=randint(1,10)
    	nc=randint(1,10)
    	tableau= getRegularArray2d(nl=nl,nc=nc,mn=-10,mx=10)
    	assert len(tableau)==nl, "Le nombre d'éléments presents dans les lignes n'est pas correct"
    	for j in range (nl):
        	assert len (tableau[i2])==nc, "le nombre d'élements présents dans les colonnes n'est pas le bon"
print("Tout est ok")

