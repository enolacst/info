#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "CONSTANCEAU Enola & PANETIER Camille"
__date__ = "06.12.20"
__usage__ = "Manipulation file avec priorité"

"""
QUEUE :File avec priorité
"""

from ezCLI import testcode

"""
Axiomes à vérifier :
"""

class BoundedOneQueue:
    def __init__(self):
        
    @property
    def max_priority:
        """envoie la valeur utlisée lors de la création de la file"""
        
    def __len__:
        """renvoie le nombre d’éléments dans la file"""
        return self.__cpt
    
    def pop(self):->None
        """enlève le premier élément de plus basse priorité
        require :file non vide"""
        
    def push(self,p:int,v:any)->None:
        """permet d'inserer un élément"""
        if 0<p<=max_priority :
            return None
        else :
            
    def first:
        """renvoie la première paire (v, p) de la liste
        require : file non vide"""
        
    def empty (self)->bool:
        """revoie vrai si la file est vide, faux sinon"""

    def to_list:
        """renvoie une liste python des paires (v, p) présentes dans la file"""

    def howmany:
        """renvoie le nombre d’éléments dans la file ayant cette priorité"""
        
    def summary:
        """renvoie une liste python de taille max_priority et contenant la distribution des priorités ordonnées de manière croissante"""

class BoundedListQueue:
    def __init__():
        
    @property
    def max_priority:
        """envoie la valeur utlisée lors de la création de la file"""
        
    def __len__:
        """renvoie le nombre d’éléments dans la file"""
        
    def pop (slef):
        """enlève le premier élément de plus basse priorité
        require :file non vide"""
        
    def push:
        """permet d'inserer un élément"""
        if p<max-priority:
            return
        else:
            
    def first:
        """renvoie la première paire (v, p) de la liste
        require : file non vide"""
        
    def empty (self)->bool:
        """revoie vrai si la file est vide, faux sinon"""

    def to_list:
        """renvoie une liste python des paires (v, p) présentes dans la file"""

    def howmany:
        """renvoie le nombre d’éléments dans la file ayant cette priorité"""
        
    def summary:
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