import flet as ft
import os
def todo_junto(page: ft.Page):
    page.window_full_screen = True  # Solo disponible para el modo escritorio
    opcion_pagina = 0
    page.title = "Pagina Principal"

    #   Accion del Boton de Profesores
    def profesores(e):
        page.window_destroy()

    class Data:
        def __init__(self) -> None:
            self.counter = 0

    d = Data()

    #                                                   Pagina: INICIO
    #                                           Comienza el Contenido de las Paginas de los BANNERS (4)

    #   Configuracion Inicial de la Pagina
    page.window_full_screen = True
    page.window_width = 1920
    page.window_height = 1080


    #                                             BANNER IV: AÑADIR EVENTO


    #       Funciones

    def añadir_evento(e):
        deslisable_añadir_evento.open = True
        deslisable_añadir_evento.update()
    def cancelar_evento(e):
        Nota.value = ""
        marcador_importancia.value = False
        deslisable_añadir_evento.open = False
        deslisable_añadir_evento.update()
        page.update()

    def guardar_evento(e):
        if marcador_importancia.value == True:
            with open("Notas_importantes.txt", 'a') as file:
                # Si selecccionaste una materia la pone, de lo contrario solo guarda la nota

                if materias.value == None or materias.value == "":
                    pendiente = Nota.value

                else:
                    pendiente = Nota.value + ". Materia:   " + materias.value
                file.write(pendiente + "\n")

            nombre_actividades_importantes.clear()
            actualizar_actividades_importantes(0)
            Lista_pendientes_importante.controls.clear()

            Lista_pendientes_importante.controls.extend(construir_lista_importante(nombre_actividades_importantes))
            Lista_pendientes_importante.update()

        if marcador_importancia.value == False:
            with open("Notas_normales.txt", 'a') as file:
                #Si selecccionaste una materia la pone, de lo contrario solo guarda la nota

                if materias.value== None or materias.value =="":
                    pendiente = Nota.value

                    #Lista_pendientes.controls.extend(construir_lista(pendiente))
                    Lista_pendientes.update()

                else:
                    pendiente = Nota.value + ". Materia:   " + materias.value

                file.write(pendiente + "\n")

            Lista_pendientes.controls.clear()
            nombre_actividades.clear()
            actualizar_notas_normales(0)


            Lista_pendientes.controls.extend(construir_lista(nombre_actividades))
            Lista_pendientes.update()

    def confirmar_nota_guardada(e):

        if Nota.value=="":
            materias.value = None
            marcador_importancia.value = False
            page.snack_bar = ft.SnackBar(
                ft.Text("No has anotado Nada para guardar", ))
            page.snack_bar.open = True
            d.counter += 1
            page.update()
            return 0
        #Verifica la importancia de la nota
        if marcador_importancia.value== True:
            #Checa si el archivo ya existe, de no ser asi crea uno
            if os.path.exists("Notas_importantes.txt"):
                guardar_evento(0)

            else :
                with open('Notas_importantes.txt', 'w') as file:
                    file.write('')
                    print("Arhivo creado")
                    guardar_evento(0)



        # Verifica la importancia de la nota
        if marcador_importancia.value == False:
            # Checa si el archivo ya existe, de no ser asi crea uno
            if os.path.exists("Notas_normales.txt"):
                guardar_evento(0)
            else :
                with open('Notas_normales.txt', 'w') as file:
                    file.write('')
                    print("Arhivo creado")
                    guardar_evento(0)

        page.snack_bar = ft.SnackBar(
            ft.Text(f"Se ha guardado todo el contenido", ))
        page.snack_bar.open = True
        d.counter += 1

        #Reiniciar los valores de la Nota
        materias.value= None
        Nota.value=""
        marcador_importancia.value=False



        page.update()


    marcador_importancia = ft.CupertinoSwitch(label="", value=False)

    lista_materias =["Calculo III", "Ingles Intermedio I", "POO", "ALgebra Lineal"]
    opciones_materias = [ft.dropdown.Option(text=materia) for materia in lista_materias]


    materias=ft.Dropdown(
        width=200,
        options=opciones_materias
    )
    Nota=ft.TextField(label="Nota", autofocus=True)
    deslisable_añadir_evento = ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                    ft.Text("¿Que vamos a guardar hoy?"),
                    Nota,
                    ft.Row([ft.Text("Materia:  "), materias,ft.Text("               ¿Es importante? "), marcador_importancia]),
                    ft.Row([
                    ft.ElevatedButton("Cancelar", icon=ft.icons.ARROW_BACK_IOS, bgcolor=ft.colors.RED_600,
                                      color=ft.colors.WHITE,on_click=cancelar_evento),
                    ft.ElevatedButton("Guardar Nota y hacer una nueva", icon=ft.icons.SAVE_ROUNDED,on_click=confirmar_nota_guardada)]),

                ],
                tight=True,
            ),
            padding=15,
        )

    )
    page.add(deslisable_añadir_evento)

    #               $$      BOTON AÑADIR EVENTO     $$


    boton_añadir_evento = ft.ElevatedButton(
        content=ft.Column(
            [
                ft.Text(value="Añadir un evento   +", size=50),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=5,
        ),

        style=ft.ButtonStyle(
            color={
                ft.MaterialState.HOVERED: ft.colors.WHITE,
                ft.MaterialState.DEFAULT: ft.colors.BLACK,
            },
            bgcolor={ft.MaterialState.FOCUSED: ft.colors.PINK_200, "": ft.colors.YELLOW},
            overlay_color=ft.colors.TRANSPARENT,
            elevation={"pressed": 0, "": 1},
            animation_duration=500,
            side={
                ft.MaterialState.DEFAULT: ft.BorderSide(3, ft.colors.BLUE),
                ft.MaterialState.HOVERED: ft.BorderSide(8, ft.colors.BLUE),
            },

            shape={
                ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=200),
                ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=20),
            },
        ),
        width=page.width,
        height=page.height * .3,
        on_click=añadir_evento

    )
    #                                                   Banner III

    #Funciones

    #       Ir a sitios de la escuela
    def ESCOLARES(e):
        page.launch_url("http://www.escolares.acatlan.unam.mx/")
    def DGAE(e):
        page.launch_url("https://www.dgae-siae.unam.mx/www_gate.php")
    def BECAS(e):
        page.launch_url("https://www.integra.unam.mx/")
    def BABEL(e):
        page.launch_url("https://sistemas.acatlan.unam.mx/babel/")
    def Noticias_importantes_icono(e):
        page.launch_url("http://siiuae.acatlan.unam.mx/TramitesCov/Acceso.asp")
    def Material_estudio(e):
        page.launch_url("https://drive.google.com/drive/folders/1cEzTcorHb7qncTWUmcIugJ5yKYojvj_s?usp=sharing")

    texto_botones= ft.Text("He aqui algunas paginas en las que podrian tener informacion de tu interes")
    botones=ft.Row([
    ft.FilledTonalButton(text="ESCOLARES",on_click=ESCOLARES),
    ft.FilledTonalButton(text="DGAE", on_click=DGAE),
    ft.FilledTonalButton(text="Integra", on_click=BECAS),
    ft.FilledTonalButton(text="Idiomas", on_click=BABEL)])

    #Recuadros Expandibles
    Noticias_Importantes=ft.ExpansionPanelList(
        controls=[
            ft.ExpansionPanel(
                header=ft.ListTile(title=ft.Text(f"Noticias Relevantes ")),
                # has no header and content - placeholders will be used
                bgcolor=ft.colors.PINK_400,
                expanded=True,
                content=ft.ListTile(
            title=ft.Text("Hace poco fueron publicadas las fichas de reinscripcion"),
            subtitle=ft.Text("Para acceder a la tuya da click en el icono. "),
                trailing=ft.IconButton(ft.icons.PERSON_PIN_CIRCLE_SHARP, on_click=Noticias_importantes_icono)))

        ])
    Hackatones = ft.ExpansionPanelList(
        controls=[
            ft.ExpansionPanel(
                header=ft.ListTile(title=ft.Text(f"Competencias de Programacion ")),
                # has no header and content - placeholders will be used
                bgcolor=ft.colors.BLUE_400,
                content=ft.ListTile(
            title=ft.Text("Vaya, parece ser que de momento no hay nada aun :("),
            subtitle=ft.Text("En cuanto haya informacion disponible seras avisado ")),
            )])
    Competencias_matematicas = ft.ExpansionPanelList(
        controls=[
            ft.ExpansionPanel(
                header=ft.ListTile(title=ft.Text(f"Competencias de Matematicas")),
                # has no header and content - placeholders will be used
                bgcolor=ft.colors.RED_500,
                content=ft.ListTile(
                    title=ft.Text("Vaya, parece ser que de momento no hay nada aun :("),
                    subtitle=ft.Text("En cuanto haya informacion disponible actualizaremos este apartado")),
            )])
    Deportes = ft.ExpansionPanelList(
        controls=[
            ft.ExpansionPanel(
                header=ft.ListTile(title=ft.Text("Material de Estudio ")),
                # has no header and content - placeholders will be used
                bgcolor=ft.colors.PURPLE_500,
                content=ft.ListTile(
                    title=ft.Text("Hemos recopilado una gran cantidad de apuntes de diferentes materias"),
                    subtitle=ft.Text("Para acceder al contenido da click en el icono"),
                trailing=ft.IconButton(ft.icons.COLLECTIONS_BOOKMARK, on_click=Material_estudio))

            )])

    contenido_informativo=ft.Container(
        content=ft.Column( controls=[Noticias_Importantes,Hackatones,Competencias_matematicas,Deportes,texto_botones,botones]))


    Titulo_tablon = ft.ListTile(
        leading=ft.Icon(ft.icons.MENU_BOOK_SHARP),
        title=ft.Text("Tablon de anuncios de MacLogic", size=30),
        subtitle=ft.Text("Solo contenido relevante.", size=13))






    #           Reunir toda la informacion y botones que se pondran en la derecha de la pagina

    Contenedores_derecha = ft.Container(
        content=ft.Column(
            controls=[Titulo_tablon,contenido_informativo,boton_añadir_evento]),
        width=page.width ,
        height=page.height)



    #                                              Banner II: Avisos Urgentes

    def Completar_evento(e,contenido):
        if contenido == "¡¡Soy un aviso removible!!":
            return 0
        with open('Notas_normales.txt', 'r') as file:
            pendientes = [line.strip() for line in file]

        pendientes.remove(contenido)
        with open('Notas_normales.txt', 'w') as file:
            for pendiente in pendientes:
                file.write(pendiente + "\n")
                Lista_pendientes.controls.clear()
                nombre_actividades.clear()
                actualizar_notas_normales(0)

                Lista_pendientes.controls.extend(construir_lista(nombre_actividades))
                Lista_pendientes.update()

    def Completar_evento_importante(e,contenido):
        if contenido=="¡¡Soy un aviso Importante removible!!":
            return 0
        with open('Notas_importantes.txt', 'r') as file:
            pendientes = [line.strip() for line in file]

        pendientes.remove(contenido)
        with open('Notas_importantes.txt', 'w') as file:
            for pendiente in pendientes:
                file.write(pendiente + "\n")
                nombre_actividades_importantes.clear()
                actualizar_actividades_importantes(0)
                Lista_pendientes_importante.update()

    nombre_actividades_importantes = []

    def actualizar_actividades_importantes(e):
        if os.path.exists("Notas_importantes.txt"):
            with open('Notas_importantes.txt', 'r') as file:
                for line in file:
                    if line != "":
                        nombre_actividades_importantes.append(line.strip())
        else:
            nombre_actividades_importantes.append("¡¡Soy un aviso Importante removible!!")

    actualizar_actividades_importantes(0)



    def construir_lista_importante(actividades):
        return [
            ft.Dismissible(
                content=ft.ListTile(title=ft.Text(actividad)),
                dismiss_direction=ft.DismissDirection.HORIZONTAL,
                background=ft.Container(bgcolor=ft.colors.GREEN_500),
                secondary_background=ft.Container(bgcolor=ft.colors.RED_700),
                on_dismiss=lambda e, actividad=actividad: Completar_evento_importante(e, actividad),


                dismiss_thresholds={
                    ft.DismissDirection.HORIZONTAL: 0.1,
                    ft.DismissDirection.START_TO_END: 0.1
                }
            )
            for actividad in nombre_actividades_importantes

        ]
    Lista_pendientes_importante = ft.ListView(controls=construir_lista_importante(nombre_actividades_importantes))

    # Mostrar el nombre del contenedor
    Titulo_Lista = ft.ListTile(
        leading=ft.Icon(ft.icons.DOORBELL_OUTLINED,color=ft.colors.BLACK,size=30),
        title=ft.Text("Notas Importantes ",color=ft.colors.BLACK,size=30)
    )
    Contenedor_avisos = ft.Container(
        content=ft.Column(
            controls=[Titulo_Lista, Lista_pendientes_importante]),
        width=page.width ,
        height=page.height * .45,
        border_radius=10,
        bgcolor=ft.colors.WHITE60,
        ink=True,
    )


    #                                       BANNER I: AVISOS NORMALES
    nombre_actividades = []
    def actualizar_notas_normales(e):
        if os.path.exists("Notas_normales.txt"):
            with open('Notas_normales.txt', 'r') as file:
                for line in file:
                    nombre_actividades.append(line.strip())
        else:
            nombre_actividades.append("¡¡Soy un aviso removible!!")

    actualizar_notas_normales(0)



    def construir_lista(actividades):
        return [
            ft.Dismissible(
                content=ft.ListTile(title=ft.Text(actividad)),
                dismiss_direction=ft.DismissDirection.HORIZONTAL,
                background=ft.Container(bgcolor=ft.colors.GREEN),
                secondary_background=ft.Container(bgcolor=ft.colors.RED),
                on_dismiss=lambda e, actividad=actividad: Completar_evento(e, actividad),
                dismiss_thresholds={ft.DismissDirection.HORIZONTAL: 0.1, ft.DismissDirection.START_TO_END: 0.1}
            ) for actividad in actividades
        ]
    Lista_pendientes = ft.ListView(controls=construir_lista(nombre_actividades))

    # Mostrar el nombre del contenedor
    Titulo_Lista = ft.ListTile(
        leading=ft.Icon(ft.icons.EVENT_NOTE,size=30),
        title=ft.Text("Notas o Pendites",size=30))

    # Coloca Lista_pendientes y a en una Columna dentro del Container

    Contenedor_avisos_normales = ft.Container(
        content=ft.Column(
            controls=[Titulo_Lista, Lista_pendientes]),
        width=page.width ,
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
                expand=True,
            ),
            ft.VerticalDivider(),
            ft.Container(
                content=Contenedores_derecha,
                expand=True,
            )]
    )

    # Añade el Container a la página
    page.add(juntador_todo)

    #En total tenemos:
    #Avisos Normales: Contenedor_avisos_normales
    #Avisos Importantes:  Contenedor_avisos
    # Anuncios  y añadir eventos: Contenedores_derecha

ft.app(target=todo_junto)