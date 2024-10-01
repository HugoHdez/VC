Estas tareas han sido realizadas de manera conjunta por ambos miembros del grupo 23 (David Marrero Sosa y Hugo Hernández Morales).

## Práctica 2. Funciones básicas de OpenCV

**TAREA 1:** Sumamos los valores de los píxeles blancos de cada fila usando la funcion "reduce" de cv2. Calculamos cuantos píxeles hay por fila dividiendo entre 255 (ya que es el valor de un pixel blanco). Obtenemos la fila que tiene mas píxeles blancos haciendo uso de la función "max" de numpy, y para determinar que filas superan o igualan el 95% de píxeles blancos respecto al máximo (0.95*maxfil) usamos la función "where" de numpy donde guardamos las filas que superen dicho umbral. Finalmente, imprimimos por pantalla los resultados que hemos ido calculando.

![canny_t1](https://github.com/user-attachments/assets/0322e3c4-f6a2-4625-b8f3-b0f9e9bed099)

**TAREA 2:** Primero convertimos la imagen a gris y la suavizamos mediante la función "GaussianBlur" de cv2. Tras ello, calculamos ambas direcciones del sobel para obtener la imagen con los bordes combinados usando "Sobel" de cv2 en eje vertical y en el horizontal, después usamos "add" de cv2 para combinarlos. Convertimos la imagen de Sobel a 8 bits mediante "convertScaleAbs" de cv2. Continuamos obteniendo la imagen ya umbralizada mediante "threshold" de cv2 para mediante un umbral predefinido asignar blanco o negro a los píxeles de la imagen. Después, al igual que en la tarea 1, sumamos los valores de los píxeles blancos de cada fila y dividimos entre 255 para obtener cuantos píxeles hay en cada fila. Tras ello determinar la fila con más blancos y buscamos que filas superan el 95% de la fila con mas píxeles blancos. Tras ello, hacemos lo mismo para las columnas. A continuación imprimimos los datos que calculamos. Finalmente, dibujamos lineas, haciendo uso de la funcion "line" de cv2, en las filas y columnas que superen los umbrales y imprimimos la imagen con las lineas.

![sobel_t2](https://github.com/user-attachments/assets/33141379-16da-4f70-bc7b-a8d08f0dcee9)
