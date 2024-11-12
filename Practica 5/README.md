Estas tareas han sido realizadas de manera conjunta por ambos miembros del grupo 23 ([David Marrero Sosa](https://github.com/deivinot) y [Hugo Hernández Morales](https://github.com/HugoHdez)).

## Práctica 5. Detección y caracterización de caras

Hemos elegido utilizar Deepface y dlib para la decteción de caras. Deepface ha sido usado para la optención de información, en este caso, la emoción predominante de la persona (aunque solo utilizamos "happy", "neutral" y "sad" para aplicar filtros) y tambien en el caso de que esta sea "happy" para la obtención de las coordenadas de los ojos. Por otro lado, hemos usado dlib para la obtención de coordenadas de puntos determinados más complejos, el punto central de la cara y la parte de los ojos más cercana a nariz, para la emoción predominante "neutral" y "sad" respectivamente. Con la información obtenida, se pone un filtro en la zona deseada.

![output_video (2)](https://github.com/user-attachments/assets/48fa5751-448d-4784-ab54-590e32a7d463)


### Pasos de implementación

Primero cargamos las imagenes y los diferentes parametros como la intefaz de detectores de cara del dlib.
