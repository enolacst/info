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
        
    def __len__(self)->int:
        """renvoie le nombre d’éléments dans la file"""
        return self.__cpt
    
    def pop(self)->None:
        """enlève le premier élément de plus basse priorité
        require :file non vide"""
        if self.empty():
            print('nothing to pop...')
        else:
            first = self.__hq
            self.__hq = self.__hq.next
                
    def push(self,p:int,v:any)->None:
        """permet d'inserer un élément"""
        if 0<p<=self.max_priority :
            print('priority not available...')
        else :
            self.__cpt += 1
            node = QNode(v,p)
            if self.empty(): #si premiere insertion la tete prend l'element
                self.__hq = node
            else:
                parcours = self.__hq
                precedent = None
                found = False
                while parcours is not None:
                # on parcours chaque element jusqu'a trouver celui de propriety supérieur
                    if parcours.priority > v:
                        if precedent is not None:
                            precedent.next = node
                        else:
                            self.__hq = node
                        node.next = parcours
                        parcours = None
                        found = True
                    else:
                        precedent = parcours
                        parcours = parcours.next
                if found == False:
                    precedent.next = node
                    node = self.__tq 

            
    def first(self):
        """renvoie la première paire (v, p) de la liste
        require : file non vide"""
        return self.__hq
        
    def empty (self)->bool:
        """revoie vrai si la file est vide, faux sinon"""
        return self.__hq is None

    def to_list(self)->list:
        """renvoie une liste python des paires (v, p) présentes dans la file"""

    def howmany(self)->int:
        """renvoie le nombre d’éléments dans la file ayant cette priorité"""
        
    def summary(self)->list:
        """renvoie une liste python de taille max_priority et contenant la distribution des priorités ordonnées de manière croissante"""

class BoundedListQueue:
    def __init__():
        """création d'une file avec priorité bornée utilisant une liste, priorité=index"""
        
    @property
    def max_priority(self):
        """envoie la valeur utlisée lors de la création de la file"""
        
    def __len__(self):
        """renvoie le nombre d’éléments dans la file"""
        
    def pop (slef):
        """enlève le premier élément de plus basse priorité
        require :file non vide"""
        
    def push(self):
        """permet d'inserer un élément"""
        if p<max-priority:
            return
        else:
            return None #return temporaire pour faire passer la complilation
            
    def first(self):
        """renvoie la première paire (v, p) de la liste
        require : file non vide"""
        
    def empty (self)->bool:
        """revoie vrai si la file est vide, faux sinon"""

    def to_list(self):
        """renvoie une liste python des paires (v, p) présentes dans la file"""

    def howmany(self):
        """renvoie le nombre d’éléments dans la file ayant cette priorité"""
        
    def summary(self):
        """renvoie une liste python de taille max_priority et contenant la distribution des priorités ordonnées de manière croissante"""

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
queue.push(12, 5)

# first

# empty

# to_list

# howmany

# summary
""" ; testcode(code)
