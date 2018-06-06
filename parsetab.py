
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftNEGATkMultTkDivTkModTkSumaTkRestaleftTkNegacionTkConjuncionTkDisyuncionleftTkValorAsciiTkAnteriorCarTkSiguienteCarleftTkCorcheteAbreTkShiftTkConcatenacionTkAnteriorCar TkArray TkAsignacion TkBegin TkBool TkCaracter TkChar TkComa TkConcatenacion TkConjuncion TkCorcheteAbre TkCorcheteCierra TkDisyuncion TkDiv TkDosPuntos TkEnd TkFalse TkFor TkFrom TkHacer TkId TkIf TkIgual TkInt TkLlaveAbre TkLlaveCierra TkMayor TkMayorIgual TkMenor TkMenorIgual TkMod TkMult TkNegacion TkNum TkOf TkOtherwise TkParAbre TkParCierra TkPrint TkPunto TkPuntoYComa TkRead TkResta TkShift TkSiguienteCar TkStep TkSuma TkTo TkTrue TkValorAscii TkVar TkWhile TkWithINICIO :  TkWith DEC TkBegin INSTR TkEnd\n\t\t\t| TkBegin INSTR TkEndDEC : DEC TkVar IDENT TkDosPuntos TIPO\n\t\t| TkVar IDENT TkDosPuntos TIPO IDENT : TkId\n\t\t\t| ASIG_ID\n\t\t\t| IDENT TkComa IDENTTIPO :    TkInt\n\t\t\t| TkChar\n\t\t\t| TkBool\n\t\t\t| TkArray TkCorcheteAbre ARIT TkCorcheteCierra TkOf TIPO INSTR :   SEC\n\t\t\t| INSTR1SEC : INSTR INSTR1INSTR1 :  ASIG\n\t\t\t| I_O\n\t\t\t| COND\n\t\t\t| DETER\n\t\t\t| INDETER\n\t\t\t| INICIOASIG : TkId TkAsignacion EXPR TkPuntoYComaASIG_ID : TkId TkAsignacion EXPRARIT : TkNum\n\t\t\t| TkParAbre ARIT TkParCierra\n\t\t\t| ARIT TkSuma ARIT\n\t\t\t| ARIT TkResta ARIT\n\t\t\t| ARIT TkMult ARIT\n\t\t\t| ARIT TkDiv ARIT\n\t\t\t| ARIT TkMod ARIT\n\t\t\t| TkValorAscii TkCaracter\n\t\t\t| TkIdARIT :\t  TkResta ARIT %prec NEGABOOL : BOOL TkConjuncion BOOL\n\t\t\t| BOOL TkDisyuncion BOOL\n\t\t\t| ARIT TkMenor ARIT\n\t\t\t| ARIT TkMenorIgual ARIT\n\t\t\t| ARIT TkMayor ARIT\n\t\t\t| ARIT TkMayorIgual ARIT\n\t\t\t| EXPR TkIgual EXPR\n\t\t\t| TkParAbre BOOL TkParCierra\n\t\t\t| TkFalse\n\t\t\t| TkTrue\n\t\t\t| TkNegacion BOOL\n\t\t\t| TkIdCHAR : TkId \n\t\t\t| TkCaracter\n\t\t\t| TkCaracter TkSiguienteCar\n\t\t\t| TkCaracter TkAnteriorCarCOND : \t  TkIf BOOL TkHacer INSTR COND0COND0 :    TkOtherwise TkHacer INSTR\n\t\t\t\t| TkEndINDETER : TkWhile BOOL TkHacer INSTR TkEndDETER :   TkFor TkId TkFrom ARIT TkTo ARIT DETER0DETER0 :  TkStep ARIT TkHacer INSTR TkEnd\n\t\t\t| TkHacer INSTR TkEndI_O :  TkRead TkId TkPuntoYComa\n\t\t\t| TkPrint EXPR TkPuntoYComaEXPR : CHAR\n\t\t\t| ARIT\n\t\t\t| ARRAY\n\t\t\t| TkId TkCorcheteAbre ARIT TkCorcheteCierra\n\t\t\t| TkIdARRAY : ARRAY TkConcatenacion ARRAY\n\t\t\t | TkShift ARRAY\n\t\t\t | TkId'
    
