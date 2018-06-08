# --------------------

#Integrantes: 
#Manuel Rodriguez 13-11223
#Ian Goldberg 14-10406

# ---------------------

import ply.yacc as yacc
import re

class InstrTree:
    def __init__(self, stamp, children = None, parent = None):
        self.stamp = stamp
        if children:
            self.children = children
        else:
            self.children = [ ]
        self.parent = parent
    
    def print_tree(self, level = 0):
        if self.parent != None: 
            print ('\t' * level + str(self.parent))
        if self.children != None:
            for children in self.children:
                if children.parent != None: children.print_tree(level+1)
                else:
                    children.print_tree(level)