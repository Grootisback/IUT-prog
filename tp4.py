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

def getMin(tab:list)->int:
    minimum=min(tab[0])
    for i in range (1,len(tab)):
        if min(tab[i])<minimum:
            minimum=min(tab[i])
    return minimum
    print(getMin(tab = [ [ 2, 1, 3], [ 6, 9 ], [ 0, 8, 1, 2 ]])) # Doit afficher 0

    def getMax(tab:list)->int:
    maximum=max(tab[0])
    for i in range (1,len(tab)):
        if max(tab[i])>maximum:
            maximum=max(tab[i])
    return maximum
    print(getMax(tab = [ [ 2, 1, 3], [ 6, 9 ], [ 0, 8, 1, 2 ]])) # Doit afficher 9

    for i in range (10000):
    nl=randint(1,10)
    nc=randint(1,10)
    mn=randint(-20,-5)
    mx=randint(5,20)
    tableau=getRegularArray2d(nl=nl,nc=nc,mn=mn,mx=mx)
    minimum=getMin(tab=tableau)
    maximum=getMax(tab=tableau)
    assert minimum<=mx and minimum>=mn,"la valeur minimale n'est pas comprise entre le max et le min "
    assert maximum<=mx and maximum>=mn,"la valeur maximale n'est pas comprise entre me max et le min"
print("tout est ok")

def getPosMin(tab:list):
    minimum=min(tab[0])
    ligneMin=0
    colMin=tab[0].index(minimum)
    for i in range (1,len(tab)):
        if min(tab[i])<minimum:
            minimum=min(tab[i])
            colMin=tab[i].index(minimum)
            ligneMin=i
    ligne,col=(ligneMin, colMin)
    return (ligne,col)
    print(getPosMin(tab = [ [ 2, 1, 3], [ 6, 9 ], [ 0, 8, 1, 2 ]])) # Doit afficher (2,0)

def getCarre2d (n:int)->list:
lst=[]
for i in range(n):
    ligne=[]
    for j in range (n):
        ligne.append(randint(1,n**2))
    lst.append(ligne)
return lst
print(getCarre2d(5))

def getSommeLignes(tab:list)->list:
    lstsom=[]
    for i in range(len(tab)):
        lstsom.append(sum(tab[i]))
    return lstsom
print(getSommeLignes( tab = [ [ 2, 1, 6 ], [ 4, 8, 9 ], [ 3, 5, 7 ] ] )) # doit afficher [ 9, 21, 15]
def getSommeColonnes(tab=list)->list:
    lstsom=[]
    for i in range(len(tab)):
        somme=0
        for j in range(len(tab)):
            somme+=tab[j][i]
        lstsom.append(somme)
    return lstsom
print(getSommeColonnes( tab = [ [ 2, 1, 6 ], [ 4, 8, 9 ], [ 3, 5, 7 ] ] )) # doit afficher [ 9, 14, 22 ]

def getSommeDiagonale1(tab:list)->int:
    somme=0
    for i in range(len(tab)):
        somme+=tab[i][i]
    return somme
print(getSommeDiagonale1( tab = [ [ 2, 1, 6 ], [ 4, 8, 9 ], [ 3, 5, 7 ] ] )) # doit afficher 17

def getSommeDiagonale2(tab:list)->int:
    somme=0
    for i in range(len(tab)):
        somme+=tab[i][len(tab)-1-i]
    return somme
print(getSommeDiagonale2( tab = [ [ 2, 1, 9 ], [ 4, 8, 6 ], [ 3, 5, 7 ] ] )) # doit afficher 20

def AffichageCarreMagique(tab:list)->None:
    sommelignes=getSommeLignes(tab)
    sommecol=getSommeColonnes(tab)
    sommediag1=getSommeDiagonale1(tab)
    sommediag2=getSommeDiagonale2(tab)
    sep=("+---")*len(tab)+'+'
    sep2="|"
    for i in range(len(tab)):
        print(f"{sep:>{len(sep)+2}}")
        print(' ', end='')
        for j in range(len(tab)):
            print(f"{sep2:^3}", end='')
            print(tab[i][j], end='')   
        print(f"{sep2:^3}", end='')
        print(sommelignes[i])
    print(sommediag1, end='  ')
    for j in range(len(tab)):
        print(sommecol[j], end='  ')
    print(' ',sommediag2)
    return None
print(AffichageCarreMagique([ [ 2, 1, 9 ], [ 4, 8, 6 ], [ 3, 5, 7 ] ]))

