from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.button import MDIconButton, MDFillRoundFlatButton
from def_bd import insert_responsavel, insert_aluno, insert_porteiro, insert_supervisao, delete_responsavel, delete_aluno, delete_porteiro, delete_supervisao
from conexao_bd import connect

mydb = connect()

KV = '''
ScreenManager:
    Screen:
        name: 'home'
        BoxLayout:
            orientation: 'vertical'

            MDTopAppBar:
                title: "SUPERVISÃO"
                md_bg_color: "#38B6FF"
                specific_text_color: 1, 1, 1, 1
                left_action_items: [["menu", lambda x: app.callback_menu()]]
                right_action_items: [["account-circle-outline", lambda x: app.callback_user()]]

            FloatLayout:
                MDRectangleFlatIconButton:
                    text: "Adicionar Usuário"
                    icon: "account-plus"
                    icon_size: "24sp"
                    text_color: app.theme_cls.primary_color
                    md_bg_color: 1, 1, 1, 1
                    size_hint: None, None
                    size: "200dp", "48dp"
                    pos_hint: {"center_x": .5, "center_y": .6}
                    on_release: app.root.current = 'inserir'

                MDRectangleFlatIconButton:
                    text: "Remover Usuário"
                    icon: "account-remove"
                    icon_size: "24sp"
                    text_color: app.theme_cls.primary_color
                    md_bg_color: 1, 1, 1, 1
                    size_hint: None, None
                    size: "200dp", "48dp"
                    pos_hint: {"center_x": .5, "center_y": .4}
                    on_release: app.root.current = 'remover'
    
    Screen:
        name: 'inserir'
        BoxLayout:
            orientation: 'vertical'

            MDTopAppBar:
                title: "Adicionar usuário"
                md_bg_color: "#38B6FF"
                specific_text_color: 1, 1, 1, 1
                left_action_items: [["menu", lambda x: app.callback_menu()]]
                right_action_items: [["account-circle-outline", lambda x: app.callback_user()]]

            FloatLayout:
                MDRectangleFlatButton:
                    text: "Responsável"
                    text_color: 0, 0, 0, 1
                    line_color: "#028096"
                    size_hint: None, None
                    size: "200dp", "48dp"
                    pos_hint: {"center_x": .5, "center_y": .8}
                    on_release: app.root.current = 'inserir_responsavel'

                MDRectangleFlatButton:
                    text: "Aluno"
                    text_color: 0, 0, 0, 1
                    line_color: "#008042"
                    size_hint: None, None
                    size: "200dp", "48dp"
                    pos_hint: {"center_x": .5, "center_y": .6}
                    on_release: app.root.current = 'inserir_aluno'
                
                MDRectangleFlatButton:
                    text: "Porteiro"
                    text_color: 0, 0, 0, 1
                    line_color: "#FFB21D"
                    size_hint: None, None
                    size: "200dp", "48dp"
                    pos_hint: {"center_x": .5, "center_y": .4}
                    on_release: app.root.current = 'inserir_porteiro'
                
                MDRectangleFlatButton:
                    text: "Administrador"
                    text_color: 0, 0, 0, 1
                    line_color: "#C20000"
                    size_hint: None, None
                    size: "200dp", "48dp"
                    pos_hint: {"center_x": .5, "center_y": .2}
                    on_release: app.root.current = 'inserir_administrador'

                MDIconButton:
                    icon: "arrow-left"
                    pos_hint: {"center_x": .1, "center_y": .10}
                    on_release: app.root.current = 'home'

    Screen:
        name: 'remover'
        BoxLayout:
            orientation: 'vertical'

            MDTopAppBar:
                title: "Remover usuário"
                md_bg_color: "#38B6FF"
                specific_text_color: 1, 1, 1, 1
                left_action_items: [["menu", lambda x: app.callback_menu()]]
                right_action_items: [["account-circle-outline", lambda x: app.callback_user()]]

            FloatLayout:
                MDRectangleFlatButton:
                    text: "Responsável"
                    text_color: 0, 0, 0, 1
                    line_color: "#028096"
                    size_hint: None, None
                    size: "200dp", "48dp"
                    pos_hint: {"center_x": .5, "center_y": .8}
                    on_release: app.root.current = 'remover_resp'

                MDRectangleFlatButton:
                    text: "Aluno"
                    text_color: 0, 0, 0, 1
                    line_color: "#008042"
                    size_hint: None, None
                    size: "200dp", "48dp"
                    pos_hint: {"center_x": .5, "center_y": .6}
                
                MDRectangleFlatButton:
                    text: "Porteiro"
                    text_color: 0, 0, 0, 1
                    line_color: "#FFB21D"
                    size_hint: None, None
                    size: "200dp", "48dp"
                    pos_hint: {"center_x": .5, "center_y": .4}
                
                MDRectangleFlatButton:
                    text: "Administrador"
                    text_color: 0, 0, 0, 1
                    line_color: "#C20000"
                    size_hint: None, None
                    size: "200dp", "48dp"
                    pos_hint: {"center_x": .5, "center_y": .2}

                MDIconButton:
                    icon: "arrow-left"
                    pos_hint: {"center_x": .1, "center_y": .10}
                    on_release: app.root.current = 'home'
                    
    Screen:
        name: 'inserir_responsavel'
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_x": .1, "center_y": .9}
            on_release: app.root.current = 'home'

        MDLabel:
            text: "Cadastro do Responsável"
            halign: "center"
            pos_hint: {'center_x': 0.5, 'center_y': 0.8}
            font_style: "H5"
            theme_text_color: "Custom"
            text_color: "#028096"

        MDTextField:
            id: name_resp
            hint_text: "Nome"
            pos_hint: {'center_x': 0.5, 'center_y': 0.7}
            size_hint_x: None
            width: 300

        MDTextField:
            id: phone_resp
            hint_text: "Telefone"
            pos_hint: {'center_x': 0.5, 'center_y': 0.6}
            size_hint_x: None
            width: 300

        MDTextField:
            id: email_resp
            hint_text: "Email"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint_x: None
            width: 300

        MDTextField:
            id: password_resp
            hint_text: "Senha"
            pos_hint: {'center_x': 0.5, 'center_y': 0.4}
            size_hint_x: None
            width: 300
            password: True

        MDRectangleFlatButton:
            text: "Cadastrar"
            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
            on_release: app.register_resp()
        

    Screen:
        name: 'inserir_aluno'
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_x": .1, "center_y": .9}
            on_release: app.root.current = 'home'

        MDLabel:
            text: "Cadastro do Aluno"
            halign: "center"
            pos_hint: {'center_x': 0.5, 'center_y': 0.8}
            font_style: "H5"
            theme_text_color: "Custom"
            text_color: "#008042"

        MDTextField:
            id: name_aluno
            hint_text: "Nome"
            pos_hint: {'center_x': 0.5, 'center_y': 0.7}
            size_hint_x: None
            width: 300

        MDTextField:
            id: idade_aluno
            hint_text: "Idade"
            pos_hint: {'center_x': 0.5, 'center_y': 0.6}
            size_hint_x: None
            width: 300
        
        MDTextField:
            id: respid_aluno
            hint_text: "ID do responsável"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint_x: None
            width: 300

        MDTextField:
            id: email_aluno
            hint_text: "Email"
            pos_hint: {'center_x': 0.5, 'center_y': 0.4}
            size_hint_x: None
            width: 300

        MDTextField:
            id: password_aluno
            hint_text: "Senha"
            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
            size_hint_x: None
            width: 300
            password: True

        MDRectangleFlatButton:
            text: "Cadastrar"
            pos_hint: {'center_x': 0.5, 'center_y': 0.2}
            on_release: app.register_aluno()

        

    Screen:
        name: 'inserir_porteiro'
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_x": .1, "center_y": .9}
            on_release: app.root.current = 'home'

        MDLabel:
            text: "Cadastro do Porteiro"
            halign: "center"
            pos_hint: {'center_x': 0.5, 'center_y': 0.8}
            font_style: "H5"
            theme_text_color: "Custom"
            text_color: "#FFB21D"

        MDTextField:
            id: name_port
            hint_text: "Nome"
            pos_hint: {'center_x': 0.5, 'center_y': 0.7}
            size_hint_x: None
            width: 300
    

        MDTextField:
            id: email_port
            hint_text: "Email"
            pos_hint: {'center_x': 0.5, 'center_y': 0.6}
            size_hint_x: None
            width: 300

        MDTextField:
            id: password_port
            hint_text: "Senha"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint_x: None
            width: 300
            password: True

        MDRectangleFlatButton:
            text: "Cadastrar"
            pos_hint: {'center_x': 0.5, 'center_y': 0.4}
            on_release: app.register_porteiro()

    Screen:
        name: 'inserir_administrador'
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_x": .1, "center_y": .9}
            on_release: app.root.current = 'home'

        MDLabel:
            text: "Cadastro do Administrador"
            halign: "center"
            pos_hint: {'center_x': 0.5, 'center_y': 0.8}
            font_style: "H5"
            theme_text_color: "Custom"
            text_color: "#C20000"

        MDTextField:
            id: email_adm
            hint_text: "Email"
            pos_hint: {'center_x': 0.5, 'center_y': 0.7}
            size_hint_x: None
            width: 300

        MDTextField:
            id: password_adm
            hint_text: "Senha"
            pos_hint: {'center_x': 0.5, 'center_y': 0.6}
            size_hint_x: None
            width: 300
            password: True

        MDRectangleFlatButton:
            text: "Cadastrar"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            on_release: app.register_adm()
    
    Screen:
        name: 'remover_resp'
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_x": .1, "center_y": .9}
            on_release: app.root.current = 'home'

        MDLabel:
            text: "Remover responsável"
            halign: "center"
            pos_hint: {'center_x': 0.5, 'center_y': 0.8}
            font_style: "H5"
            theme_text_color: "Custom"
            text_color: "#028096"

        MDTextField:
            id: id_resp
            hint_text: "Id"
            pos_hint: {'center_x': 0.5, 'center_y': 0.7}
            size_hint_x: None
            width: 300

        MDRectangleFlatButton:
            text: "Remover"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            on_release: app.remove_resp()


'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def callback_menu(self):
        print("Botão de menu pressionado")

    def callback_user(self):
        print("Botão de usuário pressionado")

    def register_resp(self):
        name = self.root.ids.name_resp.text
        phone = self.root.ids.phone_resp.text
        email = self.root.ids.email_resp.text
        password = self.root.ids.password_resp.text
        cadastrando = insert_responsavel(mydb, name, phone, email, password)
    
    def register_aluno(self):
        name = self.root.ids.name_aluno.text
        idade = self.root.ids.idade_aluno.text
        responsavel_id = self.root.ids.respid_aluno.text
        email = self.root.ids.email_aluno.text
        password = self.root.ids.password_aluno.text
        sts = 0 # "0" para ausente e "1" para presente na escola
        cadastrando = insert_aluno(mydb, name, idade, responsavel_id, email, password, sts)
    
    def register_porteiro(self):
        name = self.root.ids.name_port.text
        email = self.root.ids.email_port.text
        password = self.root.ids.password_port.text
        cadastrando = insert_porteiro(mydb, name, email, password)
    
    def register_adm(self):
        email = self.root.ids.email_adm.text
        password = self.root.ids.password_adm.text
        cadastrando = insert_supervisao(mydb, email, password)
    
    def remove_resp(self):
        id = self.root.ids.id_resp.text
        removendo = delete_responsavel(mydb, id)

    
if __name__ == "__main__":
    MainApp().run()