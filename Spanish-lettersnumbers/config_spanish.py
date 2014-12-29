# -*- coding: utf-8 -*-


########## Audio ############################
save_audio = False  ####### Set to True to save the audio, but it needs python 2.5
use_frequency= 44100
#use_encoding= "Lin24" #doesn't work
use_fileformat="WAV"
use_channels="Mono"

##### Fonts ###############
fontsize = 18
fontsize_test = 32
fontname = "Courier"

### Texts ###############

instructions="""¡Bienvenido!

El test dura aproximadamente 5 minutos.

En este test deberá leer en voz alta lo más rápido posible una serie de 50  letras o números que aparecerán en 5 filas de 10 elementos. 
Antes de cada serie de letras o números aparecerán una serie de guiones que indican la posición de las letras/números. 
Presione la barra espaciadora luego de identificar la serie de guiones, y deletree la serie de letras/números  lo más rápido posible *en voz alta* y vuelva a presionar la barra cuando haya finalizado (pero no antes). (Recuerde deletrear si  por ej. aparece o s p d a, lea o, ese, de, pe, a; 1 5 4 3 2: uno cinco cuatro tres dos) 

Antes del test tendrá una pequeña sesión de práctica.

Si tiene alguna otra pregunta, por favor, realícela en este momento.

Presione la barra espaciadora para continuar..."""

before_practice="""En la sesión de práctica aparecerán una serie de 50 letras 'o', 'a', 's', 'd' y 'p' ordenadas al azar y luego de números '2', '6', '9', '4' y '7'  ordenados al azar . Cada serie es precedida por una pantalla con guiones. Recuerde empezar a *deletrear* en voz alta tan pronto como vea la serie de letras, y presione la barra espaciadora cuando haya finalizado.

Presione la barra espaciadora para continuar
"""
before_test1="""A continuación empezará el test. ¿Tiene preguntas?

En la primera sesión del experimento aparecerán 8 series de 50 letras 'o', 'a', 's', 'd' y 'p' ordenadas al azar.

Recuerde empezar a leer tan pronto como vea la serie de letras, y presione la barra espaciadora cuando haya finalizado (pero no antes).

Presione la barra espaciadora para continuar..."""
before_test2="""
En la siguiente sesión del experimento aparecerán 8 series de 50 números '2', '6', '9', '4' y '7'  ordenados al azar.

Recuerde empezar a leer tan pronto como vea la serie de números, y presione la barra espaciadora cuando haya finalizado (pero no antes).

Presione la barra espaciadora para continuar
"""

good_bye_text ="El test ha finalizado. Gracias por su participación."
end_set="El set ha finalizado"

######## ITEMS
practice_items = {
"letters":
[
"""
p a d o s p d o s a
s d p a o a s p d o
d p a o s o d a s p
s d p a o s d p a o
p s a d o d p s o a
""",
"""
7 9 6 4 2 6 2 9 4 7
6 2 7 4 9 2 9 7 4 6
9 2 7 6 4 9 7 6 2 4
6 9 7 2 4 9 7 4 2 6
7 6 4 2 9 7 4 9 2 6
"""
]
}

items= {
"letters":
[
"""
s p d o a p d a s o
a s d p o a d s p o
d p o a s o d s p a
s o d p a s p a o d
a s p o d p d o a s
""",
"""
a o s p d o a d p s
p d s o a s o d p a
a p s d o s o d a p
d s p o a p d o a s
p d o a s a d p o s
""",
"""
a d p s o d s a p o
s a d o p s a o d p
d p a s o p d s o a
o p s d a s o d p a
p o s d a d p s a o
""",
"""
d o s p a p d o s a
p o d a s d p a s o
s o a d p o d p s a
o d s p a o p a d s
p a o d s a o s d p
""",
"""
s o d a p s o d a p
d a s p o p o d a s
o p a d s o a s d p
d o a s p o a s p d
p o a d s p s a o d
""",
"""
p a o d s o a d s p
o d p a s p o a d s
a o d p s a o p d s
d a o p s o d p a s
a o d p s p d a o s
""",
"""
a p o s d s o a p d
o a d p s p s o a d
s d p a o d s p o a
o d s p a s d a o p
a p o s d o s p d a
""",
"""
s a d p o s o p d a
d s a o p o d a s p
a o d p s d p o a s
s a d p o d s a o p
d s p o a d o p s a
"""
],
"numbers":
["""
9 6 4 2 7 6 2 7 9 4
6 2 7 4 9 2 4 7 6 9
6 9 7 4 2 6 2 9 4 7
2 4 7 9 6 9 7 4 6 2
6 2 4 9 7 2 9 6 7 4
""",
"""
4 7 6 9 2 6 7 2 4 9
2 4 7 6 9 2 9 6 7 4
6 2 9 4 7 9 2 6 4 7
9 6 7 2 4 6 9 2 7 4
2 4 7 6 9 6 7 2 9 4
""",
"""
2 4 9 7 6 2 4 6 7 9
4 9 6 7 2 7 2 6 9 4
9 4 7 2 6 9 6 2 4 7
2 9 7 4 6 2 6 4 9 7
4 2 6 7 9 7 6 2 9 4
""",
"""
6 7 9 2 4 9 7 6 4 2
7 4 9 6 2 7 6 4 2 9
4 9 7 2 6 2 7 4 9 6
2 9 6 4 7 9 2 4 7 6
2 7 9 4 6 9 4 7 6 2
""",
"""
9 4 7 6 2 9 2 4 6 7
6 7 2 9 4 2 6 4 7 9
2 4 9 7 6 4 6 2 7 9
2 4 7 6 9 4 2 6 7 9
4 6 2 9 7 4 2 6 7 9
""",
"""
9 2 6 4 7 2 4 9 6 7
9 2 6 7 4 7 6 4 2 9
4 7 2 9 6 4 9 2 6 7
2 6 7 4 9 4 6 7 2 9
7 9 4 2 6 7 4 9 6 2
""",
"""
6 2 9 4 7 2 6 9 7 4
6 2 9 4 7 4 6 7 9 2
6 7 9 2 4 2 4 6 7 9
7 6 9 4 2 9 6 2 7 4
9 4 6 2 7 6 7 4 2 9
""",
"""
2 7 6 4 9 2 4 9 6 7
2 9 6 7 4 9 2 4 7 6
7 9 6 2 4 2 4 9 6 7
9 2 6 4 7 6 7 9 2 4
2 6 4 9 7 9 2 6 4 7
"""
]

}


