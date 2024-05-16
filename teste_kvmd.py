from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton, MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.appbar import MDAppbar
from kivymd.uix.screenmanager import ScreenManager

# Carregar o código KV para a interface
KV = '''
BoxLayout:
    orientation: 'vertical'
    
    MDScreen:
        md_bg_color: self.theme_cls.secondaryContainerColor

    MDTopAppBar:
        type: "small"
        size_hint_x: .8
        pos_hint: {"center_x": .5, "center_y": .5}

        MDTopAppBarLeadingButtonContainer:

            MDActionTopAppBarButton:
                icon: "menu"

        MDTopAppBarTitle:
            text: "AppBar small"
            pos_hint: {"center_x": .5}

        MDTopAppBarTrailingButtonContainer:

            MDActionTopAppBarButton:
                icon: "account-circle-outline"
        
    BoxLayout:
        orientation: 'horizontal'
        padding: "10dp"
        
        MDFlatButton:
            text: "Adicionar Usuário"
            icon: "account-plus"
            on_release: app.add_user()
        
        MDFlatButton:
            text: "Remover Usuário"
            icon: "account-remove"
            on_release: app.remove_user()
        
    Widget:
'''


class TestApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def callback_menu(self):
        print("Botão de menu pressionado")

    def callback_user(self):
        print("Botão de usuário pressionado")
    
    def add_user(self):
        print("Adicionar usuário")

    def remove_user(self):
        print("Remover usuário")


if __name__ == "__main__":
    TestApp().run()
