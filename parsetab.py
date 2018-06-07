
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocTkMenorTkMayornonassocTkMenorIgualTkMayorIgualleftNEGATkMultTkDivTkModTkSumaTkRestaleftTkNegacionTkConjuncionTkDisyuncionleftTkValorAsciiTkAnteriorCarTkSiguienteCarleftTkCorcheteAbreTkShiftTkConcatenacionTkAnteriorCar TkArray TkAsignacion TkBegin TkBool TkCaracter TkChar TkComa TkConcatenacion TkConjuncion TkCorcheteAbre TkCorcheteCierra TkDesigual TkDisyuncion TkDiv TkDosPuntos TkEnd TkFalse TkFor TkFrom TkHacer TkId TkIf TkIgual TkInt TkLlaveAbre TkLlaveCierra TkMayor TkMayorIgual TkMenor TkMenorIgual TkMod TkMult TkNegacion TkNum TkOf TkOtherwise TkParAbre TkParCierra TkPrint TkPunto TkPuntoYComa TkRead TkResta TkShift TkSiguienteCar TkStep TkSuma TkTo TkTrue TkValorAscii TkVar TkWhile TkWithINICIO :  TkWith DEC TkBegin INSTR TkEnd\n\t\t\t| TkBegin INSTR TkEndDEC : DEC TkVar IDENT TkDosPuntos TIPO\n\t\t| TkVar IDENT TkDosPuntos TIPO IDENT : TkId\n\t\t\t| ASIG_ID\n\t\t\t| IDENT TkComa TkId\n\t\t\t| IDENT TkComa ASIG_IDTIPO : TkInt\n\t\t\t| TkChar\n\t\t\t| TkBool\n\t\t\t| TkArray TkCorcheteAbre ARIT TkCorcheteCierra TkOf TIPO INSTR :  ASIG\n\t\t\t| I_O\n\t\t\t| COND\n\t\t\t| DETER\n\t\t\t| INDETER\n\t\t\t| INICIO\n\t\t\t| ASIG INSTR\n\t\t\t| I_O INSTR\n\t\t\t| INICIO INSTR\n\t\t\t| DETER INSTR\n\t\t\t| INDETER INSTR\n\t\t\t| COND INSTRASIG : TkId TkAsignacion EXPR TkPuntoYComaASIG_ID : TkId TkAsignacion EXPRARIT : TkNum\n\t\t\t| TkParAbre ARIT TkParCierra\n\t\t\t| ARIT TkSuma ARIT\n\t\t\t| ARIT TkResta ARIT\n\t\t\t| ARIT TkMult ARIT\n\t\t\t| ARIT TkDiv ARIT\n\t\t\t| ARIT TkMod ARIT\n\t\t\t| TkValorAscii TkCaracter\n\t\t\t| TkIdARIT :\t  TkResta ARIT %prec NEGABOOL : BOOL TkConjuncion BOOL\n\t\t\t| BOOL TkDisyuncion BOOL\n\t\t\t| ARIT TkMenor ARIT\n\t\t\t| ARIT TkMenorIgual ARIT\n\t\t\t| ARIT TkMayor ARIT\n\t\t\t| ARIT TkMayorIgual ARIT\n\t\t\t| ARIT TkIgual ARIT\n\t\t\t| ARIT TkDesigual ARIT\n\t\t\t| TkParAbre BOOL TkParCierra\n\t\t\t| TkFalse\n\t\t\t| TkTrue\n\t\t\t| TkNegacion BOOL\n\t\t\t| TkIdCHAR : TkCaracter\n\t\t\t| TkCaracter TkSiguienteCar\n\t\t\t| TkCaracter TkAnteriorCarCOND :  TkIf BOOL TkHacer INSTR TkEnd\n\t\t\t|  TkIf BOOL TkHacer INSTR TkOtherwise TkHacer INSTR TkEndINDETER : TkWhile BOOL TkHacer INSTR TkEndDETER :   TkFor TkId TkFrom ARIT TkTo ARIT DETER0DETER0 :  TkStep ARIT TkHacer INSTR TkEnd\n\t\t\t| TkHacer INSTR TkEndI_O :  TkRead TkId TkPuntoYComa\n\t\t\t| TkPrint EXPR TkPuntoYComaEXPR : CHAR\n\t\t\t| ARIT\n\t\t\t| ARRAY\n\t\t\t| BOOL\n\t\t\t| TkIdARRAY : ARRAY TkConcatenacion ARRAY\n\t\t\t | TkShift ARRAY\n\t\t\t | TkId TkCorcheteAbre ARIT TkCorcheteCierra\n\t\t\t | TkId'
    
