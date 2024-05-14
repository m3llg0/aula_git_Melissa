from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen

class TelaSupervisao(BoxLayout):
    def __init__(self, **kwargs):
        super(TelaSupervisao, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [50, 20]
        self.spacing = 10

        Window.clearcolor = (0, 0, 0, 1)

        self.add_widget(Label(text='S U P E R V I S Ã O', font_size=24, bold=True, ))

        self.buttons_layout = BoxLayout(padding=[0, 10], spacing=10)
        self.inserir_button = Button(text=' I n s e r i r ', color=(0, 0, 0, 1), size=(450, 50), background_color=(100, 100, 100, 100))
        self.inserir_button.bind(on_press=self.inserir)

        self.deletar_button = Button(text=' D e l e t a r ', color=(0, 0, 0, 1), size=(450, 50), background_color=(100, 100, 100, 100))
        self.deletar_button.bind(on_press=self.deletar)

        self.buttons_layout.add_widget(self.inserir_button)
        self.buttons_layout.add_widget(self.deletar_button)
        self.add_widget(self.buttons_layout)

    def inserir(self, *args):
        self.parent.parent.current = 'Inserir'

    def deletar(self, *args):
        self.parent.parent.current = 'Deletar'

class TelaInserir():
    def __init__(self, **kwargs):
        super(TelaInserir, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [50, 20]
        self.spacing = 10

    def primeira_tela(self, *args):
        self.parent.parent.current = 'Supervisão'

class TelaDeletar():
    def __init__(self, **kwargs):
        super(TelaDeletar, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [50, 20]
        self.spacing = 10

    def primeira_tela(self, *args):
        self.parent.parent.current = 'Supervisão'
    
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        tela_supervisao = TelaSupervisao()
        tela_inserir = TelaInserir()
        tela_deletar = TelaDeletar()

        screen_supervisao = Screen(name='Supervisão')
        screen_inserir = Screen(name='Inserir')
        screen_deletar = Screen(name='Deletar')

        screen_supervisao.add_widget(tela_supervisao)
        screen_inserir.add_widget(tela_inserir)
        screen_deletar.add_widget(tela_deletar)

        sm.add_widget(screen_supervisao)
        sm.add_widget(screen_inserir)
        sm.add_widget(screen_deletar)

        return sm
    
if __name__ == '__main__':
    MyApp().run()