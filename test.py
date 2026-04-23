import flet as ft

def main(page: ft.Page):
    page.add(welcome_view.build())
    page.add(ft.Text("¡Hola Technovation! El entorno está listo."))

ft.app(target=main)