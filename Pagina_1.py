import flet as ft

def Pagina_principal(page: ft.Page):

    #   Configuracion Inicial de la Pagina
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




    #                                         Contenido del Rail y paneles de Navegacion de la pagina
    #   Contenedor para el contenido dinámico

    content_container = ft.Column(
        alignment=ft.MainAxisAlignment.START,
        expand=True
    )

    #Aqui se muestra el contenido de la pagina

    def update_content(index):
        # Aquí decides qué contenido mostrar basado en el ítem seleccionado
        if index == 0:
            new_content = juntador_todo
        elif index == 1:
            new_content = ft.Text("Contenido 2")
        elif index == 2:
            new_content = ft.Text("Contenido 3")
        elif index == 3:
            new_content = ft.Text("Contenido 4")
        elif index == 4:
            new_content = ft.Text("Contenido 5")
        elif index == 5:
            new_content = ft.Text("Contenido 6")
        # Limpiar el contenedor actual y añadir nuevo contenido
        content_container.controls.clear()
        content_container.controls.append(new_content)
        content_container.update()  # Asegúrate de actualizar el contenedor para mostrar los cambios

    # Crear Rail de Navegacion
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        leading=ft.FloatingActionButton(icon=ft.icons.SUPERVISED_USER_CIRCLE, text="Profesores", on_click=profesores),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.MAPS_HOME_WORK_OUTLINED, selected_icon=ft.icons.MAPS_HOME_WORK_ROUNDED, label="Inicio"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="Herramientas"
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                label="Horario",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("Preferencias"),
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.PERSON_PIN_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.PERSON_PIN_ROUNDED),
                label_content=ft.Text("Mi perfil"),
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.ASSIGNMENT_LATE_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.ASSIGNMENT_LATE_ROUNDED),
                label_content=ft.Text("Soporte"),
            ),
        ],
        on_change=lambda e: update_content(e.control.selected_index)  # Actualizar contenido al cambiar
    )
    # Añadir el NavigationRail y el contenedor de contenido a una fila
    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                content_container,  # Usar el contenedor de contenido aquí
            ],
            expand=True,
        )
    )
    # Para que muestre el contenido inicial de la Pagina
    update_content(opcion_pagina)





    #                                               PAGINA DE PROFESOREEEEEEEEEES
def pestaña_3_profesores(page: ft.Page):
    page.title = "Profesores"
    page.window_full_screen = True  # Solo disponible para el modo escritorio
    page.add(ft.ElevatedButton("Aqui estara el apartado de profesores", icon="person_rounded"))


#ft.app(target=Pagina_principal)
#ft.app(target=pestaña_3_profesores)