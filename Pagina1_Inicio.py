import flet as ft
def todo_junto(page: ft.Page):
    page.window_full_screen = True  # Solo disponible para el modo escritorio
    opcion_pagina = 0
    page.title = "Pagina Principal"

    #   Accion del Boton de Profesores
    def profesores(e):
        page.window_destroy()

    #                                                   Pagina: INICIO
    #                                           Comienza el Contenido de las Paginas de los BANNERS (4)

    #                                                  BANNER 1: Avisos Normales
    page.window_full_screen = True
    page.window_width = 1920
    page.window_height = 1080

    #                                                   BANNER 3 y 4
    #                                           Aqui esta el codigo del Apartado de HORARIO
    TituloContenedor_HORARIOS = ft.ListTile(
        leading=ft.Icon(ft.icons.CALENDAR_MONTH_OUTLINED),
        title=ft.Text("Horario No Disponible  :("),
        subtitle=ft.Text("Parece ser que no te has registrado, porfavor inicia sesion para acceder a tu horario."),
    )
    Icono_horario = ft.Icon(name=ft.icons.CALENDAR_TODAY_SHARP, color="white", size=100)
    hola = ft.Container(
        content=
        ft.Column(controls=[ft.Text("Acceder al Horario", style=ft.TextThemeStyle.DISPLAY_MEDIUM), Icono_horario],
                  alignment=ft.alignment.center_right),
        margin=10,
        padding=10,
        alignment=ft.alignment.center,
        width=page.width,
        height=page.height * .6,
        border_radius=10,
        bgcolor=ft.colors.LIGHT_BLUE,
        ink=True,
        on_click=lambda e: print("He recibido una solicitud de acceso!"),
    )

    Añadir_icono = ft.Icon(name=ft.icons.EDIT_CALENDAR_SHARP, color="white", size=100)
    Texto_añadir = ft.Text("Añadir un evento ", style=ft.TextThemeStyle.DISPLAY_MEDIUM)

    Boton_añaDIR_AVISO = ft.Container(
        content=ft.Column(
            controls=[Texto_añadir, Añadir_icono],
            alignment=ft.alignment.top_center, ),
        margin=0,
        padding=0,
        alignment=ft.alignment.center,
        width=page.width,
        height=page.height * .35,
        bgcolor=ft.colors.LIGHT_GREEN_300,
        border_radius=10,
        ink=True,
        on_click=lambda e: print("Se ha querido añadir una tarea nueva"),
    )
    Contenedor_avisos_HORARIO = ft.Container(
        content=ft.Column(
            controls=[TituloContenedor_HORARIOS, hola, Boton_añaDIR_AVISO]),
        width=page.width * .65,
        height=page.height,
        border_radius=10,
        ink=True, )

    # page.add(Contenedor_avisos_HORARIO)

    #                                                              Coontenedor de Avisos
    #                                              BANNER de Avisos Urgentes, Banner 2

    def Completar_evento(e):
        print("ELiminar")

    def accion_clickear_tareas():
        # Lista de tareas con elementos deslizables
        print("Accion a realizar")

    Lista_pendientes = ft.ListView(
        controls=[
            ft.Dismissible(
                content=ft.ListTile(title=ft.Text(f"Prueba u evaluacion {i}", color=ft.colors.BLACK)),
                dismiss_direction=ft.DismissDirection.HORIZONTAL,
                background=ft.Container(bgcolor=ft.colors.BLUE, on_click=accion_clickear_tareas),
                secondary_background=ft.Container(bgcolor=ft.colors.PURPLE),
                on_dismiss=Completar_evento,
                on_resize=Completar_evento,
                dismiss_thresholds={
                    ft.DismissDirection.HORIZONTAL: 0.1,
                    ft.DismissDirection.START_TO_END: 0.1
                }
            )
            for i in range(8)
        ]
    )
    # Mostrar el nombre del contenedor
    Titulo_Lista = ft.ListTile(
        leading=ft.Icon(ft.icons.SQUARE_FOOT_OUTLINED, color=ft.colors.BLACK),
        title=ft.Text("Evaluaciones de:Estadistica I", color=ft.colors.BLACK),
        trailing=ft.PopupMenuButton(
            icon=ft.icons.MORE_VERT,
            items=[
                ft.PopupMenuItem(text="Ingles Intemedio II"),
                ft.PopupMenuItem(text="Calculo III"),
            ],
        )
    )
    Contenedor_avisos = ft.Container(
        content=ft.Column(
            controls=[Titulo_Lista, Lista_pendientes]),
        width=page.width / 2,
        height=page.height * .45,
        bgcolor=ft.colors.RED_400,
        border_radius=10,
        ink=True,
    )

    #                                       BANNER AVISOS NORMALES, BANNER 2
    Lista_pendientes = ft.ListView(
        controls=[
            ft.Dismissible(
                content=ft.ListTile(title=ft.Text(f"Nombre de Actividad {i}")),
                dismiss_direction=ft.DismissDirection.HORIZONTAL,
                background=ft.Container(bgcolor=ft.colors.GREEN, on_click=accion_clickear_tareas),
                secondary_background=ft.Container(bgcolor=ft.colors.RED),
                on_dismiss=Completar_evento,
                on_resize=Completar_evento,
                dismiss_thresholds={
                    ft.DismissDirection.HORIZONTAL: 0.1,
                    ft.DismissDirection.START_TO_END: 0.1
                }
            )
            for i in range(5)
        ]
    )

    # Mostrar el nombre del contenedor
    Titulo_Lista = ft.ListTile(
        leading=ft.Icon(ft.icons.PAGES_OUTLINED),
        title=ft.Text("Pendientes de Calculo III"),
        trailing=ft.PopupMenuButton(
            icon=ft.icons.MORE_VERT,

            items=[
                ft.PopupMenuItem(text="Ingles Intemedio II"),
                ft.PopupMenuItem(text="Estadistica I"),
            ],
        )
    )

    # Coloca Lista_pendientes y a en una Columna dentro del Container

    Contenedor_avisos_normales = ft.Container(
        content=ft.Column(
            controls=[Titulo_Lista, Lista_pendientes]),
        width=page.width / 2,
        height=page.height * .75,
        bgcolor=ft.colors.GREY_800,
        border_radius=10,
        ink=True,
    )

    juntador = ft.Container(
        content=ft.Column(
            controls=[Contenedor_avisos_normales, Contenedor_avisos]
            , alignment=ft.alignment.top_center
        )

    )
    juntador_todo = ft.Row(
        [
            ft.Container(
                content=juntador,
                alignment=ft.alignment.center,
                expand=True,
            ),
            ft.VerticalDivider(),
            ft.Container(
                content=Contenedor_avisos_HORARIO,
                alignment=ft.alignment.center,
                expand=True,
            )]
    )

    # Añade el Container a la página
    page.add(juntador_todo)

    #En total tenemos:
    #Avisos Normales: Contenedor_avisos_normales
    #Avisos Importantes:  Contenedor_avisos
    # Horario y añadir avisos: Contenedor_avisos_HORARIO




ft.app(target=todo_junto)