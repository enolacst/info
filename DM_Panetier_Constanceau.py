#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "CONSTANCEAU Enola & PANETIER Camille"
__date__ = "06.12.20"
__usage__ = "Manipulation file avec priorité"

"""
QUEUE :File avec priorité
une liste chainee servant de file (FIFO: First In, First Out) 
    utilisation de deux sentinelles pour les acces

    hq: head of the queue (the first element)
    tq: tail of the queue (the last element)
    count: number of element in the queue
"""
"""
Axiomes à vérifier : cf L2 ASD
A1 est_vide(creer()) = VRAI
A2 est_vide(ajouter(x, f)) = FAUX
A3 premier(ajouter(x, creer())) = x
A4 premier(ajouter(x, f)) = premier(f)
A5 enlever(ajouter(x, f)) = ajouter(x, enlever(f)) si non est_vide(f)
A6 enlever(ajouter(x, creer())) = creer()
A7 max_priority(creer(n))== n

longueur et to_list
B1: longueur(creer()) = 0
B2: longueur(enlever(f)) = longueur(f) -1
B3: longueur(ajouter(x, f)) = longueur(f) +1
B4: longueur(to_list(f)) = longueur(f)
B5: to_list(f)[0] = premier(f)
B6: to_list(ajouter(x, f))[-1] = x

Howmany:
C1: est_vide(ajouter(v,p)) alors howmany(p)=1

Summary:
C2: len(summary())== n

"""


from ezCLI import testcode

from simpleQueue import SQueue

class QNode:
    """ un element pour la liste chainee """
    __slots__ = ('__value', '__priority', '__next')
    def __init__(self, value:any, priority:int):
        self.__value = value
        self.__priority = priority
        self.__next = None

    def __repr__(self) -> str:
        return "{0.__class__.__name__}({0.value},{0.priority})".format(self)
    def __str__(self) -> str:
        return "value: {0.value}, priority: {0.priority} next: {0.next}".format(self)
    
    @property
    def value(self) -> any:
        """ protection en ecriture """
        return self.__value
    @property
    def priority(self) -> int:
        """ protection en ecriture """
        return self.__priority
    @property
    def next(self) -> 'QNode or None':
        """ accesseur en lecture """
        return self.__next
    @next.setter
    def next(self, other:'QNode'):
        """ accesseur en ecriture, on controle quoi et si on met """
        if isinstance(other, QNode) or other is None:
            self.__next = other


class BoundedOneQueue:
    # attributs
    __slots__ = ('__max_priority', '__cpt', '__hq', '__tq')

    def __init__(self, max_priority:int):
       """création de la file avec priorité bornée n'utilisant qu'une seule liste""" 
       self.__hq = self.__tq = None
       self.__max_priority = max_priority
       self.__cpt = 0

    @property
    def max_priority(self)->int:
        """envoie la valeur utlisée lors de la création de la file"""
        return self.__max_priority
    
    """getters"""
    @property
    def cpt(self)->int:
        return self.__cpt

    @property
    def hq(self)->QNode:
        return self.__hq

    @property
    def tq(self)->QNode:
        return self.__tq

    def __len__(self)->int:
        """renvoie le nombre d’éléments dans la file"""
        return self.__cpt
    
    def pop(self)->None:
        """enlève le premier élément de plus basse priorité
        require :file non vide"""
        if self.empty():
            print('nothing to pop...')
        else:
            self.__cpt -= 1
            self.__hq = self.__hq.next
            if self.__cpt == 0:
                self.__tq = None
                
    def push(self,v:any,p:int)->None:
        """permet d'inserer un élément"""
        if 0>p>=self.max_priority :
            print('priority not available...')
        else :
            self.__cpt += 1
            node = QNode(v,p)
            if self.empty(): #si premiere insertion la tete prend l'element
                self.__hq = node
                self.__tq = node
            else:
                parcours = self.__hq
                precedent = None
                found = False
                while parcours is not None:
                # on parcours chaque element jusqu'a trouver celui de propriety supérieur
                    if parcours.priority > p:
                        node.next = parcours
                        if precedent is not None:
                            precedent.next = node
                        else:
                            self.__hq = node
                        parcours = None
                        found = True
                    else:
                        precedent = parcours
                        parcours = parcours.next
                if found == False: # on place l'élément à la fin
                    self.__tq = node
                    if precedent is None:
                        self.__hq.next = self.__tq
                    else:
                        precedent.next = self.__tq
                    

            
    def first(self):
        """renvoie la première paire (v, p) de la liste
        require : file non vide"""
        if not self.empty():
            return [self.__hq.value, self.__hq.priority]
        else:
            return None
        
    def empty (self)->bool:
        """revoie vrai si la file est vide, faux sinon"""
        return self.__hq is None

    def to_list(self)->list:
        """renvoie une liste python des paires (v, p) présentes dans la file"""
        _current = self.__hq # curseur de parcours
        _store = [] # structure de stockage
        while _current is not None:
            _store.append([_current.value, _current.priority])
            _current = _current.next
        return _store

    def howmany(self, p:int)->int:
        """renvoie le nombre d’éléments dans la file ayant cette priorité"""
        _current = self.__hq # curseur de parcours
        _nbElem = 0 # nombre d'élément trouvé
        while _current is not None:
            if _current.priority == p:
                _nbElem += 1
            _current = _current.next
        return _nbElem
        
    def summary(self)->list:
        """renvoie une liste python de taille max_priority et contenant la distribution des priorités ordonnées de manière croissante"""
        _current = self.__hq # curseur de parcours
        _store = [] # structure de stockage
        _currentPriority = 0
        _store.append(0)
        while _currentPriority != self.max_priority:
            if _current is not None and _currentPriority == _current.priority:
                _store[_currentPriority] += 1
                _current = _current.next
            else:
                _currentPriority += 1
                if _currentPriority != self.max_priority:
                    _store.append(0)
        return _store

