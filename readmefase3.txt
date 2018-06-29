## Integrantes
Manuel Rodriguez 13-11223
Ian Goldberg 14-10406

## Fase III proyecto CI-3725

## Como correr el programa:

Para ejecutar el parser se debe ejecutar en la terminal la instrucci�n: 
"./BasicTran <nombre del Archivo>"

En caso de existir alg�n error, revisar que el script tiene los permisos necesarios para ser ejecutado. Tambi�n se puede presentar el caso en el que archivo ingresado no existe o no se le asigna un argumento al script, en ambos casos el mismo arrojar� un error de �Error al procesar el archivo de entrada�

## Obtenci�n del tipo de cada variable y formaci�n de la tabla de s�mbolos.

Para la obtenci�n del tipo de una variable se coloc� un atributo nuevo en el �rbol con el cual mantenemos el control de qu� tipo es un identificador o una expresi�n.
Al entrar en la etiqueta "TIPO" se guarda en el atributo antes mencionado el tipo por el cual se entr� a la etiqueta. Este atributo es utilizado en la etiquetas 
etiquetas DEC, DEC0 y DEC1, las cuales se encargan de declarar las variables. 
Por otro lado cada vez que se ingresa a la etiqueta IDENT se guarda en una lista llamada "variables" el string asociado al TkId por el que se entr� a la etiqueta.
Haciendo uso del atributo y la lista mencionados empleamos estos dos en la etiqueta DEC, DEC0 y DEC1 para vincular estas dos (cada variable con su tipo) e ingresarlos a
un diccionario en el cual el nombre de la variable es la llave y el tipo el valor.

## Almacenaje de las tablas de s�mbolos.

Al terminar una declaraci�n, es decir, en las etiquetas de DEC, DEC0 y DEC1 luego de hacer el vinculo y la creaci� del diccionario especificada anteriormente se procede 
a guardar el diccionario en una lista llamada "total_variables"

## Errores de tipo.

Mediante el uso del atributo a�adido al �rbol en esta entrega y el diccionario se puede obtener el tipo con el cual fue declarada cada variable. 
Cuando entramos en la etiqueta EXPR, que es la que maneja las expresiones y sus operaciones, podemos obtener el tipo de sus expresiones mediante las variables
utilizadas en ellas. Una vez obtenidas estas se guardan en el atributo del nodo del �rbol. 
Cuando se va a realizar una operaci�n de cierto tipo sobre una o m�s expresiones se revisa el atributo "tipo" de estos nodos, de forma que podamos verificar que
este es el tipo indicado para poder llevarse a cabo dicha operaci�n. De no pasar la verificaci�n se imprime en consola un error de tipo espec�fico para el caso.

## Variables no declaradas.

Al entrar en la etiqueta EXPR en el caso en el que se tiene TkId se verifica en los diccionarios almacenados en "total_variables" si se contiene almacenada la
variable que se pretende usar. De no encontrarse la variable se imprime un error en consola diciendo que la variable en cuesti�n no fue declarada.

## Redeclaraci�n de variables.

Una vez se est� en la etiqueta DEC, DEC0 o DEC1 y se recibe un nuevo TkId de una variable a declarar se revisan los diccionarios correspondientes en 
"total_variables" y adem�s se revisa la lista de variables con el fin de verificar si se ha declarado una variable con ese mismo nombre anteriormente.
De ser as� se procede a imprimir en consola el error correspondiente.

