import flet as ft

class RegisterView:
    def __init__(self, page: ft.Page):
        self.page = page

    def build(self):
        # 1. Título con estilo
        titulo = ft.Text(
            value="Crear Cuenta", 
            size=30, 
            color=ft.colors.BLUE_900, 
            weight=ft.FontWeight.BOLD
        )
        
        subtitulo = ft.Text(
            value="¡Únete al reto de la hidratación!",
            size=16,
            color=ft.colors.BLUE_GREY_700
        )

        # 2. Campos de entrada de datos
        input_nombre = ft.TextField(
            label="Nombre Completo",
            prefix_icon=ft.icons.PERSON_OUTLINE,
            border_color=ft.colors.BLUE_400,
            hint_text="Ej. Ana Rodríguez"
        )

        input_correo = ft.TextField(
            label="Correo Electrónico",
            prefix_icon=ft.icons.EMAIL_OUTLINED,
            border_color=ft.colors.BLUE_400,
            keyboard_type=ft.KeyboardType.EMAIL,
            hint_text="ejemplo@correo.com"
        )

        input_edad = ft.TextField(
            label="Edad",
            prefix_icon=ft.icons.CAKE_OUTLINED,
            border_color=ft.colors.BLUE_400,
            keyboard_type=ft.KeyboardType.NUMBER,
            width=150 # La edad no necesita tanto espacio
        )

        # 3. Botones
        boton_registrar = ft.ElevatedButton(
            text="Finalizar Registro",
            bgcolor=ft.colors.CYAN_700,
            color=ft.colors.WHITE,
            width=250,
            height=50,
            on_click=lambda _: print("Datos capturados: ", input_nombre.value) # Luego conectaremos al controlador
        )

        boton_regresar = ft.TextButton(
            text="¿Ya tienes cuenta? Inicia sesión",
            on_click=lambda _: self.page.go("/login")
        )

        # 4. Organización visual (Layout)
        # Usamos una columna para apilar todo verticalmente
        registro_container = ft.Column(
            controls=[
                titulo,
                subtitulo,
                ft.Container(height=10), # Espaciador
                input_nombre,
                input_correo,
                input_edad,
                ft.Container(height=20), # Espaciador
                boton_registrar,
                boton_regresar
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        )

        return registro_container