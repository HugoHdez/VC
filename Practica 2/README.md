Estas tareas han sido realizadas de manera conjunta por ambos miembros del grupo 23 (David Marrero Sosa y Hugo Hernández Morales).

## Práctica 2. Funciones básicas de OpenCV

**TAREA 1:** Sumamos los valores de los píxeles blancos de cada fila usando la funcion "reduce" de cv2. Calculamos cuantos píxeles hay por fila dividiendo entre 255 (ya que es el valor de un pixel blanco). Obtenemos la fila que tiene mas píxeles blancos haciendo uso de la función "max" de numpy, y para determinar que filas superan o igualan el 95% de píxeles blancos respecto al máximo (0.95*maxfil) usamos la función "where" de numpy donde guardamos las filas que superen dicho umbral. Finalmente, imprimimos por pantalla los resultados que hemos ido calculando.

![canny_t1](https://github.com/user-attachments/assets/0322e3c4-f6a2-4625-b8f3-b0f9e9bed099)
