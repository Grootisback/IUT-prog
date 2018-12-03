from random import *
def getrandomList (nb: int, mn: int, mx:int) -> list:
	return [randint(mn,mx) for i in range (nb)]

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
"""
for _ in range(10000):
	lst=getrandomList(nb=randint(0,15),mn=-100,mx=100)
	lst.sort()
	val=randint(-50,50)
	idx=IndexOfSorted(lst=lst,val=val)
	assert lst[idx]==val if idx!=-1 else val not in lst, f"{lst} : La position de {val} retourne {idx} qui semble faux"
	print('Tout est ok')
"""
def binarySearch(lst:list, val:int) ->int:
	result=-1
	ideb=0
	ifin=len(lst)-1
	while ideb<ifin:
		imilieu=ifin-ideb//2
		if val<=lst[imilieu]:
			ifin=imilieu-1
		else:
			ideb=imilieu+1
	if lst[ideb]==val:
		result=ideb
	elif lst[ifin]==val:
		result=ifin
	return result
print(binarySearch([1,2,4,5,9,10,22],5))
