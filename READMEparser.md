Manuel Rodriguez 13-11223
Ian Goldberg 14-10406

Fase II proyecto para la clase CI-3725

C�mo correr el programa:

Para ejecutar el parser se debe ejecutar en la terminal la instrucci�n ./BasicTran <Nombre del Archivo>

Estructura de la Gram�tica:

La gram�tica fue estructurada siguiendo un modelo en el cual cada tipo de dato y cada tipo de instrucci�n posee su propia etiqueta, es decir, las operaciones que 
producen expresiones aritm�ticas se encuentran en una etiqueta distinta a las operaciones que producen booleanos, y la instrucci�n del ciclo for se 
encuentra en una etiqueta distinta a la del ciclo while, por ejemplo.

Las instrucciones que pueden poseer cualquier instrucci�n utilizan una etiqueta llamada EXPR que se encarga de direccionar hacia las etiquetas de cualquier tipo de
expresion, debido a esta decisi�n por parte de nuestro equipo estamos concientes de que exiten alertas de tipo reduce/reduce al momento de ejecutar el parser debido a
que podemos llegar al mismo resultado tomando caminos distintos (las expresiones poseen estados finales en com�n)

Estructura del �rbol:

Para formar el �rbol que contiene la informaci�n del programa se cre� una clase llamada InstrTree, a la cual se le pasa como primer par�metro un string con una 
etiqueta o identificador que haga referencia a la operaci�n realizada en ese nodo, el segundo par�metro son los hijos que se desprender�n de ese nodo, es decir,
los operandos y el tercero es el padre de ese nodo, es decir, el operador.

Ejemplo: a <- b, en esta operaci�n se crear�a la instancia InstrTree("Asignaci�n", [p[1], p[2]], p[2]), siendo p[1] = a, p[2] = <- y p[3] = b

Siendo los hijos nodos o None y los padres strings o None. Este �ltimo caso hace referencia a cuando se pasa por un estado que no se desea mostrar.

Ejemplos de distintas instrcciones

Asignaci�n:


