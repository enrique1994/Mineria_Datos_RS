# Mineria_Datos_RS

1.-Descargar la biblioteca de python la cual nos ayudara a descargar el corpus que requerimos para el algoritmo.

2.-Crear el diccionario de palabras que expresen algun sentimiento personal.

3.-Se modifican las siguiente lineas del algoritmo de la biblioteca con
Linea 11: s=open("training_NombreTema.txt","w");

Linea 13: s=open("test_NombreTema.txt","w");

Linea 17:	for tweet in Twitter().search('NombreTema',start=1,count=100):

En la linea 11 se usa la palabra training que significa entrenamiento el cual sera el archivo que nosotros utilizaremos para poder entrenar el clasificador de exitos.

En la linea 13 se usa la palabra test para probar el algoritmo de naive bayes el cual nos indicara que tan exitoso es el algoritmo implementado.

En la linea 17 se usa un for ya que se extraeran de la base de datos del twitter 100 tweets del NombreTema en tiempo real

Lineas posteriores de estas mencionadas al momento de descargar los tweets se utiliza una funcion:tweet.text.encode('utf-8') la cual nos permite codificar el tipo de texto para que pueda python poderlo manejar como cadena.

4.-Por ultimo se utilizara un algoritmo para quitar los acentos ya que para PLN en algunos puntos el acento nos puede ocasionar problemas por lo cual se tomo la decision de cambiar las letras con acentos, con letras sin acentos, de ahi procedemos a etiquetar los tweets a traves de un algoritmo automatico de etiquetado el cual nos permitira determinar si es una noticia u opinion todo dependiendo del diccionario anteriormente creado.

5.-En el mismo programa de python del paso 4 se procede a entrenar el clasificador bayesiano con el archivo training_NombreTema.

6.-En el mismo programa se evalua el algoritmo con el clasificador bayesiano de la biblioteca de Pattern pero con la diferencia de que se llama test_NombreTema, con el numero de palabras implementadas en el algoritmo mencionado en el paso 2 nos arroja en las pruebas un indice del 80% acertados.