_lr_action_items = {'TkNegacion':([8,12,15,26,34,45,51,58,76,77,],[26,26,26,26,26,26,26,26,26,26,]),'TkValorAscii':([8,12,15,26,31,34,45,51,58,61,62,63,64,65,66,67,68,69,70,71,73,76,77,80,87,126,129,138,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'TkWhile':([3,6,7,10,13,14,18,20,38,75,82,90,92,94,124,128,131,133,137,139,141,145,146,148,],[15,15,15,15,15,15,15,15,-2,15,-60,15,-59,-1,-25,-53,-55,15,-56,15,-54,15,-58,-57,]),'TkParCierra':([28,29,33,35,59,60,72,74,78,79,85,86,103,104,105,106,107,108,109,110,111,112,113,114,116,117,118,119,],[-47,-46,-35,-27,-48,-34,-35,-36,118,119,118,-35,-43,-40,-41,-30,-31,-32,-33,-44,-42,-39,-29,118,-38,-37,-28,-45,]),'TkSiguienteCar':([47,],[88,]),'TkChar':([57,93,140,],[101,101,101,]),'TkDiv':([30,33,35,40,46,60,72,74,78,85,86,103,104,105,106,107,108,109,110,111,112,113,114,118,120,122,132,134,142,],[66,-35,-27,66,-35,-34,-35,-36,66,66,-35,66,66,66,-30,-31,-32,-33,66,66,66,-29,66,-28,66,66,66,66,66,]),'TkBegin':([0,3,4,6,7,10,13,14,18,20,38,75,82,90,92,94,97,99,100,101,124,125,128,131,133,137,139,141,144,145,146,148,],[3,3,20,3,3,3,3,3,3,3,-2,3,-60,3,-59,-1,-4,-11,-9,-10,-25,-3,-53,-55,3,-56,3,-54,-12,3,-58,-57,]),'TkDesigual':([30,33,35,40,46,60,72,74,78,85,86,106,107,108,109,113,118,],[68,-35,-27,68,-35,-34,-35,-36,68,68,-35,-30,-31,-32,-33,-29,-28,]),'TkMayorIgual':([30,33,35,40,46,60,72,74,78,85,86,106,107,108,109,113,118,],[69,-35,-27,69,-35,-34,-35,-36,69,69,-35,-30,-31,-32,-33,-29,-28,]),'TkDosPuntos':([21,22,23,28,29,33,35,39,40,42,44,46,47,54,59,60,72,74,83,84,88,89,95,96,102,103,104,105,106,107,108,109,110,111,112,113,116,117,118,119,121,130,],[57,-5,-6,-47,-46,-49,-27,-63,-62,-64,-61,-35,-50,93,-48,-34,-35,-36,-69,-67,-51,-52,-7,-8,-26,-43,-40,-41,-30,-31,-32,-33,-44,-42,-39,-29,-38,-37,-28,-45,-66,-68,]),'TkParAbre':([8,12,15,26,31,34,45,51,58,61,62,63,64,65,66,67,68,69,70,71,73,76,77,80,87,126,129,138,],[34,45,34,34,73,34,45,45,45,73,73,73,73,73,73,73,73,73,73,73,73,34,34,73,73,73,73,73,]),'TkFrom':([36,],[80,]),'TkInt':([57,93,140,],[100,100,100,]),'TkSuma':([30,33,35,40,46,60,72,74,78,85,86,103,104,105,106,107,108,109,110,111,112,113,114,118,120,122,132,134,142,],[71,-35,-27,71,-35,-34,-35,-36,71,71,-35,71,71,71,-30,-31,-32,-33,71,71,71,-29,71,-28,71,71,71,71,71,]),'TkTo':([35,60,72,74,106,107,108,109,113,118,120,],[-27,-34,-35,-36,-30,-31,-32,-33,-29,-28,129,]),'$end':([2,38,94,],[0,-2,-1,]),'TkPrint':([3,6,7,10,13,14,18,20,38,75,82,90,92,94,124,128,131,133,137,139,141,145,146,148,],[12,12,12,12,12,12,12,12,-2,12,-60,12,-59,-1,-25,-53,-55,12,-56,12,-54,12,-58,-57,]),'TkMayor':([30,33,35,40,46,60,72,74,78,85,86,106,107,108,109,113,118,],[63,-35,-27,63,-35,-34,-35,-36,63,63,-35,-30,-31,-32,-33,-29,-28,]),'TkResta':([8,12,15,26,30,31,33,34,35,40,45,46,51,58,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,76,77,78,80,85,86,87,103,104,105,106,107,108,109,110,111,112,113,114,118,120,122,126,129,132,134,138,142,],[31,31,31,31,64,31,-35,31,-27,64,31,-35,31,31,-34,31,31,31,31,31,31,31,31,31,31,31,-35,31,-36,31,31,64,31,64,-35,31,64,64,64,-30,-31,-32,-33,64,64,64,-29,64,-28,64,64,31,31,64,64,31,64,]),'TkMult':([30,33,35,40,46,60,72,74,78,85,86,103,104,105,106,107,108,109,110,111,112,113,114,118,120,122,132,134,142,],[65,-35,-27,65,-35,-34,-35,-36,65,65,-35,65,65,65,-30,-31,-32,-33,65,65,65,-29,65,-28,65,65,65,65,65,]),'TkId':([3,5,6,7,8,9,10,12,13,14,15,17,18,19,20,26,31,34,38,43,45,51,56,58,61,62,63,64,65,66,67,68,69,70,71,73,75,76,77,80,81,82,87,90,92,94,124,126,128,129,131,133,137,138,139,141,145,146,148,],[16,22,16,16,33,36,16,46,16,16,33,52,16,22,16,33,72,33,-2,83,86,46,95,46,72,72,72,72,72,72,72,72,72,72,72,72,16,33,33,72,83,-60,72,16,-59,-1,-25,72,-53,72,-55,16,-56,72,16,-54,16,-58,-57,]),'TkRead':([3,6,7,10,13,14,18,20,38,75,82,90,92,94,124,128,131,133,137,139,141,145,146,148,],[17,17,17,17,17,17,17,17,-2,17,-60,17,-59,-1,-25,-53,-55,17,-56,17,-54,17,-58,-57,]),'TkCorcheteCierra':([35,60,72,74,106,107,108,109,113,118,122,132,],[-27,-34,-35,-36,-30,-31,-32,-33,-29,-28,130,135,]),'TkCaracter':([12,27,51,58,],[47,60,47,47,]),'TkComa':([21,22,23,28,29,33,35,39,40,42,44,46,47,54,59,60,72,74,83,84,88,89,95,96,102,103,104,105,106,107,108,109,110,111,112,113,116,117,118,119,121,130,],[56,-5,-6,-47,-46,-49,-27,-63,-62,-64,-61,-35,-50,56,-48,-34,-35,-36,-69,-67,-51,-52,-7,-8,-26,-43,-40,-41,-30,-31,-32,-33,-44,-42,-39,-29,-38,-37,-28,-45,-66,-68,]),'TkIgual':([30,33,35,40,46,60,72,74,78,85,86,106,107,108,109,113,118,],[61,-35,-27,61,-35,-34,-35,-36,61,61,-35,-30,-31,-32,-33,-29,-28,]),'TkPuntoYComa':([28,29,33,35,39,40,41,42,44,46,47,52,59,60,72,74,83,84,88,89,91,103,104,105,106,107,108,109,110,111,112,113,116,117,118,119,121,130,],[-47,-46,-49,-27,-63,-62,82,-64,-61,-35,-50,92,-48,-34,-35,-36,-69,-67,-51,-52,124,-43,-40,-41,-30,-31,-32,-33,-44,-42,-39,-29,-38,-37,-28,-45,-66,-68,]),'TkArray':([57,93,140,],[98,98,98,]),'TkTrue':([8,12,15,26,34,45,51,58,76,77,],[28,28,28,28,28,28,28,28,28,28,]),'TkIf':([3,6,7,10,13,14,18,20,38,75,82,90,92,94,124,128,131,133,137,139,141,145,146,148,],[8,8,8,8,8,8,8,8,-2,8,-60,8,-59,-1,-25,-53,-55,8,-56,8,-54,8,-58,-57,]),'TkFor':([3,6,7,10,13,14,18,20,38,75,82,90,92,94,124,128,131,133,137,139,141,145,146,148,],[9,9,9,9,9,9,9,9,-2,9,-60,9,-59,-1,-25,-53,-55,9,-56,9,-54,9,-58,-57,]),'TkVar':([1,4,97,99,100,101,125,144,],[5,19,-4,-11,-9,-10,-3,-12,]),'TkCorcheteAbre':([46,83,98,],[87,87,126,]),'TkOtherwise':([6,7,10,13,14,18,24,25,37,38,48,49,53,82,92,94,115,124,128,131,137,141,146,148,],[-14,-16,-17,-13,-18,-15,-20,-22,-23,-2,-19,-21,-24,-60,-59,-1,127,-25,-53,-55,-56,-54,-58,-57,]),'TkEnd':([6,7,10,11,13,14,18,24,25,37,38,48,49,53,55,82,92,94,115,123,124,128,131,136,137,141,143,146,147,148,],[-14,-16,-17,38,-13,-18,-15,-20,-22,-23,-2,-19,-21,-24,94,-60,-59,-1,128,131,-25,-53,-55,141,-56,-54,146,-58,148,-57,]),'TkBool':([57,93,140,],[99,99,99,]),'TkFalse':([8,12,15,26,34,45,51,58,76,77,],[29,29,29,29,29,29,29,29,29,29,]),'TkConjuncion':([28,29,32,33,35,42,46,50,59,60,72,74,79,86,103,104,105,106,107,108,109,110,111,112,113,116,117,118,119,],[-47,-46,77,-49,-27,77,-49,77,-48,-34,-35,-36,77,-49,-43,-40,-41,-30,-31,-32,-33,-44,-42,-39,-29,-38,-37,-28,-45,]),'TkHacer':([28,29,32,33,35,50,59,60,72,74,103,104,105,106,107,108,109,110,111,112,113,116,117,118,119,127,134,142,],[-47,-46,75,-49,-27,90,-48,-34,-35,-36,-43,-40,-41,-30,-31,-32,-33,-44,-42,-39,-29,-38,-37,-28,-45,133,139,145,]),'TkMenorIgual':([30,33,35,40,46,60,72,74,78,85,86,106,107,108,109,113,118,],[62,-35,-27,62,-35,-34,-35,-36,62,62,-35,-30,-31,-32,-33,-29,-28,]),'TkDisyuncion':([28,29,32,33,35,42,46,50,59,60,72,74,79,86,103,104,105,106,107,108,109,110,111,112,113,116,117,118,119,],[-47,-46,76,-49,-27,76,-49,76,-48,-34,-35,-36,76,-49,-43,-40,-41,-30,-31,-32,-33,-44,-42,-39,-29,-38,-37,-28,-45,]),'TkStep':([35,60,72,74,106,107,108,109,113,118,134,],[-27,-34,-35,-36,-30,-31,-32,-33,-29,-28,138,]),'TkShift':([12,43,51,58,81,],[43,43,43,43,43,]),'TkOf':([135,],[140,]),'TkConcatenacion':([39,46,83,84,121,130,],[81,-69,-69,-67,-66,-68,]),'TkMod':([30,33,35,40,46,60,72,74,78,85,86,103,104,105,106,107,108,109,110,111,112,113,114,118,120,122,132,134,142,],[67,-35,-27,67,-35,-34,-35,-36,67,67,-35,67,67,67,-30,-31,-32,-33,67,67,67,-29,67,-28,67,67,67,67,67,]),'TkAsignacion':([16,22,95,],[51,58,58,]),'TkWith':([0,3,6,7,10,13,14,18,20,38,75,82,90,92,94,124,128,131,133,137,139,141,145,146,148,],[1,1,1,1,1,1,1,1,1,-2,1,-60,1,-59,-1,-25,-53,-55,1,-56,1,-54,1,-58,-57,]),'TkNum':([8,12,15,26,31,34,45,51,58,61,62,63,64,65,66,67,68,69,70,71,73,76,77,80,87,126,129,138,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'TkAnteriorCar':([47,],[89,]),'TkMenor':([30,33,35,40,46,60,72,74,78,85,86,106,107,108,109,113,118,],[70,-35,-27,70,-35,-34,-35,-36,70,70,-35,-30,-31,-32,-33,-29,-28,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'TIPO':([57,93,140,],[97,125,144,]),'BOOL':([8,12,15,26,34,45,51,58,76,77,],[32,42,50,59,79,79,42,42,116,117,]),'IDENT':([5,19,],[21,54,]),'DEC':([1,],[4,]),'EXPR':([12,51,58,],[41,91,102,]),'ASIG_ID':([5,19,56,],[23,23,96,]),'INICIO':([0,3,6,7,10,13,14,18,20,75,90,133,139,145,],[2,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'I_O':([3,6,7,10,13,14,18,20,75,90,133,139,145,],[6,6,6,6,6,6,6,6,6,6,6,6,6,]),'INDETER':([3,6,7,10,13,14,18,20,75,90,133,139,145,],[10,10,10,10,10,10,10,10,10,10,10,10,10,]),'CHAR':([12,51,58,],[44,44,44,]),'DETER0':([134,],[137,]),'ARRAY':([12,43,51,58,81,],[39,84,39,39,121,]),'DETER':([3,6,7,10,13,14,18,20,75,90,133,139,145,],[7,7,7,7,7,7,7,7,7,7,7,7,7,]),'INSTR':([3,6,7,10,13,14,18,20,75,90,133,139,145,],[11,24,25,37,48,49,53,55,115,123,136,143,147,]),'ARIT':([8,12,15,26,31,34,45,51,58,61,62,63,64,65,66,67,68,69,70,71,73,76,77,80,87,126,129,138,],[30,40,30,30,74,78,85,40,40,103,104,105,106,107,108,109,110,111,112,113,114,30,30,120,122,132,134,142,]),'ASIG':([3,6,7,10,13,14,18,20,75,90,133,139,145,],[13,13,13,13,13,13,13,13,13,13,13,13,13,]),'COND':([3,6,7,10,13,14,18,20,75,90,133,139,145,],[18,18,18,18,18,18,18,18,18,18,18,18,18,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> INICIO","S'",1,None,None,None),
  ('INICIO -> TkWith DEC TkBegin INSTR TkEnd','INICIO',5,'p_inicio','parser.py',10),
  ('INICIO -> TkBegin INSTR TkEnd','INICIO',3,'p_inicio','parser.py',11),
  ('DEC -> DEC TkVar IDENT TkDosPuntos TIPO','DEC',5,'p_dec','parser.py',20),
  ('DEC -> TkVar IDENT TkDosPuntos TIPO','DEC',4,'p_dec','parser.py',21),
  ('IDENT -> TkId','IDENT',1,'p_ident','parser.py',30),
  ('IDENT -> ASIG_ID','IDENT',1,'p_ident','parser.py',31),
  ('IDENT -> IDENT TkComa TkId','IDENT',3,'p_ident','parser.py',32),
  ('IDENT -> IDENT TkComa ASIG_ID','IDENT',3,'p_ident','parser.py',33),
  ('TIPO -> TkInt','TIPO',1,'p_tipo','parser.py',46),
  ('TIPO -> TkChar','TIPO',1,'p_tipo','parser.py',47),
  ('TIPO -> TkBool','TIPO',1,'p_tipo','parser.py',48),
  ('TIPO -> TkArray TkCorcheteAbre ARIT TkCorcheteCierra TkOf TIPO','TIPO',6,'p_tipo','parser.py',49),
  ('INSTR -> ASIG','INSTR',1,'p_instr','parser.py',58),
  ('INSTR -> I_O','INSTR',1,'p_instr','parser.py',59),
  ('INSTR -> COND','INSTR',1,'p_instr','parser.py',60),
  ('INSTR -> DETER','INSTR',1,'p_instr','parser.py',61),
  ('INSTR -> INDETER','INSTR',1,'p_instr','parser.py',62),
  ('INSTR -> INICIO','INSTR',1,'p_instr','parser.py',63),
  ('INSTR -> ASIG INSTR','INSTR',2,'p_instr','parser.py',64),
  ('INSTR -> I_O INSTR','INSTR',2,'p_instr','parser.py',65),
  ('INSTR -> INICIO INSTR','INSTR',2,'p_instr','parser.py',66),
  ('INSTR -> DETER INSTR','INSTR',2,'p_instr','parser.py',67),
  ('INSTR -> INDETER INSTR','INSTR',2,'p_instr','parser.py',68),
  ('INSTR -> COND INSTR','INSTR',2,'p_instr','parser.py',69),
  ('ASIG -> TkId TkAsignacion EXPR TkPuntoYComa','ASIG',4,'p_asig','parser.py',75),
  ('ASIG_ID -> TkId TkAsignacion EXPR','ASIG_ID',3,'p_asig_id','parser.py',81),
  ('ARIT -> TkNum','ARIT',1,'p_arit','parser.py',87),
  ('ARIT -> TkParAbre ARIT TkParCierra','ARIT',3,'p_arit','parser.py',88),
  ('ARIT -> ARIT TkSuma ARIT','ARIT',3,'p_arit','parser.py',89),
  ('ARIT -> ARIT TkResta ARIT','ARIT',3,'p_arit','parser.py',90),
  ('ARIT -> ARIT TkMult ARIT','ARIT',3,'p_arit','parser.py',91),
  ('ARIT -> ARIT TkDiv ARIT','ARIT',3,'p_arit','parser.py',92),
  ('ARIT -> ARIT TkMod ARIT','ARIT',3,'p_arit','parser.py',93),
  ('ARIT -> TkValorAscii TkCaracter','ARIT',2,'p_arit','parser.py',94),
  ('ARIT -> TkId','ARIT',1,'p_arit','parser.py',95),
  ('ARIT -> TkResta ARIT','ARIT',2,'p_nega','parser.py',112),
  ('BOOL -> BOOL TkConjuncion BOOL','BOOL',3,'p_bool','parser.py',118),
  ('BOOL -> BOOL TkDisyuncion BOOL','BOOL',3,'p_bool','parser.py',119),
  ('BOOL -> ARIT TkMenor ARIT','BOOL',3,'p_bool','parser.py',120),
  ('BOOL -> ARIT TkMenorIgual ARIT','BOOL',3,'p_bool','parser.py',121),
  ('BOOL -> ARIT TkMayor ARIT','BOOL',3,'p_bool','parser.py',122),
  ('BOOL -> ARIT TkMayorIgual ARIT','BOOL',3,'p_bool','parser.py',123),
  ('BOOL -> ARIT TkIgual ARIT','BOOL',3,'p_bool','parser.py',124),
  ('BOOL -> ARIT TkDesigual ARIT','BOOL',3,'p_bool','parser.py',125),
  ('BOOL -> TkParAbre BOOL TkParCierra','BOOL',3,'p_bool','parser.py',126),
  ('BOOL -> TkFalse','BOOL',1,'p_bool','parser.py',127),
  ('BOOL -> TkTrue','BOOL',1,'p_bool','parser.py',128),
  ('BOOL -> TkNegacion BOOL','BOOL',2,'p_bool','parser.py',129),
  ('BOOL -> TkId','BOOL',1,'p_bool','parser.py',130),
  ('CHAR -> TkCaracter','CHAR',1,'p_char','parser.py',149),
  ('CHAR -> TkCaracter TkSiguienteCar','CHAR',2,'p_char','parser.py',150),
  ('CHAR -> TkCaracter TkAnteriorCar','CHAR',2,'p_char','parser.py',151),
  ('COND -> TkIf BOOL TkHacer INSTR TkEnd','COND',5,'p_cond','parser.py',164),
  ('COND -> TkIf BOOL TkHacer INSTR TkOtherwise TkHacer INSTR TkEnd','COND',8,'p_cond','parser.py',165),
  ('INDETER -> TkWhile BOOL TkHacer INSTR TkEnd','INDETER',5,'p_indeter','parser.py',170),
  ('DETER -> TkFor TkId TkFrom ARIT TkTo ARIT DETER0','DETER',7,'p_deter','parser.py',176),
  ('DETER0 -> TkStep ARIT TkHacer INSTR TkEnd','DETER0',5,'p_deter0','parser.py',182),
  ('DETER0 -> TkHacer INSTR TkEnd','DETER0',3,'p_deter0','parser.py',183),
  ('I_O -> TkRead TkId TkPuntoYComa','I_O',3,'p_i_o','parser.py',192),
  ('I_O -> TkPrint EXPR TkPuntoYComa','I_O',3,'p_i_o','parser.py',193),
  ('EXPR -> CHAR','EXPR',1,'p_expr','parser.py',199),
  ('EXPR -> ARIT','EXPR',1,'p_expr','parser.py',200),
  ('EXPR -> ARRAY','EXPR',1,'p_expr','parser.py',201),
  ('EXPR -> BOOL','EXPR',1,'p_expr','parser.py',202),
  ('EXPR -> TkId','EXPR',1,'p_expr','parser.py',203),
  ('ARRAY -> ARRAY TkConcatenacion ARRAY','ARRAY',3,'p_array','parser.py',215),
  ('ARRAY -> TkShift ARRAY','ARRAY',2,'p_array','parser.py',216),
  ('ARRAY -> TkId TkCorcheteAbre ARIT TkCorcheteCierra','ARRAY',4,'p_array','parser.py',217),
  ('ARRAY -> TkId','ARRAY',1,'p_array','parser.py',218),
]
