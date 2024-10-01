Estas tareas han sido realizadas de manera conjunta por ambos miembros del grupo 23 (David Marrero Sosa y Hugo Hernández Morales).
**autores** https://github.com/deivinot

## Práctica 2. Funciones básicas de OpenCV

**TAREA 1:** Sumamos los valores de los píxeles blancos de cada fila usando la funcion "reduce" de OpenCV. Calculamos cuantos píxeles hay por fila dividiendo entre 255 (ya que es el valor de un pixel blanco). Obtenemos la fila que tiene mas píxeles blancos haciendo uso de la función "max" de numpy, y para determinar que filas superan o igualan el 95% de píxeles blancos respecto al máximo (0.95*maxfil) usamos la función "where" de numpy donde guardamos las filas que superen dicho umbral. Finalmente, imprimimos por pantalla los resultados que hemos ido calculando.

![canny_t1](https://github.com/user-attachments/assets/0322e3c4-f6a2-4625-b8f3-b0f9e9bed099)

**TAREA 2:** Primero convertimos la imagen a gris y la suavizamos mediante la función "GaussianBlur" de OpenCV. Tras ello, calculamos ambas direcciones del sobel para obtener la imagen con los bordes combinados usando "Sobel" de OpenCV en eje vertical y en el horizontal, después usamos "add" de OpenCV para combinarlos. Convertimos la imagen de Sobel a 8 bits mediante "convertScaleAbs" de OpenCV. Continuamos obteniendo la imagen ya umbralizada mediante "threshold" de OpenCV para mediante un umbral predefinido asignar blanco o negro a los píxeles de la imagen. Después, al igual que en la tarea 1, sumamos los valores de los píxeles blancos de cada fila y dividimos entre 255 para obtener cuantos píxeles hay en cada fila. Lo siguiente es determinar la fila con más blancos y buscamos que filas superan el 95% de la fila con mas píxeles blancos. Tras ello, hacemos lo mismo para las columnas. A continuación imprimimos los datos que calculamos. Finalmente, dibujamos lineas, haciendo uso de la funcion "line" de OpenCV, en las filas y columnas que superen los umbrales y imprimimos la imagen con las lineas.

![sobel_t2](https://github.com/user-attachments/assets/33141379-16da-4f70-bc7b-a8d08f0dcee9)

**TAREA 3: Propuesta de modificaciones de vídeo desde la webcam** En esta tarea, hemos realizado cuatro usos de los conocimientos adquiridos en estas dos últimas prácticas:
- Uso número 1: Canny
    Aplicamos el algoritmo Canny para la detección de bordes de una imagen. Para ello, primero debemos convertir cada frame del video a escala de colores grises. A continuación, aplicamos desenfoque con el fin de reducir el ruido de la imagen y evitar detecciones falsas. Esto lo hacemos con la función de OpenCV GaussianBlur(). Luego, aplicamos la función Canny() al frame desenfocado para detectar estos mismos bordes, ajustando los bordes fuertes (Threshold1) y débiles (Threshold2). 

- Uso número 2: Sobel
    Aplicamos el algoritmo Sobel para la detección de bordes de una imagen. Al igual que en el anterior, primero convertimos los frames a escalas de grises y aplicamos desenfoque con las mismas funciones. A continuación, detectamos los bordes con la función Sobel(), pero para ambas direcciones del frame, es decir, en Vertical (Y) y Horizonatal (X). Una vez hecho esto, combinamos los píxeles de ambas detecciones en una misma imagen con la función add() de OpenCV. A continuación, calculamos la magnitud del gradiente para calcular los bordes en todas las direcciones (no solo X e Y) y conseguir un resaltado de los bordes mayor y normalizamos el resultado a entero de 8 bits sin signo (uint8). Para finalizar, aplicamos umbralizado binario a la magnitud del gradiente en la imagen de la detección de los bordes combinados para conseguir bordes más definidos, con la función threshold().

- Uso número 3: Umbralizado binario
    Aplicamos umbralización binaria con la función threshold() y THRESH.BINARY de los frames convertidos a escala de grises. Aplicamos un umbral de 150, en el que, los píxeles que superen dicho umbral, se convertirán en negro, y si no, en blanco.

- Uso número 4: Cartoon
    Convertiremos la imagen en una imagen tipo Cartoon o dibujo animado. Para ello, primero aplicaremos un desenfoque a los frames en gris con la función medianBlur(). Luego, para añadir en la imagen bordes, tal y como son estos dibujos, con la función adaptiveThreshold(), detectaremos bordes haciendo uso de la umbralización adaptativa, ayudándonos también de ADAPTIVE_THRESH_MEAN_C Y THRESH_BINARY dentro de la misma función. Para finalizar, aplicaremosd filtrado bilateral de colores a los frames originales para suavizar los colores con la función bilateralFilter(). Combinaremos la imagen de la detección de bordes con la imagen suavizada haciendo uso de la función bitwise_and() y tendremos el output de la imagen Cartoon.

![t3](https://github.com/user-attachments/assets/b554d1c9-7d48-4572-b567-c65a82525605)


**TAREA 4:** La última tarea que realizaremos consiste en la detección de caras y su respectivo pixelado en tiempo real y también su umbralizado (2 tareas distintas).

- Pixelado: Primero cargamos un clasificador en cascada preentrenado que se utiliza para la detección de rostros en imágenes o videos. Después, creamos una funcion para píxelar la cara a la cual se le pasa por parámetro la imagen a pixelar y número de bloques del pixelado y devuelve la imagen pixelada dividiendo la imagen en bloques que agrupan píxeles calculando la media de su color. Luego, para reemplazar la cara pixelada en la imagen a tiempo real, usamos la función "detectMultiScale" de OpenCV, que se ayuda del objeto anterior face_cascade del clasificador de caras para hacer la detección. Así, recorremos el bloque de la cara detectada y aplicamos el pixelado con la función creada anteriormente y reemplazamos la zona de interés (face_roi, que se corresponde con la cara sin pixelar) por la cara pixelada.

![pixelado](https://github.com/user-attachments/assets/449266cc-03cc-483b-960a-d046f83c0614)

- Umbralizado: Seguimos la misma técnica para la detección de cara (detectMultiScale) y, al recorrer la zona de interés, en vez de sustituir la misma por la cara pixelada, aplicamos la función "threshold_face" para umbralizarla. En esta función, convertimos a escala de grises la imagen y aplicamos la función de umbralizado "threshold" con umbralizado "THRESH_OTSU" que determina automáticamente el umbral de una imagen. Para finalizar, convertimos la imagen de escala de grises a BGR.

![t4_umbral](https://github.com/user-attachments/assets/ce3f6631-c8c6-4b25-acbe-ff7a67857908)

  
