import flet as ft

def main(page: ft.Page):
    page.title = "Mobile App"

    def send_btn(e):
        if not url_txt.value:
            url_txt.error_text = "Coloque uma URL valida!"
            page.update()
        else:
            page.clean()
            page.add(ft.Text("Link enviado"))

    url_txt = ft.TextField(label="Url")

    page.add(url_txt, ft.ElevatedButton("Enviar", on_click=send_btn))

ft.app(main)