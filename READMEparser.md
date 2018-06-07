## Integrantes
Manuel Rodriguez 13-11223
Ian Goldberg 14-10406

## Fase II proyecto CI-3725

## Como correr el programa:

Para ejecutar el parser se debe ejecutar en la terminal la instrucción: 
"./BasicTran <nombre del Archivo>"

En caso de existir algún error, revisar que el script tiene los permisos necesarios para ser ejecutado. También se puede presentar el caso en el que archivo ingresado no existe o no se le asigna un argumento al script, en ambos casos el mismo arrojará un error de “Error al procesar el archivo de entrada”

## Estructura de la Gramática

La gramática fue estructurada siguiendo un modelo en el cual cada tipo de dato y cada tipo de instrucci�n posee su propia etiqueta, es decir, las operaciones que 
producen expresiones aritm�ticas se encuentran en una etiqueta distinta a las operaciones que producen booleanos, y la instrucci�n del ciclo for se 
encuentra en una etiqueta distinta a la del ciclo while, por ejemplo.

Las instrucciones que pueden poseer cualquier instrucci�n utilizan una etiqueta llamada EXPR que se encarga de direccionar hacia las etiquetas de cualquier tipo de
expresion, debido a esta decisi�n por parte de nuestro equipo estamos concientes de que exiten alertas de tipo reduce/reduce al momento de ejecutar el parser debido a
que podemos llegar al mismo resultado tomando caminos distintos (las expresiones poseen estados finales en com�n)

## Estructura del �rbol

Para formar el �rbol que contiene la informaci�n del programa se cre� una clase llamada InstrTree, a la cual se le pasa como primer par�metro un string con una 
etiqueta o identificador que haga referencia a la operaci�n realizada en ese nodo, el segundo par�metro son los hijos que se desprender�n de ese nodo, es decir,
los operandos y el tercero es el padre de ese nodo, es decir, el operador.

Ejemplo: a <- b, en esta operaci�n se crear�a la instancia InstrTree("Asignaci�n", [p[1], p[2]], p[2]), siendo p[1] = a, p[2] = <- y p[3] = b

Siendo los hijos nodos o None y los padres strings o None. Este �ltimo caso hace referencia a cuando se pasa por un estado que no se desea mostrar.

## Lectura del arbol

### Instruccion de un solo operador
Las instrucciones con operadores simples (<-, +, *, entre otros) se leen de la forma
al primer hijo *se aplica* la instrucción con el segundo hijo.
Ejemplo de a <- 5: 
<-
    a
    5

### Instrucciones compuestas
Instrucciones con mas datos especificos (if, for, while) tienen hijos que identifican
las etapas de estas instrucciones. Los hijos pueden ser instrucciones como las del caso anterior.

Ejemplo de if a > b -> print x;
begin
        if
                condicion
                        >
                                a
                                b
                exito
                        print
                                x

### Declaración de variables
Los hijos de las declaraciones de variables son las variables bajo el alcance de un
"var" y el identificador del tipo de la variable.
Ejemplo de var a : bool:
with
        var
                a
                tipo
                        bool

Ejemplo de var a <- hola : array[m] of int
with
        var
                <-
                        a
                        hola
                array
                        size
                                m
                        tipo
                                int

