import flet as ft
import pygame
from flet import  colors
#                              Importar la animacion   y los datos restantes de esta pagina (botones para acceso)
from Primera_interfaz import animacion
from Pagina_0 import Cara_1

#                                                 Importar la autenticacion con Google
from Autenticacion_Google import inicio_sesion

#                                                       Importar el Menu
from Pagina_1 import Pagina_principal

def main(page: ft.Page):
    opcion_entrada = "1"
    with open('opcion_inicio_sesion.txt', 'w') as archivo:
        archivo.write(opcion_entrada)



    #                                                                   Icono de Usuario
    #   Creacion del Icono y colocacion en el centro de la pagina
    page.title = "Inicio de sesion"

    icon = ft.Icon(name=ft.icons.PERSON_OUTLINED, color="transparent", size=160)
    container_usuario = ft.Container(content=icon, width=page.width, height=100, alignment=ft.alignment.top_center)
    page.add(container_usuario)

    #Opciones de inicio de la app

    #1 Para celulares
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.window_width = 700
    page.window_height = 1000
    page.window_full_screen = True #Solo disponible para el modo escritorio

    page.add(animacion(page=page))

    #Hacer un tiempo en lo que acaba la animacion y despues añadir los botones
    pygame.time.delay(3200)
    pygame.quit()

    icon.color = colors.WHITE
    container_usuario.update()





    #                                        Si no se ha iniciado sesion previamente, añade los demas elementos
    # Añadir el contenido de la Cara 1

    Cara_1(page=page)


if __name__ == "__main__":
    ft.app(target=main)

#                                                 Maneras de entrar al Menu principal
with open('opcion_inicio_sesion.txt', 'r') as archivo:
    contenido = archivo.read()

    if contenido=="3.5":
        ft.app(target=inicio_sesion, port=8550, view=ft.AppView.WEB_BROWSER)

    if contenido=="2" or contenido=="3":
        ft.app(target=Pagina_principal)


