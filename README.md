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

