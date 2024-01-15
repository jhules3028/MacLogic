import flet as ft
from flet.auth.providers import GoogleOAuthProvider
from Pagina_1 import Pagina_principal

def inicio_sesion(page: ft.Page):

    class Data:
        def __init__(self) -> None:
            self.counter = 0

    d = Data()
    clientID = "957846839226-g0cj3smu1trp7sfiud9j5akjdsv69vdg.apps.googleusercontent.com"
    Secreto_cliente = "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"

    proovedor = GoogleOAuthProvider(
        client_id=clientID,
        client_secret=Secreto_cliente,
        redirect_url="http://localhost:8550/api/oauth/redirect"
    )
    def inicio_finalizado(a):
        page.snack_bar = ft.SnackBar(ft.Text(f"EL acceso se ha concluido exitosamente, porfavor cierra esta pagina "))
        page.snack_bar.open = True
        d.counter += 1
        page.update()

        #Ya que se ha iniciado sesion, puedes llamar al Menu Principal
        ft.app(target=Pagina_principal)

    def logingoogle(e):
        page.login(proovedor)

    def Invitado(e):
        usuario= "Invitado"
        with open('Usuario.txt', 'w') as archivo:
            archivo.write(usuario)
        opcion_entrada="2"
        with open('opcion_inicio_sesion.txt', 'w') as archivo:
            archivo.write(opcion_entrada)
        inicio_finalizado(0)
    # Despues de aqui podemos obtener mas informacion de acceso

    def on_login(e):
        usuario=page.auth.user['name']
        #email=page.auth.user['email']

        with open('Usuario.txt', 'w') as archivo:
            archivo.write(usuario)
        opcion_entrada="3"
        with open('opcion_inicio_sesion.txt', 'w') as archivo:
            archivo.write(opcion_entrada)


        #Mandar a llamar el menu principal

        inicio_finalizado(0)
        page.update()
        return 


    page.on_login = on_login
    print(page.on_login)

    # Función que maneja la apertura del diálogo
    confirmacion = ft.AlertDialog(
        modal=True,
        title=ft.Text("¡¡Hola Usuario!!"),
        content=ft.Text("Porfavor, seleccione su inicio de seion"),
        actions=[
            ft.ElevatedButton("Continuar con Google", on_click=logingoogle,icon=ft.icons.WEB_ROUNDED),
            ft.ElevatedButton("Entrar como Invitado", on_click=Invitado,icon=ft.icons.PERSON_2_OUTLINED)
        ],
        actions_alignment=ft.MainAxisAlignment.END,

    )

    page.dialog = confirmacion
    confirmacion.open = True
    page.update()


    #Accionar el codigo sin usar el codigo principal
#if __name__ == "__main__":
#ft.app(target=inicio_sesion, port=8550,  view=ft.AppView.WEB_BROWSER)