import flet as ft
import pygame
from flet import Container, ElevatedButton, Page, Stack, colors
import random
from math import pi

def animacion(page):

    size =15 #Tamaño de la animacion
    gap = 3 #intervalos entre los cuadros
    duration = 2000 #tiempo que dura la animacion


    #Lista de colores de los que se pintan todos los contenedores
    all_colors = [
        colors.AMBER_400,
        colors.AMBER_ACCENT_400,
        colors.BLUE_400,
        colors.BROWN_400,
        colors.CYAN_700,
        colors.DEEP_ORANGE_500,
        colors.CYAN_500,
        colors.INDIGO_600,
        colors.ORANGE_ACCENT_100,
        colors.PINK,
        colors.RED_600,
        colors.GREEN_400,
        colors.GREEN_ACCENT_200,
        colors.TEAL_ACCENT_200,
        colors.LIGHT_BLUE_500,
    ]
    # Color de las letras principales
    todos_colores_sin_repetir = all_colors
    def lista_colores_menos(color_menos):
        todos_colores_sin_repetir.remove(color_menos)

    c1 = todos_colores_sin_repetir[random.randrange(0, len(all_colors))]
    lista_colores_menos(c1)
    c4 = all_colors[random.randrange(0, len(all_colors))]
    lista_colores_menos(c4)
    c5 = all_colors[random.randrange(0, len(all_colors))]
    lista_colores_menos(c5)
    c6 = all_colors[random.randrange(0, len(all_colors))]
    lista_colores_menos(c6)
    c7 = all_colors[random.randrange(0, len(all_colors))]
    lista_colores_menos(c7)
    c8 = all_colors[random.randrange(0, len(all_colors))]
    lista_colores_menos(c8)
    c9= all_colors[random.randrange(0, len(all_colors))]
    lista_colores_menos(c9)

    #Letras a armar ordenadas por grupos (letra y color)
    parts = [
        # M
        (0, 1, c1),
        (0, 2, c1),
        (0, 3, c1),
        (0, 4, c1),
        (0, 5, c1),
        (1,2,c1),
        (2,3, c1),
        (3,2 , c1),
        (4,1 , c1),
        (4,2 , c1),
        (4, 3, c1),
        (4, 4, c1),
        (4, 5, c1),
        # A
        (6,2,c5),
        (6, 3, c5),
        (6, 4, c5),
        (6,5 , c5),
        (7,1 , c5),
        (7,3 , c5),
        (8,1 , c5),
        (8,3 , c5),
        (9,2 , c5),
        (9,3 , c5),
        (9,4 , c5),
        (9,5 , c5),

        # C
        (11,2 , c4),
        (11,3,c4),
        (11,4 , c4),
        (12, 1, c4),
        (12,5 , c4),
        (13,1 , c4),
        (13,5 , c4),
        (14,1 , c4),
        (14, 5, c4),
        # l
        (16,1 , c6),
        (16,2 , c6),
        (16,3 , c6),
        (16,4 , c6),
        (16,5 , c6),
        (17,5, c6),
        (18,5 , c6),
        # O
        (20, 2, c7),
        (20,3 , c7),
        (20,4 , c7),
        (21,1 , c7),
        (21, 5, c7),
        (22, 1, c7),
        (22, 5, c7),
        (23,2 , c7),
        (23,3 , c7),
        (23,4 , c7),
        # G
        (25,2 , c8),
        (25,3 , c8),
        (25,4 , c8),
        (26,1 , c8),
        (26,5 , c8),
        (27,1 , c8),
        (27,3 , c8),
        (27,5 , c8),
        (28,1 , c8),
        (28,3 , c8),
        (28,4 , c8),
        (28, 5, c8),

        # I
        (30,1,c9),
        (30, 2, c9),
        (30, 3, c9),
        (30, 4, c9),
        (30, 5, c9),

        #C
        (32, 2, c4),
        (32, 3, c4),
        (32, 4, c4),
        (33, 1, c4),
        (33, 5, c4),
        (34, 1, c4),
        (34, 5, c4),
        (35, 1, c4),
        (35, 5, c4),
    ]

    #Tamaño de pantalla de la animacion (camara)
    width =  36* (size + gap)
    #height = 5 * (size + gap)
    height = 10 * (size + gap)


    canvas = Stack(
        width=width,
        height=height,
        animate_scale=duration,
        animate_opacity=duration,
    )

    # spread parts randomly
    for i in range(len(parts)):
        canvas.controls.append(
            Container(
                animate=duration,
                animate_position=duration,
                animate_rotation=duration,
            )
        )

    def randomize(e):
        random.seed()
        for i in range(len(parts)):
            c = canvas.controls[i]
            part_size = random.randrange(int(size / 2), int(size * 3))
            c.left = random.randrange(0, width)
            c.top = random.randrange(0, height)
            c.bgcolor = all_colors[random.randrange(0, len(all_colors))]
            c.width = part_size
            c.height = part_size
            c.border_radius = random.randrange(0, int(size / 2))
            c.rotate = random.randrange(0, 90) * 2 * pi / 360
        canvas.scale = 5
        canvas.opacity = 0.3
        go_button.visible = True
        again_button.visible = False
        page.update()


    def assemble(e):
                #Pequeña pausa antes de que se armen las piezas
        pygame.time.delay(500)
        pygame.quit()

                #Armado de las piezas
        go_button.visible = False
        again_button.visible = False
        page.update()
        i = 0
        for left, top, bgcolor in parts:
            c = canvas.controls[i]
            c.left = left * (size + gap)
            c.top = top * (size + gap)

            c.bgcolor = bgcolor
            c.width = size
            c.height = size
            c.border_radius = 5
            c.rotate = 0
            i += 1
        canvas.scale = 1
        canvas.opacity = 1

        again_button.visible = False
        page.update()


    go_button = ElevatedButton("", autofocus=True,on_focus= assemble, visible=False)
    again_button = ElevatedButton("", on_click=randomize, visible=False)

    randomize(None)


    return ft.Container(
        expand=True,
        alignment=ft.alignment.center,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            tight=True,
            controls=[
                canvas,
                go_button,
                again_button,
            ],
        ),
    )