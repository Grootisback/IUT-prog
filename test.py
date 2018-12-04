from random import *
"""
def getRandomList(nb : int, mn : int, mx : int) -> list:
    return [ randint(mn, mx) for i in range(nb)]

def indexOf(lst:list, val:int)->int:
	i=0
	ival=-1
	while ival==-1 and i<len(lst):
		if lst[i]==val:
			ival=i
		i=i+1
	return ival

def IndexOfSorted (lst:list,  val:int)-> int:
	i=0
	ival=-1
	if lst!=[] and val >=lst[0] and val >=lst[i]:
		if val==lst[i]:
			ival=i
		i=i+1
	else:
		print("la valeur",val,"n'est pas dans la liste")
	return ival

def binarySearch(lst:list, val:int) ->int:
	result=-1
	ideb=0
	ifin=len(lst)-1
	if val>lst[ideb] and val<lst[ifin]:
		while ideb<=ifin and result==-1:
			imilieu=ifin+ideb//2
			if val<=lst[imilieu]:
				ifin=imilieu-1
			else:
				ideb=imilieu+1
		if lst[ideb]==val:
			result=ideb
		elif lst[ifin]==val:
			result=ifin
		return result
print(binarySearch([1,2,4,5,9,10,22],1))

for _ in range(10_000):
    lst = getRandomList(nb=randint(0,15), mn=-randint(1,100), mx=randint(1,100))
    lst.sort()
    val = randint(-50, 50)
    idx = binarySearch(lst=lst, val=val)
    assert lst[idx]==val if idx!=-1 else val not in lst, f"{lst} : La position de {val} retourne {idx} qui semble incorrecte"
    print('tout est ok')
"""
def getReponse (val:int)->str:
	print("proposition de l'ordinateur : ",val)
	reponse=input("Est-ce, (E)gal, plus (G)rand ou plus (P)etit ? (tapez E, G ou P): ")
	reponse.capitalize()
	if reponse =="E" or reponse =="G" or reponse =="P":
		result=reponse
	else:
		print("saisie", reponse,"incorrecte, tapez E, G ou P")
		print(getReponse(val=val))
	return result
val=randint(0,100)
print(getReponse(val=val))

"""
Écrire la fonction getReponse qui reçoit en paramètre un entier val. Cette fonction affiche l'entier à l'écran et demande à l'utilisateur si le nombre qu'il a choisi est plus (P)etit, (E)gal ou plus (G)rand que celui affiché.

La fonction demande une réponse qui doit être 'P', 'E' ou 'G'. On reposera la question à l'utilisateur tant que ce dernier n'aura pas tapé l'une de ses trois lettres. On pourra lui épargner la mise en majuscule ! On acceptera donc aussi les lettres p, e et g.

La fonction retourne la saisie de l'utilisateur (chaîne de caractères) qui sera obligatoirement une chaîne parmi ('P', 'E' et 'G').

Exemple d'affichage :

Proposition de l'ordinateur : 12
Est-ce (E)gal, plus (G)rand ou plus (P)etit ? (tapez E, G ou P) : egal
Saisie EGAL incorrecte, tapez E, G ou P
Proposition de l'ordinateur : 12
Est-ce (E)gal, plus (G)rand ou plus (P)etit ? (tapez E, G ou P) : petit
Saisie PETIT incorrecte, tapez E, G ou P
Proposition de l'ordinateur : 12
Est-ce (E)gal, plus (G)rand ou plus (P)etit ? (tapez E, G ou P) : p
"""


def getReponse (val:int)->str:
    print("proposition de l'ordinateur : ",val)
    reponse=input("Est-ce, (E)gal, plus (G)rand ou plus (P)etit ? (tapez E, G ou P): ")
    reponse=reponse.capitalize()
    if reponse =="E" or reponse =="G" or reponse =="P":
        result=reponse
    else:
        print("saisie", reponse,"incorrecte, tapez E, G ou P")
        result=(getReponse(val=val))
    return result
val=randint(0,100)
print(getReponse(val=val))

"""
On veut écrire une fonction adapterIntervalle permettant d'ajuster l'intervalle de recherche en fonction de la réponse donnée par l'utilisateur.

Cette fonction reçoit donc en paramètre l'intervalle de départ interv sous la forme d'une liste de deux entiers (le premier étant la borne inférieure incluse, le second la borne supérieure incluse), ainsi que la valeur entière proposée val et la réponse de l'utilisateur rep ('P' ou 'G').

Cette fonction doit retourner les nouvelles bornes de l'intervalle de recherche. Or une fonction ne peut retourner qu'un seul objet. Une solution consiste à utiliser une liste et à placer les différents objets à retourner dans cette liste.

Python propose une autre solution : les Tuple (type tuple), qui seront vus prochainement en cours mais que vous avez déjà vu en Maths. Les Tuple sont des listes immuables (non modifiables). On utilise les parenthèses à la place des crochets pour les définir.
La syntaxe :

    a = (12, 23, "hello")
déclare un Tuple. Pour accéder aux éléments, on peut utiliser les crochets [] comme dans une liste.

Là encore, Python propose une autre syntaxe particulière :

    (n1, n2, s) = a
Dans cette syntaxe, la variable n1 reçoit la valeur du premier élément du Tuple (ici, 12), la variable n2 reçoit la valeur du second élément du Tuple (ici, 23) et la variable s reçoit la valeur du troisième élément du Tuple (ici, "hello").

Dans notre cas, la fonction adapterIntervalle retournera les nouvelles bornes de l'intervalle de recherche dans un Tuple. Si la variable rep ne contient ni 'P', ni 'G', la fonction retournera None.

Écrire la fonction adapterIntervalle.
 """
def adapterIntervalle (interv:list,val:int,rep:str)->list:
    if rep=='P':
        interv=[ val,interv[1]]
        result=interv
    elif rep=='G':
        interv=[interv[0],val]
        result=interv
    else:
        result=None
    return result
