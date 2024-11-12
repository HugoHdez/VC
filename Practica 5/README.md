Estas tareas han sido realizadas de manera conjunta por ambos miembros del grupo 23 ([David Marrero Sosa](https://github.com/deivinot) y [Hugo Hernández Morales](https://github.com/HugoHdez)).

## Práctica 5. Detección y caracterización de caras

Hemos elegido utilizar *Deepface* y *dlib* para la deteción de caras. Hemos hecho uso de *Deepface* para la optención de información, en este caso, de la emoción predominante de la persona (aunque solo utilizamos "happy", "neutral" y "sad" para aplicar filtros) y también, en el caso de que esta sea "happy", para la obtención de las coordenadas de los ojos. Por otro lado, hemos usado dlib para la obtención de coordenadas de puntos determinados más complejos, el punto central de la cara y la parte de los ojos más cercana a nariz, para la emoción predominante "neutral" y "sad" respectivamente. Con la información obtenida, se pone un filtro en la zona deseada.

![output_video (2)](<demo/output_video.gif>)


### Pasos de implementación

Primero, cargamos las imágenes y los diferentes parámetros, como la intefaz de detectores de cara del dlib. Ahora capturaremos la webcam y analizaremos frame a frame, con *DeepFace*, detectando los rasgos carácterísticos de una cara, que, en este caso, simplemente será el género y la emoción reflejada del sujeto en cuestión. Haremos lo propio, en cada uno de los casos de emociones, con *dlib* para obtener los puntos característicos de la cara.

Como se explicó en el apartado anterior, dependiendo de la emoción que detectemos con ayuda de DeepFace, aplicaremos diferentes filtros. Primero, si la emoción es 'sad', es decir, triste, el filtro serán unas gotas, emulando el llanto. Para ello, detectaremos la cara, ojos y puntos carácteristicos con ayuda de la función *SingleFaceEyesDetection()* del archivo FaceDlibs.py, que contiene las funciones que usaremos de *dlib* proporcionadas por el profesorado. A partir de estos datos, podemos conseguir las coordenadas y dimensiones tanto de la cara como de los ojos para saber la zona en que aplicaremos el filtro. Además, calculamos el ángulo de rotación entre los ojos izquierdo y derecho, con la función *atan2()* (arcotangente) para poder obtener la matriz de rotación, que conseguiremos con *getRotationMatrix2D()*, aplicando así el giro al filtro de las gotas respecto a la cara en tiempo real, y tener un efecto más realista. Aplicaremos la rotación sobre el filtro ayudándonos de la función *warpAffine()* que hace uso de la matriz de rotación calculada. Hecho esto, aplicaremos las gotas justo debajo de los ojos, ayudándonos de los puntos carácterísticos calculados anteriormente (izq. pto. 39, dcho. pto. 42). 

![alt text](<demo/sad_demo.png>)
![output_video (2)](<demo/output_video_sad.gif>)


A continuación, haremos algo parecido para la emoción 'happy', es decir, felicidad, detectada con DeepFace. Colocaremos de igual forma, sobre los ojos unos emoticonos representativos de esta emoción. 

![output_video (2)](<demo/output_video_happy.gif>)


Para finalizar, cuando la cara analizada tenga una emoción neutral, es decir, no muestre ninguna emoción, pondremos un filtro emulando a 'Papá Noel', con su característico gorro y barba. Para este caso, al ser un filtro no simétrico, usamos el punto 27 de los puntos carácterísticos, que corresponde con el punto superior del puente de la nariz, entre las cejas, como referencia. Ajustamos con estas coordenadas para centrar el filtro en la cara.

![output_video (2)](<demo/output_video_santa.gif>)

Una vez acabada la demostración, se concluirá pulsando la tecla 'ESC'. 

