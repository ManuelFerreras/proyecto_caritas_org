from colores import *

lineas = 119
vacio = "|"+ (" " * (lineas-2)) + "|\n"
cuadro = " " + "_" * (lineas-2)
cuadro += "\n"

def texto_menu(max_donacion):
    cartel_caritas = vacio + """|              ________        ___         _____      ___________  __________        ___         ______               |
|             |               /   \       |     \          |            |           /   \       |                     |
|             |              /     \      |      \         |            |          /     \      |                     |
|             |             /       \     |-------|        |            |         /       \     |______               |
|             |            /         \    |      \         |            |        /         \          |               |
|             |           /-----------\   |       \        |            |       /-----------\         |               |
|             |________  /             \  |        \  _____|_____       |      /             \  ______|               |
""" + vacio
    recaudar = "{:^117}".format("Todavia se necesitan recaudar $" + str(max_donacion))
    opciones = [
        "Añadir un donador",
        "Ver todas las donaciones",
        "Maxima donacion recibida",
        "Minima donacion recibida",
        "Donaciones de mayor a menor",
        "Donaciones de menor a mayor",
        "Buscar donadores por nombre",
        "Buscar donadores por monto",
        "Breve historia de CARITAS",
        "Salir del programa",
        ]
    cuerpo = cartel_caritas + vacio + "|" + recaudar + "|\n" + vacio
    i = 0
    while i < (len(opciones)-1):
        cuerpo += "|" + " "*10 + "{:<49}".format(str(i+1) + "- " + opciones[i])
        cuerpo +=  " "*10 + "{:<48}".format(str(i+2) + "- " + opciones[i+1]) +  "|\n"
        cuerpo += vacio
        i += 2
    caritas_menu = cambiar_color(1, 33) + cuadro + cuerpo + vacio + vacio + "|" + cuadro + NOCOLOR
    return caritas_menu

def historia():
    historia_texto = cambiar_color(1,34) + cuadro + vacio + "|{:^117}|".format("CARITAS ARGENTINA") + "\n" + vacio + vacio + """|     Cáritas Argentina es el organismo oficial de la Iglesia Católica que lleva adelante la pastoral caritativa,     |
|     para lograr el desarrollo integral de todo el hombre y de todos los hombres, con especial preferencia por       |
|     las personas y por las comunidades más pobres y marginadas.                                                     |""" + "\n" + vacio + vacio + """|     Esta enorme tarea es posible gracias al compromiso cotidiano de más de 32.000 voluntarios y a la colaboración   |
|     solidaria de toda la sociedad.                                                                                  |""" + "\n" + vacio + vacio + """|     A través de ellos, Cáritas lleva adelante proyectos de promoción humana y micro emprendimientos productivos     |
|     y de autoconsumo, acompaña el abordaje pastoral y comunitario de las adicciones, brinda capacitación laboral,   |
|     formación en ciudadanía y cuidados de la primera infancia, becas escolares y universitarias, talleres de        |
|     alfabetización y apoyo escolar.                                                                                 |""" + "\n" + vacio + vacio + """|     También acompaña tareas de prevención y atención de emergencias climáticas y trabaja con personas en            |
|     situación de calle, junto a otras acciones de tipo asistencial, conforme a necesidades y lugares específicos.   |""" + "\n" + vacio + "|" + cuadro + NOCOLOR

    return historia_texto
