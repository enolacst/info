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

# max_priority
queue.max_priority

# len
len(queue)

# pop
queue.pop()

# push
len(queue) == 0
queue.push(12, 5)
len(queue) == 1

print(queue.to_list())

# first
queue.push(10, 1)
print(queue.to_list())
queue.first() == [10, 1]

# empty
queue.empty() == False
queue.pop()
queue.pop()
queue.empty() == True

# to_list
queue.push(28, 1)
queue.push(11, 5)
list = queue.to_list()
print(list)

# howmany
queue.howmany(1) == 1
queue.howmany(3) == 0

# summary
queue.summary() == [0, 1, 0, 0, 0, 1, 0, 0, 0, 0]

# creation file vide
queue = BoundedListQueue(10)

# max_priority
queue.max_priority

# len
len(queue)

# pop
queue.pop()

# push
len(queue) == 0
queue.push(12, 5)
len(queue) == 1

print(queue.to_list())

# first
queue.push(10, 1)
print(queue.to_list())
queue.first() == [10, 1]

# empty
queue.empty() == False
queue.pop()
queue.pop()
queue.empty() == True

# to_list
queue.push(28, 1)
queue.push(11, 5)
list = queue.to_list()
print(list)

# howmany
queue.howmany(1) == 1
queue.howmany(3) == 0

# summary
queue.summary() == [0, 1, 0, 0, 0, 1, 0, 0, 0, 0]

""" ; testcode(code)
