#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "CONSTANCEAU Enola & PANETIER Camille"
__date__ = "06.12.20"
__usage__ = "Manipulation file avec priorité"

"""
QUEUE :File avec priorité
"""

from ezCLI import testcode


class BoundedOneQueue:
    def __init__(self):
       """création de la file avec priorité bornée n'utilisant qu'une seule liste""" 
    @property
    def max_priority(self):
        """envoie la valeur utlisée lors de la création de la file"""
        
    def __len__(self):
        """renvoie le nombre d’éléments dans la file"""
        return self.__cpt
    
    def pop(self)->None:
        """enlève le premier élément de plus basse priorité
        require :file non vide"""
        
    def push(self,p:int,v:any)->None:
        """permet d'inserer un élément"""
        if 0<p<=max_priority :
            return None
        else :
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

# max_priority

# len

# pop

# push

# first

# empty

# to_list

# howmany

# summary
""" ; testcode(code)
