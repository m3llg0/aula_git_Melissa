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

        Window.clearcolor = (1, 1, 1, 0)

        self.add_widget(Label(text='S U P E R V I S Ã O', font_size=24, bold=True, color=(0, 0, 0, 1) ))

        self.buttons_layout = BoxLayout(padding=[0, 10], spacing=10)
        self.inserir_button = Button(text=' I n s e r i r ', color=(1, 1, 1, 1), size=(450, 50), size_hint=(0.3, 0.3), halign=('center'),  background_color=(0, 0, 0, 1))
        self.inserir_button.bind(on_press=self.inserir)

        self.deletar_button = Button(text=' D e l e t a r ', color=(1, 1, 1, 1), size=(450, 50), size_hint=(0.3, 0.3), background_color=(0, 0, 0, 1))
        self.deletar_button.bind(on_press=self.deletar)

        self.buttons_layout.add_widget(self.inserir_button)
        self.buttons_layout.add_widget(self.deletar_button)
        self.add_widget(self.buttons_layout)

    def inserir(self, *args):
        self.parent.parent.current = 'Inserir'

    def deletar(self, *args):
        self.parent.parent.current = 'Deletar'

class TelaInserir(BoxLayout):
    def __init__(self, **kwargs):
        super(TelaInserir, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [50, 20]
        self.spacing = 10

        Window.clearcolor = (1, 1, 1, 0)

        self.add_widget(Label(text='I N S E R I R', font_size=24, bold=True, color=(0, 0, 0, 1) ))

        self.b01_layout = BoxLayout(padding=[0, 10], spacing=10)
        self.responsavel_button = Button(text='R e s p o n s á v e l', color=(1, 1, 1, 1), size=(450, 50), size_hint=(0.3, 0.5), halign=('center'),  background_color=(0, 0, 0, 1))
        self.responsavel_button.bind(on_press=self.inserir_responsavel)
        self.aluno_button = Button(text='A l u n o', color=(1, 1, 1, 1), size=(450, 50), size_hint=(0.3, 0.5), halign=('center'),  background_color=(0, 0, 0, 1))
        #self.aluno_button.bind(on_press=self.inserir_aluno)

        self.b01_layout.add_widget(self.responsavel_button)
        self.b01_layout.add_widget(self.aluno_button)
        self.add_widget(self.b01_layout)

        self.b02_layout = BoxLayout(padding=[0, 10], spacing=10)
        self.porteiro_button = Button(text='P o r t e i r o', color=(1, 1, 1, 1), size=(450, 50), size_hint=(0.3, 0.5), halign=('center'),  background_color=(0, 0, 0, 1))
        #self.porteiro_button.bind(on_press=self.inserir_porteiro)
        self.supervisao_button = Button(text='S u p e r v i s ã o', color=(1, 1, 1, 1), size=(450, 50), size_hint=(0.3, 0.5), halign=('center'),  background_color=(0, 0, 0, 1))
        #self.supervisao_button.bind(on_press=self.inserir_supervisao)

        self.b02_layout.add_widget(self.porteiro_button)
        self.b02_layout.add_widget(self.supervisao_button)
        self.add_widget(self.b02_layout)

        
        self.button = Button(text='Voltar', color=(1, 1, 1, 1), size=(450, 50), size_hint=(0.3, 0.3), halign=('center'),  background_color=(0, 0, 1, 1))
        self.button.bind(on_press=self.primeira_tela)
        self.add_widget(self.button)

    def primeira_tela(self, *args):
        self.parent.parent.current = 'Supervisão'
    
    def inserir_responsavel(self, *args):
        self.parent.parent.current = 'Inserir Responsavel'

class InserirResponsavel(BoxLayout):
    def __init__(self, **kwargs):
        super(InserirResponsavel, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [50, 20]
        self.spacing = 10

        self.add_widget(Label(text='I N S E R I R   R E S P O N S Á V E L', font_size=24, bold=True, color=(0, 0, 0, 1) ))

        # Nome
        self.nome_layout = BoxLayout(padding=[0, 10], spacing=10)
        self.nome_text = Label(text='N o m e', font_size=24, bold=True, color=(0, 0, 0, 1) )
        self.nome_input = TextInput(text='')
        self.nome_layout.add_widget(self.nome_text)
        self.nome_layout.add_widget(self.nome_input)
        self.add_widget(self.nome_layout)

        # Telefone
        self.telefone_layout = BoxLayout(padding=[0, 10], spacing=10)
        self.telefone_text = Label(text='T e l e f o n e', font_size=24, bold=True, color=(0, 0, 0, 1) )
        self.telefone_input = TextInput(text='')
        self.telefone_layout.add_widget(self.telefone_text)
        self.telefone_layout.add_widget(self.telefone_input)
        self.add_widget(self.telefone_layout)

        # Email
        self.email_layout = BoxLayout(padding=[0, 10], spacing=10)
        self.email_text = Label(text='E m a i l', font_size=24, bold=True, color=(0, 0, 0, 1) )
        self.email_input = TextInput(text='')
        self.email_layout.add_widget(self.email_text)
        self.email_layout.add_widget(self.email_input)
        self.add_widget(self.email_layout)

        # Senha
        self.senha_layout = BoxLayout(padding=[0, 10], spacing=10)
        self.senha_text = Label(text='S e n h a', font_size=24, bold=True, color=(0, 0, 0, 1) )
        self.senha_input = TextInput(text='')
        self.senha_layout.add_widget(self.senha_text)
        self.senha_layout.add_widget(self.senha_input)
        self.add_widget(self.senha_layout)

        self.button = Button(text='Voltar', color=(1, 1, 1, 1), size=(450, 50), size_hint=(0.3, 0.3), halign=('center'),  background_color=(0, 0, 1, 1))
        self.button.bind(on_press=self.voltar_tela)
        self.add_widget(self.button)

    def voltar_tela(self, *args):
        self.parent.parent.current = 'Supervisão'



class TelaDeletar(BoxLayout):
    def __init__(self, **kwargs):
        super(TelaDeletar, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [50, 20]
        self.spacing = 10

        self.button = Button(text='Voltar')
        self.button.bind(on_press=self.segunda_tela)
        self.add_widget(self.button)

    def segunda_tela(self, *args):
        self.parent.parent.current = 'Supervisão'
    
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        tela_supervisao = TelaSupervisao()
        tela_inserir = TelaInserir()
        tela_deletar = TelaDeletar()
        tela_inserir_responsavel = InserirResponsavel()

        screen_supervisao = Screen(name='Supervisão')
        screen_inserir = Screen(name='Inserir')
        screen_deletar = Screen(name='Deletar')
        screen_inserir_responsavel = Screen(name='Inserir Responsavel')

        screen_supervisao.add_widget(tela_supervisao)
        screen_inserir.add_widget(tela_inserir)
        screen_deletar.add_widget(tela_deletar)
        screen_inserir_responsavel.add_widget(tela_inserir_responsavel)

        sm.add_widget(screen_supervisao)
        sm.add_widget(screen_inserir)
        sm.add_widget(screen_deletar)
        sm.add_widget(screen_inserir_responsavel)

        return sm
    
if __name__ == '__main__':
    MyApp().run()