class BoundedListQueue:
        # attributs
    __slots__ = ('__max_priority', '__cpt', '__list')
    
    #[[(v,next),(v,next) -> None], [v,v,v], [empty]] //3


    def __init__(self, max_priority:int):
        """création d'une file avec priorité bornée utilisant une liste, priorité=index"""
        self.__max_priority = max_priority
        self.__cpt = 0
        self.__list = []
        for index in range(max_priority):
            self.__list.append(SQueue())
        
    @property
    def max_priority(self):
        """renvoie la valeur utlisée lors de la création de la file"""
        return self.__max_priority
    @property
    def cpt(self)->int:
        return self.__cpt
    @property
    def list(self)->int:
        return self.__list
      
    def __len__(self)->int:
        """renvoie le nombre d’éléments dans la file"""
        return self.__cpt
        
    def pop (self)->None:
        """enlève le premier élément de plus basse priorité
        require :file non vide"""
        if self.empty():
            print('nothing to pop...')
        else:
            self.__cpt -= 1
            found = False
            index = 0
            while found == False and index != self.__max_priority:
                if not self.__list[index].empty():
                    self.__list[index].pop()
                    found = True
                index += 1
        
    def push(self,v:any,p:int)->None:
        """permet d'inserer un élément"""
        if 0>p>=self.max_priority :
            print('priority not available...')
        else:
            self.__cpt += 1
            self.__list[p].push(v)

    def first(self):
        """renvoie la première paire (v, p) de la liste
        require : file non vide"""
        if self.empty():
            return None
        else:
            index = 0
            while index != self.__max_priority:
                if not self.__list[index].empty():
                    return [self.__list[index].first(), index]
                index += 1
        
    def empty (self)->bool:
        """revoie vrai si la file est vide, faux sinon"""
        return self.__cpt == 0

    def to_list(self)->list:
        """renvoie une liste python des paires (v, p) présentes dans la file, p=index"""
        _store = []
        index = 0
        for sQueue in self.__list:
            if not sQueue.empty():
                for value in sQueue.to_list():
                    _store.append([value, index])
            index += 1
        return _store

    def howmany(self, p:int)->int:
        """renvoie le nombre d’éléments dans la file ayant cette priorité"""
        return len(self.__list[p])
        
    def summary(self)->list:
        """renvoie une liste python de taille max_priority et contenant la distribution des priorités ordonnées de manière croissante"""
        _store = []
        for sQueue in self.__list:
            _store.append(len(sQueue))
        print(_store)
        return _store

