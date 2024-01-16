import flet as ft
import os
import pygame
#                                                   Importa la conexion en Mysql
from Conexion_mysql import Conexion

def Cara_1(page: ft.Page):
    #                 Antes de ejecutar elr esto del codigo vamos a verificar si un usuario ya inicio sesion

    nombre_archivo = 'Usuario.txt'
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()

            if contenido != "Invitado" and contenido != "":
                #    ¡Si ha encontrado un usuario lo saluda y lo manda al Menu!
                class Data:
                    def __init__(self) -> None:
                        self.counter = 0

                d = Data()
                page.snack_bar = ft.SnackBar(
                    ft.Text(f"Bienvenido  {contenido}", ))
                page.snack_bar.open = True
                d.counter += 1
                page.update()
                pygame.time.delay(1500)
                pygame.quit()

                opcion_entrada = "3"
                with open('opcion_inicio_sesion.txt', 'w') as archivo:
                    archivo.write(opcion_entrada)
                page.window_destroy()

    #          Si no ha encontrado un inicio de sesion ya existente, se ejecuta con normalidad y añade los objetos de la pagina



    #                                                           Boton de salir
    #   Funciones del boton salir
    def cerrar_ventana(e):
        # if e.data == "close":
        page.dialog = confirmacion
        confirmacion.open = True
        page.update()

    def aceptar_salir(e):
        opcion_entrada = "1"
        with open('opcion_inicio_sesion.txt', 'w') as archivo:
            archivo.write(opcion_entrada)

        page.window_destroy()

    def cancelar_salir(e):
        confirmacion.open = False
        page.update()


    #   Alerta de dialogo del boton salir
    confirmacion = ft.AlertDialog(
        modal=True,
        title=ft.Text("Porfavor confirme"),
        content=ft.Text("¿Estas seguro de que quieres salir de la aplicacion?"),
        actions=[
            ft.ElevatedButton("Si", on_click=aceptar_salir),
            ft.OutlinedButton("No", on_click=cancelar_salir),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    #                                                           Botones de Accion de Google
    def Continuar_con_Google(e):
        opcion_entrada = "3.5"
        with open('opcion_inicio_sesion.txt', 'w') as archivo:
            archivo.write(opcion_entrada)
        page.window_destroy()

    #                           Boton de Acceder como Invitado

    def Modo_Invitado(e):
        def cancelar_salir_INV(e):
            confirmacion.open = False
            page.update()

        def invitado_mode(e):
            usuario="Invitado"
            with open('Usuario.txt', 'w') as archivo:
                archivo.write(usuario)
            opcion_entrada = "2"
            with open('opcion_inicio_sesion.txt', 'w') as archivo:
                archivo.write(opcion_entrada)
            page.window_destroy()




        confirmacion = ft.AlertDialog(
            modal=True,
            title=ft.Text("¡¡Bienvenido!!"),
            content=ft.Text("Algunas funciones seran limitadas"),
            actions=[
                ft.ElevatedButton("Continuar", on_click=invitado_mode),
                ft.OutlinedButton("Cancelar", on_click=cancelar_salir_INV),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.dialog = confirmacion
        confirmacion.open = True
        page.update()


    #                                                               Botones con superpocisiones                                                                           "Botones con superciocisiones"
    #   Creacion de las funciones que van a usar los botones de superpocisiones.

    # Inicio de sesion (1)
    def mostrar_ranura(e):
        ranura_Inicio_de_Sesion.open = True
        ranura_Inicio_de_Sesion.update()

    def cerrar_ranura(e):
        ranura_Inicio_de_Sesion.open = False
        ranura_Inicio_de_Sesion.update()

    # Registro de usuario (2)
    def mostrar_ranura_registro(e):
        ranura_registro.open = True
        ranura_registro.update()

    def cerrar_ranura_registro(e):
        ranura_registro.open = False
        ranura_registro.update()

    # Inicio de Sesion con correo (1.1)
    def Iniciar_sesion_correo(e):
        inicio_correo.open = True
        inicio_correo.update()

    def Hacer_sesion_correo(e):
        # Vamos a declarar una variable llamada error, si esta vale 1 entonces se dejara al usuario terminar de corregir sus datos
        error = 0
        if Usuario_inic_correo.value == "" or Usuario_inic_correo.value == None:
            Usuario_inic_correo.error_text = "Coloque algun usuario valido"
            error = 1
        if Contraseña_inic_correo.value == "":
            Contraseña_inic_correo.error_text = "No es una contraseña valida"
            error = 1
        if error == 0:
            Terminar_sesion_correo(None)
        page.update()

    def Terminar_sesion_correo(e):
        # Vamos a reiniciar todas las variables asi como lso avisos
        Usuario_inic_correo.error_text = ""
        Usuario_inic_correo.value = ""

        Contraseña_inic_correo.error_text = ""
        Contraseña_inic_correo.value = ""

        inicio_correo.open = False
        inicio_correo.update()

    #               Ranura de Iniciar un Registro con correo (2.1)
    def Iniciar_Registro(e):
        registro_correo.open = True
        registro_correo.update()

    #   Pequeña animacion mientars se hace el registro
    Barra_carga= ft.AlertDialog(
        modal=True,
        title=ft.Text("Cargando datos, porfavor espere"),
        content=ft.Text("Este proceso no deberia de tardar mucho tiempo"),
        actions=[
            ft.ProgressBar(width=400, color="amber", bgcolor="#eeeeee")
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    def Hacer_Registro(e):
        # Vamos a declarar una variable llamada error, si esta vale 1 entonces se dejara al usuario terminar de corregir sus datos

        error = 5
        if usuario_reg_corr.value == "" or len(usuario_reg_corr.value)>=24:
            usuario_reg_corr.error_text = "Nombre de usuario no valido"
            error = error-1
        if correo_reg_corr.value == "":
            correo_reg_corr.error_text = "No se ha colocado un correo valido"
            error = error-1
        if contraseña_reg_corr.value == "" or len(contraseña_reg_corr.value)>=24:
            contraseña_reg_corr.error_text = "No se ha colocado una contraseña valida"
            error = error-1
        if repite_con_reg_corr.value == "":
            repite_con_reg_corr.error_text = "No se ha confirmado la contraseña"
            error = error-1
        if contraseña_reg_corr.value != repite_con_reg_corr.value:
            repite_con_reg_corr.error_text = "¡Las contraseñas son diferentes!"
            error = error-1

        if error == 5:
            Usuario_creado=usuario_reg_corr.value
            # Mostrar la barra de Carga
            page.dialog = Barra_carga
            Barra_carga.open = True
            page.update()


            opcion=1
            resultado=Conexion(opcion,usuario_reg_corr.value,contraseña_reg_corr.value,correo_reg_corr.value)


            class Data:
                def __init__(self) -> None:
                    self.counter = 0
            d = Data()
            # resultado=0 registro exitoso, resultado=1 algo ha pasado.
            if resultado==0:

                page.snack_bar = ft.SnackBar(ft.Text(f"Registro echo exitosamente, bienvenido {Usuario_creado}"))
                page.snack_bar.open = True
                d.counter += 1

                Barra_carga.open = False
                ranura_registro.open = False

                page.update()
                pygame.time.delay(2000)
                pygame.quit()

                #Cierra la pagina y manda al Menu guardando el usuario
                opcion_entrada = "3"
                with open('opcion_inicio_sesion.txt', 'w') as archivo:
                    archivo.write(opcion_entrada)
                with open('Usuario.txt', 'w') as archivo:
                    archivo.write(Usuario_creado)
                page.window_destroy()

            if resultado==1:
                page.snack_bar = ft.SnackBar(
                    ft.Text(f"Lo sentimos, algo ha fallado con el registro :("))
                page.snack_bar.open = True
                d.counter += 1
                Barra_carga.open = False
                ranura_registro.open = False

                page.update()



        page.update()

    def Terminar_Registro(e):
        # Vamos a reiniciar todas las variables asi como lso avisos
        usuario_reg_corr.error_text = ""
        usuario_reg_corr.value = ""

        correo_reg_corr.error_text = ""
        correo_reg_corr.value = ""

        contraseña_reg_corr.error_text = ""
        contraseña_reg_corr.value = ""

        repite_con_reg_corr.error_text = ""
        repite_con_reg_corr.value = ""

        registro_correo.open = False
        registro_correo.update()

        page.update()

    #   Creacion y añadido de los botones con superpocisiones

    # Boton de Inicio de Sesion (1)
    ranura_Inicio_de_Sesion = ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                    ft.Text("¿Como te gustaria iniciar sesion?"),
                    ft.ElevatedButton("Iniciar Sesion con Google", icon=ft.icons.SCREEN_SEARCH_DESKTOP_SHARP,on_click=Continuar_con_Google),
                    # Añadir comando "on_click"
                    ft.ElevatedButton("Iniciar Sesion con correo", icon=ft.icons.EMAIL_ROUNDED,
                                      on_click=Iniciar_sesion_correo),
                    ft.ElevatedButton("Regresar", icon=ft.icons.ARROW_BACK_IOS, on_click=cerrar_ranura,bgcolor=ft.colors.RED_600, color=ft.colors.WHITE),

                ],
                tight=True,
            ),
            padding=15,
        )

        ,
        on_dismiss=cerrar_ranura,
    )
    page.overlay.append(ranura_Inicio_de_Sesion)

    #   Boton para iniciar sesion con correo (1.1)
    def Inicio_Sesion(e):
        Conexion(2,Usuario_inic_correo.value,Contraseña_inic_correo.value,Usuario_inic_correo.value)
    # Juntar dos botones
    botones_accion_inic_correo = ft.Row(controls=[ft.ElevatedButton("¿Olvidaste tu contraseña?"),
                                                  ft.ElevatedButton("Volver", icon=ft.icons.ARROW_BACK_IOS,
                                                                    on_click=Terminar_sesion_correo,bgcolor=ft.colors.RED_600, color=ft.colors.WHITE),
                                                  ft.ElevatedButton("Aceptar", on_click=Inicio_Sesion)])
    Usuario_inic_correo = ft.TextField(label="Nombre de Usuario o correo electronico", autofocus=True)
    Contraseña_inic_correo = ft.TextField(label="Contraseña", password=True, can_reveal_password=True)
    inicio_correo = ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                    Usuario_inic_correo,
                    Contraseña_inic_correo,
                    botones_accion_inic_correo
                ],
                tight=True,
            ),
            padding=30,
        ),
        on_dismiss=Terminar_Registro
    )
    page.add(inicio_correo)
    # Boton de Registro de Usuario (2)
    ranura_registro = ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                    ft.Text("¿Como te gustaria Registrarte?"),
                    ft.ElevatedButton("Registrarme con Google", icon=ft.icons.SCREEN_SEARCH_DESKTOP_SHARP,on_click=Continuar_con_Google),
                    # Añadir comando "on_click"
                    ft.ElevatedButton("Usar un correo", icon=ft.icons.EMAIL_ROUNDED, on_click=Iniciar_Registro),
                    ft.ElevatedButton("Volver", icon=ft.icons.ARROW_BACK_IOS, on_click=cerrar_ranura_registro,bgcolor=ft.colors.RED_600, color=ft.colors.WHITE),

                ],
                tight=True,
            ),
            padding=15,
        )

        ,
        on_dismiss=cerrar_ranura_registro,
    )
    page.overlay.append(ranura_registro)

    # Boton para Iniciar Sesion con un correo

    # Boton para registrarse con correo (2.1)

    botones_accion_reg_correo = ft.Row(
        controls=[ft.ElevatedButton("Volver", icon=ft.icons.ARROW_BACK_IOS, on_click=Terminar_Registro,bgcolor=ft.colors.RED_600, color=ft.colors.WHITE),
                  ft.ElevatedButton("Completar Registro", on_click=Hacer_Registro), ])
    nota_reg_corr=ft.Text("Aviso: El Usuario y Contraseña deben tener menos de 20 caracteres")
    usuario_reg_corr = ft.TextField(label="Nombre de Usuario", autofocus=True)
    correo_reg_corr = ft.TextField(label="Correo Electronico", )
    contraseña_reg_corr = ft.TextField(label="Contraseña", password=True, can_reveal_password=True)
    repite_con_reg_corr = ft.TextField(label="Repite la contraseña", password=True, can_reveal_password=True)

    registro_correo = ft.BottomSheet(
        ft.Container(
            content=ft.Column(
                controls=[
                    nota_reg_corr,
                    usuario_reg_corr,
                    correo_reg_corr,
                    contraseña_reg_corr,
                    repite_con_reg_corr,
                    botones_accion_reg_correo

                ],

                tight=True,
            ),
            padding=30,
        ),
        on_dismiss=Terminar_Registro
    )
    page.add(registro_correo)



    # Con esto hemos terminado la parte de botones con superpocisiones

    #                                                              Botones Principales
    #   Crear los botones
    #   Modo Invitado



    Inicia_Sesion = ft.ElevatedButton("Iniciar Sesion", icon="person_rounded", on_click=mostrar_ranura)
    Registrar = ft.ElevatedButton("Registrarme", icon="person_add_alt", on_click=mostrar_ranura_registro)
    Cerrar_app = ft.ElevatedButton("Cerrar app", icon=ft.icons.ARROW_BACK_IOS, on_click=cerrar_ventana,bgcolor=ft.colors.RED, color=ft.colors.WHITE)
    Entrar_como_invitado =ft.ElevatedButton("Modo Invitado", icon=ft.icons.PERSON_OUTLINE_SHARP,on_click=Modo_Invitado)
    #   Hacer los botones mas grandes
    inicia_sesion_grande = ft.Container(
        content=Inicia_Sesion,
        width=200,
        height=50,
    )
    Registrar_grande = ft.Container(
        content=Registrar,
        width=200,
        height=50,
    )
    Cerrar_app_grande = ft.Container(
        content=Cerrar_app,
        width=200,
        height=50,
    )
    Entrar_como_invitado_grande=ft.Container(
        content=Entrar_como_invitado,
        width=200,
        height=50,
        on_click= Modo_Invitado
    )

    page.add(
        ft.Container(
            expand=True,
            alignment=ft.alignment.center,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
                controls=[
                    inicia_sesion_grande, Registrar_grande,Entrar_como_invitado_grande,Cerrar_app_grande
                ],
            ),
        ))