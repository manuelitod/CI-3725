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
        print(self.stamp)
        if self.children != None:
            for children in self.children:
                children.print_tree()
        else:
            for instr in self.instr:
                instr.print_tree()