if __name__ == "__main__":

    code = """
# creation file vide
queue = BoundedOneQueue(10)
queue.empty()==True  #A1
len(queue)==0        #B1

# max_priority
queue.max_priority
queue = BoundedOneQueue(10)
queue.max_priority==10  #A7

# push
len(queue) == 0
queue.push(12, 1)
len(queue) == 1
pre = len(queue)
queue.push(12,1)
post = len(queue)
post == pre + 1 # B3
queue.empty() == False # A2
print(queue.to_list())

queue1 = BoundedOneQueue(10)
for _ in range(5): queue1.push(_,0)
queue2 = BoundedOneQueue(10)
for _ in range(5): queue2.push(_,0)
queue1.to_list() == queue2.to_list()
queue1.pop()
queue1.push(42,0)
queue2.push(42,0)
queue2.pop()
queue1.to_list() == queue2.to_list() # A5


# pop
pre = len(queue)
queue.pop()
print(queue.to_list())
post = len(queue)
post == pre -1 #B2
queue.first() == [12, 1] #A3
queue.push(-1,2)
queue.first() == [12, 1] # A4
queue.push(-7,3)
queue.first() == [12, 1] # A4

# len
len(queue)
queue1.push(15,2)
queue2.pop()
len(queue.to_list()) == len(queue)   # B4
len(queue1.to_list()) == len(queue1) # B4
len(queue2.to_list()) == len(queue2) # B4

# first
queue.push(10, 1)
print(queue.to_list())
queue.first() == queue.to_list()[0]   # B5
queue1.first() == queue1.to_list()[0] # B5
queue2.first() == queue2.to_list()[0] # B5


# to_list
queue=BoundedOneQueue(10)
queue.push(28, 2)
queue.push(23, 1)
queue.to_list()[-1] == [28,2]  # B6
queue1.push(11, 5)
queue1.to_list()[-1] == [11, 5] # B6
queue2.push(31,6)
queue2.to_list()[-1] == [31,6] # B6
list = queue.to_list()
print(list)


# howmany
queue.howmany(1) == 1 #C1
queue.howmany(3) == 0 #C1

# summary
len(queue.summary())==10   #C2
queue.summary() == [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]

# creation file vide
# creation file vide
queue = BoundedListQueue(10)
queue.empty()==True  #A1
len(queue)==0        #B1

# max_priority
queue.max_priority
queue = BoundedListQueue(10)
queue.max_priority==10  #A7

# push
len(queue) == 0
queue.push(12, 1)
len(queue) == 1
pre = len(queue)
queue.push(12,1)
post = len(queue)
post == pre + 1 # B3
queue.empty() == False # A2
print(queue.to_list())

queue1 = BoundedListQueue(10)
for _ in range(5): queue1.push(_,0)
queue2 = BoundedOneQueue(10)
for _ in range(5): queue2.push(_,0)
queue1.to_list() == queue2.to_list()
queue1.pop()
queue1.push(42,0)
queue2.push(42,0)
queue2.pop()
queue1.to_list() == queue2.to_list() # A5


# pop
pre = len(queue)
queue.pop()
print(queue.to_list())
post = len(queue)
post == pre -1 #B2
queue.first() == [12, 1] #A3
queue.push(-1,2)
queue.first() == [12, 1] # A4
queue.push(-7,3)
queue.first() == [12, 1] # A4

# len
len(queue)
queue1.push(15,2)
queue2.pop()
len(queue.to_list()) == len(queue)   # B4
len(queue1.to_list()) == len(queue1) # B4
len(queue2.to_list()) == len(queue2) # B4

# first
queue.push(10, 1)
print(queue.to_list())
queue.first() == queue.to_list()[0]   # B5
queue1.first() == queue1.to_list()[0] # B5
queue2.first() == queue2.to_list()[0] # B5


# to_list
queue=BoundedListQueue(10)
queue.push(28, 2)
queue.push(23, 1)
queue.to_list()[-1] == [28,2]  # B6
queue1.push(11, 5)
queue1.to_list()[-1] == [11, 5] # B6
queue2.push(31,6)
queue2.to_list()[-1] == [31,6] # B6
list = queue.to_list()
print(list)


# howmany
queue.howmany(1) == 1 #C1
queue.howmany(3) == 0 #C1

# summary
len(queue.summary())==10   #C2
queue.summary() == [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]

""" ; testcode(code)
