#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ezCLI import testcode

"""
Axiomes à vérifier : cf L2 ASD
A1 est_vide(creer()) = VRAI
A2 est_vide(ajouter(x, f)) = FAUX
A3 premier(ajouter(x, creer())) = x
A4 premier(ajouter(x, f)) = premier(f)
A5 enlever(ajouter(x, f)) = ajouter(x, enlever(f)) si non est_vide(f)
A6 enlever(ajouter(x, creer())) = creer()

longueur et to_list
B1: longueur(creer()) = 0
B2: longueur(enlever(f)) = longueur(f) -1
B3: longueur(ajouter(x, f)) = longueur(f) +1
B4: longueur(to_list(f)) = longueur(f)
B5: to_list(f)[0] = premier(f)
B6: to_list(ajouter(x, f))[-1] = x
"""

class QNode:
    """ un element pour la liste chainee """
    __slots__ = ('__item', '__next')
    def __init__(self, value:any):
        self.__item = value
        self.__next = None

    def __repr__(self) -> str:
        return "{0.__class__.__name__}({0.item})".format(self)
    def __str__(self) -> str:
        return "item: {0.item}, next: {0.next}".format(self)
    
    @property
    def item(self) -> any:
        """ protection en ecriture """
        return self.__item
    @property
    def next(self) -> 'QNode or None':
        """ accesseur en lecture """
        return self.__next
    @next.setter
    def next(self, other:'QNode'):
        """ accesseur en ecriture, on controle quoi et si on met """
        if isinstance(other, QNode) or other is None:
            self.__next = other

class SQueue:
    """ une liste chainee servant de file (FIFO: First In, First Out) 
        utilisation de deux sentinelles pour les acces

        hq: head of the queue (the first element)
        tq: tail of the queue (the last element)
        count: number of element in the queue
    """
    __slots__ = ('__hq', '__tq', '__count')
    def __init__(self):
        """ creation d'une file vide """
        self.__hq = self.__tq = None
        self.__count = 0

    def __len__(self) -> int:
        """ nombre d'elements """
        return self.__count

    def push(self, value:any):
        """ ajout d'un element en fin """
        _node = QNode(value)
        self.__count += 1
        if self.empty(): # cas file vide
            self.__hq = self.__tq = _node
        else: # cas file non vide
            self.__tq.next = _node # ajout
            self.__tq = self.__tq.next # deplacement de la sentinelle

    def pop(self):
        """ suppression d'un element fonction partielle 
        require: file non vide
        """
        _node = self.__hq
        self.__hq = self.__hq.next # deplacement de la sentinelle
        self.__count -= 1

    def first(self) -> any:
        """ permet d'obtenir l'information du premier element 
        fonction partielle
        require: file non vide
        """
        return self.__hq.item

    def empty(self) -> bool:
        """ savoir si la file est vide """
        return self.__hq is None

    def to_list(self) -> list:
        """ renvoie la liste python des informations """
        _current = self.__hq # curseur de parcours
        _store = [] # structure de stockage
        while _current is not None:
            _store.append(_current.item)
            _current = _current.next
        return _store
    
if __name__ == "__main__":
    code = """
# creation file vide
q = SQueue()
q.empty() == True # A1
len(q) == 0       # B1

# push
pre = len(q)
q.push(1)
post = len(q)
post == pre + 1 # B3
q.empty() == False # A2

# pop
pre = len(q)
q.pop()
post = len(q)
post == pre -1 #B2

q = SQueue()
q.push(17)
q.first() == 17 # A3

q.empty() == False
q.push(-1)
q.first() == 17 # A4
q.push(-7)
q.first() == 17 # A4

# push(x, pop(q)) = pop(push(x, q))
q1 = SQueue()
for _ in range(5): q1.push(_)
q2 = SQueue()
for _ in range(5): q2.push(_)
q1.to_list() == q2.to_list()
q1.pop()
q1.push(42)
q2.push(42)
q2.pop()
q1.to_list() == q2.to_list() # A5

# len
q1.push(13)
q2.pop()
len(q.to_list()) == len(q)   # B4
len(q1.to_list()) == len(q1) # B4
len(q2.to_list()) == len(q2) # B4

# first
q.first() == q.to_list()[0]   # B5
q1.first() == q1.to_list()[0] # B5
q2.first() == q2.to_list()[0] # B5

# push/to_list
q.push(23)
q.to_list()[-1] == 23  # B6
q1.push(13)
q1.to_list()[-1] == 13 # B6
q2.push(31)
q2.to_list()[-1] == 31 # B6


""" ; testcode(code)
