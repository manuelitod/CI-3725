import ply.yacc as yacc
import re
from structs import *
from lexNEO import *

class Expr: pass

class BinOp(Expr):
    def __init__(self,left,op,right, typ):
        self.typ = typ
        self.left = left
        self.right = right
        self.op = op

class UniOp(Expr):
    def __init__(self,term,op, typ):
        self.typ = typ
        self.term = term
        self.op = op


class Number(Expr):
    def __init__(self,value):
        self.type = "Number"
        self.value = value

class Ident(Expr):
    def __init__(self,value):
        self.type = "Ident"
        self.value = value

class Bool(Expr):
    def __init__(self,value):
        self.type = "Bool"
        self.value = value

class Node:
    def __init__(self,stamp , children = None,instr = None):
         self.stamp = stamp
         if children:
              self.children = children
         else:
              self.children = [ ]
         self.instr = instr