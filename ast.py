import ply.yacc as yacc
import re

class InstrTree:
    def __init__(self ,stamp , children = None,instr = None):
        self.stamp = stamp
        if children:
            self.children = children
        else:
            self.children = [ ]
        self.instr = instr
    
    def print_tree(self):
        if self.instr != None: print(self.instr)
        if self.children != None:
            for children in self.children:
                if type(children) is not str:
                    children.print_tree()
                else:
                    print(children, end='')