from random import *

def getRandomList(nb : int, mn : int, mx : int) -> list:
    return [ randint(mn, mx) for i in range(nb)]

def __compare__(l:list, s:set) -> bool:
    return len(l)==len(s) and len([ v for v in l if not v in s])==0