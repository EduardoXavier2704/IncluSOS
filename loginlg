from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Color, Rectangle
from kivy.utils import get_color_from_hex
from functools import partial
from kivy.uix.modalview import ModalView

class Login(RelativeLayout):
    def __init__(self, arg1=None, arg2=None, **kwargs):
        Window.clearcolor = (1, 1, 1, 1)
        super().__init__(**kwargs)
        self.arg1 = arg1
        self.arg2 = arg2
        self.setup_ui()

    def setup_ui(self):

        
        self.add_widget(Image(source='data:image/jpeg;base64,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', allow_stretch=True, keep_ratio=False))

        
        logo_image = Image(source='data:image/jpeg;base64,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', size_hint=(None, None), size=(150, 150), pos_hint={'center_x': 0.5, 'center_y': 0.7})
        self.add_widget(logo_image)

        
        self.username_input = TextInput(hint_text="Nome de usuário", pos_hint={'center_x': 0.5, 'center_y': 0.5}, size_hint=(None, None), size=(300, 50))
        self.senha_input = TextInput(hint_text="Senha", password=True, pos_hint={'center_x': 0.5, 'center_y': 0.4}, size_hint=(None, None), size=(300, 50))
        self.add_widget(self.username_input)
        self.add_widget(self.senha_input)

        self.cadastrar_button = Button(text="Entrar", background_color=(0, 1, 0, 0.75), pos_hint={'center_x': 0.7, 'center_y': 0.3}, size_hint=(None, None), size=(350, 50))
        self.login_button = Button(text="Não possui uma conta? Cadastre-se", background_color=(0.1, 0.5, 0.8, 1), pos_hint={'center_x': 0.3, 'center_y': 0.3}, size_hint=(None, None), size=(350, 50))
        self.login_button.bind(on_release=partial(self.create_new_window, self.arg1, self.arg2))
        self.add_widget(self.cadastrar_button)
        self.add_widget(self.login_button)

        self.mensagem_label = Label(text="", pos_hint={'center_x': 0.5, 'center_y': 0.2}, size_hint=(None, None), size=(400, 50))
        self.add_widget(self.mensagem_label)

    def cadastrar_usuario(self, instance):
        self.mensagem_label.text = "Usuário cadastrado!"

    def create_new_window(self, arg1, arg2, instance):
            new_window = NewWindow(arg1, arg2)
            new_window.open()

    def open(self):
        self._window = ModalView(size_hint=(0.9, 0.9))
        self._window.add_widget(self)
        self._window.open()

class NewWindow(BoxLayout):
    def __init__(self, arg1, arg2, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [100, 100]
        self.spacing = 10
        self.arg1 = 'value1'
        self.arg2 = 'value2'
        self.orientation = 'vertical'
        self.padding = [120, 120]
        self.spacing = 10

        self.add_widget(Label(text='Tela Cadastro', font_size=30, font_name='Georgia', color=get_color_from_hex('#1E90FF')))

        self.username_input = TextInput(hint_text="Nome de usuário ...")
        self.email_input = TextInput(hint_text="Digite seu email ...")
        self.celular_input = TextInput(hint_text="Digite o número do seu celular ...")
        self.senha_input = TextInput(hint_text="Digite sua senha ...", password=True)

        self.add_widget(Label(text="Nome de usuário:", font_name='Arial', color=get_color_from_hex('#32CD32')))
        self.add_widget(self.username_input)
        self.add_widget(Label(text="Email:", font_name='Arial', color=get_color_from_hex('#32CD32')))
        self.add_widget(self.email_input)
        self.add_widget(Label(text="Celular:", font_name='Arial', color=get_color_from_hex('#32CD32')))
        self.add_widget(self.celular_input)
        self.add_widget(Label(text="Senha:", font_name='Arial', color=get_color_from_hex('#32CD32')))
        self.add_widget(self.senha_input)

        self.button_cadastrar = Button(text='Cadastrar', background_color=(0, 0, 1))
        self.button_cadastrar.bind(on_release=partial(self.entrar_interface_login, self.arg1, self.arg2))
        self.add_widget(self.button_cadastrar)
    
    def entrar_interface_login(self, arg1, arg2, instance):
              entrar_login = Login(arg1, arg2)
              entrar_login.open()


    def open(self):
        self._window = ModalView(size_hint=(0.9, 0.9))
        self._window.add_widget(self)
        self._window.open()

class MyApp(App):
    def build(self):
        return Login()

if __name__ == '__main__':
    MyApp().run()
