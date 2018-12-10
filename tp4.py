from random import *

def getRandomList(nb : int, mn : int, mx : int) -> list:
    return [ randint(mn, mx) for i in range(nb)]

def __compare__(l:list, s:set) -> bool:
    return len(l)==len(s) and len([ v for v in l if not v in s])==0


    def getRegularArray2d (nl:int, nc:int, mn:int, mx:int)->list:
    lst=[]
    for i in range(nl):
        ligne=[]
        for i2 in range (nc):
            ligne.append(randint(mn,mx))
        lst.append(ligne)
    return lst
    print(getRegularArray2d(3,5,2,100))