_lr_action_items = {'TkMult':([23,27,30,36,40,53,54,55,67,79,88,90,91,92,93,94,95,100,101,102,103,106,125,126,132,],[-31,-23,60,-31,60,-31,-32,-30,60,60,60,-27,-28,-29,-25,-26,-24,60,60,60,60,60,60,60,60,]),'TkVar':([3,19,109,110,111,112,122,137,],[20,47,-10,-4,-9,-8,-3,-11,]),'TkTo':([27,53,54,55,90,91,92,93,94,95,106,],[-23,-31,-32,-30,-27,-28,-29,-25,-26,-24,121,]),'TkIf':([1,4,6,8,11,12,13,15,16,18,43,44,46,59,68,70,80,82,87,97,105,107,117,119,120,124,127,129,130,133,135,136,138,139,],[14,-12,-15,-17,-19,-16,-13,-18,14,-20,-2,-14,14,-57,-56,14,14,14,-21,14,14,-1,-52,-51,-49,14,14,-53,14,14,14,-55,14,-54,]),'TkParCierra':([22,23,26,27,30,31,35,36,38,53,54,55,57,58,65,66,67,72,78,79,89,90,91,92,93,94,95,96,98,99,100,101,102,103,104,116,],[-58,-31,-60,-23,-59,-46,-41,-31,-42,-31,-32,-30,-64,-65,-48,-47,95,-43,104,95,-63,-27,-28,-29,-25,-26,-24,-34,-33,-39,-35,-36,-38,-37,-40,-61,]),'TkSiguienteCar':([31,],[66,]),'TkFalse':([10,14,37,41,69,71,],[35,35,35,35,35,35,]),'TkResta':([7,10,14,21,23,24,27,30,32,36,37,40,41,52,53,54,55,60,61,62,63,64,67,69,71,73,74,75,76,77,79,81,86,88,90,91,92,93,94,95,100,101,102,103,106,121,123,125,126,128,132,],[24,24,24,24,-31,24,-23,64,24,-31,24,64,24,24,-31,-32,-30,24,24,24,24,24,64,24,24,24,24,24,24,24,64,24,24,64,-27,-28,-29,-25,-26,-24,64,64,64,64,64,24,24,64,64,24,64,]),'TkMenorIgual':([27,36,40,53,54,55,79,90,91,92,93,94,95,],[-23,-31,75,-31,-32,-30,75,-27,-28,-29,-25,-26,-24,]),'TkArray':([84,108,134,],[113,113,113,]),'TkBool':([84,108,134,],[109,109,109,]),'TkHacer':([22,23,26,27,30,31,34,35,36,38,42,53,54,55,57,58,65,66,72,89,90,91,92,93,94,95,96,98,99,100,101,102,103,104,116,118,125,132,],[-58,-31,-60,-23,-59,-46,70,-41,-44,-42,80,-31,-32,-30,-64,-65,-48,-47,-43,-63,-27,-28,-29,-25,-26,-24,-34,-33,-39,-35,-36,-38,-37,-40,-61,124,130,135,]),'TkTrue':([10,14,37,41,69,71,],[38,38,38,38,38,38,]),'TkPrint':([1,4,6,8,11,12,13,15,16,18,43,44,46,59,68,70,80,82,87,97,105,107,117,119,120,124,127,129,130,133,135,136,138,139,],[7,-12,-15,-17,-19,-16,-13,-18,7,-20,-2,-14,7,-57,-56,7,7,7,-21,7,7,-1,-52,-51,-49,7,7,-53,7,7,7,-55,7,-54,]),'TkBegin':([0,1,4,6,8,11,12,13,15,16,18,19,43,44,46,59,68,70,80,82,87,97,105,107,109,110,111,112,117,119,120,122,124,127,129,130,133,135,136,137,138,139,],[1,1,-12,-15,-17,-19,-16,-13,-18,1,-20,46,-2,-14,1,-57,-56,1,1,1,-21,1,1,-1,-10,-4,-9,-8,-52,-51,-49,-3,1,1,-53,1,1,1,-55,-11,1,-54,]),'TkShift':([7,10,14,21,28,37,41,56,69,71,73,86,],[28,28,28,28,28,28,28,28,28,28,28,28,]),'TkIgual':([22,26,27,31,36,39,40,53,54,55,57,58,65,66,79,89,90,91,92,93,94,95,116,],[-58,-60,-23,-46,-31,73,-59,-31,-32,-30,-64,-65,-48,-47,-59,-63,-27,-28,-29,-25,-26,-24,-61,]),'TkDosPuntos':([22,23,26,27,30,31,48,49,50,53,54,55,57,58,65,66,83,89,90,91,92,93,94,95,114,115,116,],[-58,-31,-60,-23,-59,-46,-6,84,-5,-31,-32,-30,-64,-65,-48,-47,108,-63,-27,-28,-29,-25,-26,-24,-7,-22,-61,]),'TkCorcheteAbre':([23,36,113,],[52,52,123,]),'TkAnteriorCar':([31,],[65,]),'TkStep':([27,53,54,55,90,91,92,93,94,95,125,],[-23,-31,-32,-30,-27,-28,-29,-25,-26,-24,128,]),'TkConjuncion':([22,23,26,27,30,31,34,35,36,38,42,53,54,55,57,58,65,66,72,78,89,90,91,92,93,94,95,96,98,99,100,101,102,103,104,116,],[-58,-31,-60,-23,-59,-46,71,-41,-44,-42,71,-31,-32,-30,-64,-65,-48,-47,-43,71,-63,-27,-28,-29,-25,-26,-24,-34,-33,-39,-35,-36,-38,-37,-40,-61,]),'TkCaracter':([7,10,14,21,25,37,41,69,71,73,86,],[31,31,31,31,55,31,31,31,31,31,31,]),'TkConcatenacion':([23,26,36,57,58,89,],[-65,56,-65,-64,-65,-63,]),'TkFor':([1,4,6,8,11,12,13,15,16,18,43,44,46,59,68,70,80,82,87,97,105,107,117,119,120,124,127,129,130,133,135,136,138,139,],[17,-12,-15,-17,-19,-16,-13,-18,17,-20,-2,-14,17,-57,-56,17,17,17,-21,17,17,-1,-52,-51,-49,17,17,-53,17,17,17,-55,17,-54,]),'TkNum':([7,10,14,21,24,32,37,41,52,60,61,62,63,64,69,71,73,74,75,76,77,81,86,121,123,128,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'TkWhile':([1,4,6,8,11,12,13,15,16,18,43,44,46,59,68,70,80,82,87,97,105,107,117,119,120,124,127,129,130,133,135,136,138,139,],[10,-12,-15,-17,-19,-16,-13,-18,10,-20,-2,-14,10,-57,-56,10,10,10,-21,10,10,-1,-52,-51,-49,10,10,-53,10,10,10,-55,10,-54,]),'TkEnd':([4,6,8,11,12,13,15,16,18,43,44,59,68,82,87,97,105,107,117,119,120,127,129,133,136,138,139,],[-12,-15,-17,-19,-16,-13,-18,43,-20,-2,-14,-57,-56,107,-21,117,119,-1,-52,-51,-49,-50,-53,136,-55,139,-54,]),'TkPuntoYComa':([22,23,26,27,29,30,31,33,51,53,54,55,57,58,65,66,89,90,91,92,93,94,95,116,],[-58,-31,-60,-23,59,-59,-46,68,87,-31,-32,-30,-64,-65,-48,-47,-63,-27,-28,-29,-25,-26,-24,-61,]),'TkId':([1,4,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,24,28,32,37,41,43,44,46,47,52,56,59,60,61,62,63,64,68,69,70,71,73,74,75,76,77,80,81,82,85,86,87,97,105,107,117,119,120,121,123,124,127,128,129,130,133,135,136,138,139,],[5,-12,-15,23,-17,33,36,-19,-16,-13,36,-18,5,45,-20,50,23,53,58,53,36,36,-2,-14,5,50,53,58,-57,53,53,53,53,53,-56,36,5,36,23,53,53,53,53,5,53,5,50,23,-21,5,5,-1,-52,-51,-49,53,53,5,5,53,-53,5,5,5,-55,5,-54,]),'TkRead':([1,4,6,8,11,12,13,15,16,18,43,44,46,59,68,70,80,82,87,97,105,107,117,119,120,124,127,129,130,133,135,136,138,139,],[9,-12,-15,-17,-19,-16,-13,-18,9,-20,-2,-14,9,-57,-56,9,9,9,-21,9,9,-1,-52,-51,-49,9,9,-53,9,9,9,-55,9,-54,]),'TkNegacion':([10,14,37,41,69,71,],[37,37,37,37,37,37,]),'TkDiv':([23,27,30,36,40,53,54,55,67,79,88,90,91,92,93,94,95,100,101,102,103,106,125,126,132,],[-31,-23,61,-31,61,-31,-32,-30,61,61,61,-27,-28,-29,-25,-26,-24,61,61,61,61,61,61,61,61,]),'TkWith':([0,1,4,6,8,11,12,13,15,16,18,43,44,46,59,68,70,80,82,87,97,105,107,117,119,120,124,127,129,130,133,135,136,138,139,],[3,3,-12,-15,-17,-19,-16,-13,-18,3,-20,-2,-14,3,-57,-56,3,3,3,-21,3,3,-1,-52,-51,-49,3,3,-53,3,3,3,-55,3,-54,]),'TkChar':([84,108,134,],[111,111,111,]),'TkValorAscii':([7,10,14,21,24,32,37,41,52,60,61,62,63,64,69,71,73,74,75,76,77,81,86,121,123,128,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'$end':([2,43,107,],[0,-2,-1,]),'TkDisyuncion':([22,23,26,27,30,31,34,35,36,38,42,53,54,55,57,58,65,66,72,78,89,90,91,92,93,94,95,96,98,99,100,101,102,103,104,116,],[-58,-31,-60,-23,-59,-46,69,-41,-44,-42,69,-31,-32,-30,-64,-65,-48,-47,-43,69,-63,-27,-28,-29,-25,-26,-24,-34,-33,-39,-35,-36,-38,-37,-40,-61,]),'TkAsignacion':([5,50,],[21,86,]),'TkMenor':([27,36,40,53,54,55,79,90,91,92,93,94,95,],[-23,-31,74,-31,-32,-30,74,-27,-28,-29,-25,-26,-24,]),'TkFrom':([45,],[81,]),'TkInt':([84,108,134,],[112,112,112,]),'TkMayor':([27,36,40,53,54,55,79,90,91,92,93,94,95,],[-23,-31,77,-31,-32,-30,77,-27,-28,-29,-25,-26,-24,]),'TkOf':([131,],[134,]),'TkCorcheteCierra':([27,53,54,55,88,90,91,92,93,94,95,126,],[-23,-31,-32,-30,116,-27,-28,-29,-25,-26,-24,131,]),'TkSuma':([23,27,30,36,40,53,54,55,67,79,88,90,91,92,93,94,95,100,101,102,103,106,125,126,132,],[-31,-23,63,-31,63,-31,-32,-30,63,63,63,-27,-28,-29,-25,-26,-24,63,63,63,63,63,63,63,63,]),'TkOtherwise':([4,6,8,11,12,13,15,18,43,44,59,68,87,105,107,117,119,120,127,129,136,139,],[-12,-15,-17,-19,-16,-13,-18,-20,-2,-14,-57,-56,-21,118,-1,-52,-51,-49,-50,-53,-55,-54,]),'TkComa':([22,23,26,27,30,31,48,49,50,53,54,55,57,58,65,66,83,89,90,91,92,93,94,95,114,115,116,],[-58,-31,-60,-23,-59,-46,-6,85,-5,-31,-32,-30,-64,-65,-48,-47,85,-63,-27,-28,-29,-25,-26,-24,85,-22,-61,]),'TkMod':([23,27,30,36,40,53,54,55,67,79,88,90,91,92,93,94,95,100,101,102,103,106,125,126,132,],[-31,-23,62,-31,62,-31,-32,-30,62,62,62,-27,-28,-29,-25,-26,-24,62,62,62,62,62,62,62,62,]),'TkMayorIgual':([27,36,40,53,54,55,79,90,91,92,93,94,95,],[-23,-31,76,-31,-32,-30,76,-27,-28,-29,-25,-26,-24,]),'TkParAbre':([7,10,14,21,24,32,37,41,52,60,61,62,63,64,69,71,73,74,75,76,77,81,86,121,123,128,],[32,41,41,32,32,32,41,41,32,32,32,32,32,32,41,41,32,32,32,32,32,32,32,32,32,32,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'I_O':([1,16,46,70,80,82,97,105,124,127,130,133,135,138,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'BOOL':([10,14,37,41,69,71,],[34,42,72,78,96,98,]),'ARRAY':([7,10,14,21,28,37,41,56,69,71,73,86,],[26,26,26,26,57,26,26,89,26,26,26,26,]),'SEC':([1,46,70,80,124,130,135,],[4,4,4,4,4,4,4,]),'INSTR1':([1,16,46,70,80,82,97,105,124,127,130,133,135,138,],[13,44,13,13,13,44,44,44,13,44,13,44,13,44,]),'CHAR':([7,10,14,21,37,41,69,71,73,86,],[22,22,22,22,22,22,22,22,22,22,]),'ASIG':([1,16,46,70,80,82,97,105,124,127,130,133,135,138,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'DEC':([3,],[19,]),'DETER0':([125,],[129,]),'COND':([1,16,46,70,80,82,97,105,124,127,130,133,135,138,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'DETER':([1,16,46,70,80,82,97,105,124,127,130,133,135,138,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'IDENT':([20,47,85,],[49,83,114,]),'INSTR':([1,46,70,80,124,130,135,],[16,82,97,105,127,133,138,]),'ARIT':([7,10,14,21,24,32,37,41,52,60,61,62,63,64,69,71,73,74,75,76,77,81,86,121,123,128,],[30,40,40,30,54,67,40,79,88,90,91,92,93,94,40,40,30,100,101,102,103,106,30,125,126,132,]),'INDETER':([1,16,46,70,80,82,97,105,124,127,130,133,135,138,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'INICIO':([0,1,16,46,70,80,82,97,105,124,127,130,133,135,138,],[2,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'TIPO':([84,108,134,],[110,122,137,]),'EXPR':([7,10,14,21,37,41,69,71,73,86,],[29,39,39,51,39,39,39,39,99,115,]),'COND0':([105,],[120,]),'ASIG_ID':([20,47,85,],[48,48,48,]),}

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
  ('DEC -> DEC TkVar IDENT TkDosPuntos TIPO','DEC',5,'p_dec','parser.py',21),
  ('DEC -> TkVar IDENT TkDosPuntos TIPO','DEC',4,'p_dec','parser.py',22),
  ('IDENT -> TkId','IDENT',1,'p_ident','parser.py',31),
  ('IDENT -> ASIG_ID','IDENT',1,'p_ident','parser.py',32),
  ('IDENT -> IDENT TkComa IDENT','IDENT',3,'p_ident','parser.py',33),
  ('TIPO -> TkInt','TIPO',1,'p_tipo','parser.py',46),
  ('TIPO -> TkChar','TIPO',1,'p_tipo','parser.py',47),
  ('TIPO -> TkBool','TIPO',1,'p_tipo','parser.py',48),
  ('TIPO -> TkArray TkCorcheteAbre ARIT TkCorcheteCierra TkOf TIPO','TIPO',6,'p_tipo','parser.py',49),
  ('INSTR -> SEC','INSTR',1,'p_instr','parser.py',58),
  ('INSTR -> INSTR1','INSTR',1,'p_instr','parser.py',59),
  ('SEC -> INSTR INSTR1','SEC',2,'p_sec','parser.py',65),
  ('INSTR1 -> ASIG','INSTR1',1,'p_instr1','parser.py',71),
  ('INSTR1 -> I_O','INSTR1',1,'p_instr1','parser.py',72),
  ('INSTR1 -> COND','INSTR1',1,'p_instr1','parser.py',73),
  ('INSTR1 -> DETER','INSTR1',1,'p_instr1','parser.py',74),
  ('INSTR1 -> INDETER','INSTR1',1,'p_instr1','parser.py',75),
  ('INSTR1 -> INICIO','INSTR1',1,'p_instr1','parser.py',76),
  ('ASIG -> TkId TkAsignacion EXPR TkPuntoYComa','ASIG',4,'p_asig','parser.py',82),
  ('ASIG_ID -> TkId TkAsignacion EXPR','ASIG_ID',3,'p_asig_id','parser.py',88),
  ('ARIT -> TkNum','ARIT',1,'p_arit','parser.py',94),
  ('ARIT -> TkParAbre ARIT TkParCierra','ARIT',3,'p_arit','parser.py',95),
  ('ARIT -> ARIT TkSuma ARIT','ARIT',3,'p_arit','parser.py',96),
  ('ARIT -> ARIT TkResta ARIT','ARIT',3,'p_arit','parser.py',97),
  ('ARIT -> ARIT TkMult ARIT','ARIT',3,'p_arit','parser.py',98),
  ('ARIT -> ARIT TkDiv ARIT','ARIT',3,'p_arit','parser.py',99),
  ('ARIT -> ARIT TkMod ARIT','ARIT',3,'p_arit','parser.py',100),
  ('ARIT -> TkValorAscii TkCaracter','ARIT',2,'p_arit','parser.py',101),
  ('ARIT -> TkId','ARIT',1,'p_arit','parser.py',102),
  ('ARIT -> TkResta ARIT','ARIT',2,'p_nega','parser.py',119),
  ('BOOL -> BOOL TkConjuncion BOOL','BOOL',3,'p_bool','parser.py',125),
  ('BOOL -> BOOL TkDisyuncion BOOL','BOOL',3,'p_bool','parser.py',126),
  ('BOOL -> ARIT TkMenor ARIT','BOOL',3,'p_bool','parser.py',127),
  ('BOOL -> ARIT TkMenorIgual ARIT','BOOL',3,'p_bool','parser.py',128),
  ('BOOL -> ARIT TkMayor ARIT','BOOL',3,'p_bool','parser.py',129),
  ('BOOL -> ARIT TkMayorIgual ARIT','BOOL',3,'p_bool','parser.py',130),
  ('BOOL -> EXPR TkIgual EXPR','BOOL',3,'p_bool','parser.py',131),
  ('BOOL -> TkParAbre BOOL TkParCierra','BOOL',3,'p_bool','parser.py',132),
  ('BOOL -> TkFalse','BOOL',1,'p_bool','parser.py',133),
  ('BOOL -> TkTrue','BOOL',1,'p_bool','parser.py',134),
  ('BOOL -> TkNegacion BOOL','BOOL',2,'p_bool','parser.py',135),
  ('BOOL -> TkId','BOOL',1,'p_bool','parser.py',136),
  ('CHAR -> TkId','CHAR',1,'p_char','parser.py',154),
  ('CHAR -> TkCaracter','CHAR',1,'p_char','parser.py',155),
  ('CHAR -> TkCaracter TkSiguienteCar','CHAR',2,'p_char','parser.py',156),
  ('CHAR -> TkCaracter TkAnteriorCar','CHAR',2,'p_char','parser.py',157),
  ('COND -> TkIf BOOL TkHacer INSTR COND0','COND',5,'p_cond','parser.py',170),
  ('COND0 -> TkOtherwise TkHacer INSTR','COND0',3,'p_cond0','parser.py',176),
  ('COND0 -> TkEnd','COND0',1,'p_cond0','parser.py',177),
  ('INDETER -> TkWhile BOOL TkHacer INSTR TkEnd','INDETER',5,'p_indeter','parser.py',186),
  ('DETER -> TkFor TkId TkFrom ARIT TkTo ARIT DETER0','DETER',7,'p_deter','parser.py',192),
  ('DETER0 -> TkStep ARIT TkHacer INSTR TkEnd','DETER0',5,'p_deter0','parser.py',198),
  ('DETER0 -> TkHacer INSTR TkEnd','DETER0',3,'p_deter0','parser.py',199),
  ('I_O -> TkRead TkId TkPuntoYComa','I_O',3,'p_i_o','parser.py',208),
  ('I_O -> TkPrint EXPR TkPuntoYComa','I_O',3,'p_i_o','parser.py',209),
  ('EXPR -> CHAR','EXPR',1,'p_expr','parser.py',215),
  ('EXPR -> ARIT','EXPR',1,'p_expr','parser.py',216),
  ('EXPR -> ARRAY','EXPR',1,'p_expr','parser.py',217),
  ('EXPR -> TkId TkCorcheteAbre ARIT TkCorcheteCierra','EXPR',4,'p_expr','parser.py',218),
  ('EXPR -> TkId','EXPR',1,'p_expr','parser.py',219),
  ('ARRAY -> ARRAY TkConcatenacion ARRAY','ARRAY',3,'p_array','parser.py',231),
  ('ARRAY -> TkShift ARRAY','ARRAY',2,'p_array','parser.py',232),
  ('ARRAY -> TkId','ARRAY',1,'p_array','parser.py',233),
]
