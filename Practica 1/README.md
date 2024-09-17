Estas tareas han sido realizadas de manera conjunta por ambos miembros del grupo 23 (David Marrero Sosa y Hugo Hernández Morales).

## VISIÓN POR COMPUTADOR: PRÁCTICA 1.

**TAREA 1:** Recorremos, por filas y columnas, los 800 píxeles, de 100 en 100. Cada vez que nos encontremos en una casilla par o impar en ambas fila y columna, haremos blanco los pixeles de la posición en que nos encontramos hasta la posición más 100 (para hacer el cuadrado blanco).

**TAREA 2:** Creamos rectangulos con la función rectangle de OpenCV, dejando espacio entre los mismos para crear líneas negras con el fondo, que es negro.

**TAREA 3:** Misma que la tarea uno, pero con la función rectangle de OpenCV.

**TAREA 4:** Modificamos los colores de la codificación RGB, invirtiendo el color Rojo, y aumentando y disminuyendo el brillo del canal G y B con la función clip de NumPy, que fuerza que los valores estén entre 0 y 255 (por si la suma o resta hace disminuir estos valores).

**TAREA 5:** Con la función minMaxLoc de OpenCV, encontramos los valores máximos y mínimos de color y su localización por frame, ayudándonos de la función circle de OpenCV para rodear de ROJO el tono más claro y de AMARILLO el tono más oscuro.

**TAREA 6:** Aplicamos una serie de filtros con diferentes colores de estilo PopArt como referencia, ayudándonos de la función where de NumPy para aplicar este filtro en los canales de color, haciendo que, si un canal supera o no un umbral, se convierta o no al valor del canal RGB de este color.