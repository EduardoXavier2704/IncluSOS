from kivy.app import App
from conexao import connect
from bd import insert, insert_proximo, update, delete, query, lista, register, login
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from datetime import datetime
from usuario import Usuario
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from functools import partial
from kivy.uix.modalview import ModalView
from kivy.lang import Builder
import os
from kivy.uix.label import Label
from kivy.lang import Builder

Builder.load_string('''
<SeuWidget>:
    font_name: '/Users/aluno.sesipaulista/Desktop/IncluSOS/Oswald/Oswald-VariableFont_wght.ttf'
''')

class SeuWidget(Label):
    pass


mydb = connect()

# Obter o caminho absoluto do diretório onde o script está localizado
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construir o caminho absoluto para o arquivo KV
kv_file = os.path.join(current_dir, 'login_cadastro.kv')

# Verificar se o arquivo KV existe
if not os.path.exists(kv_file):
    print(f"Arquivo KV não encontrado: {kv_file}")
    raise FileNotFoundError(f"Arquivo KV não encontrado: {kv_file}")

# Carregar o arquivo KV
Builder.load_file(kv_file)

class TelaPrincipal(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (1, 1, 1, 1)
        self.arg1 = None  # Inicializando arg1 como None
        self.arg2 = None  # Inicializando arg2 como None

    def on_kv_post(self, base_widget):
        # Widgets são acessíveis após o arquivo KV ser carregado
        self.inicial_para_login = self.ids.inicial_para_login
        self.inicial_para_login.bind(on_release=partial(self.principal_para_login))

    def principal_para_login(self, instance):
        botao_entrar = Login()
        botao_entrar.open()
        Window.clearcolor = (0, 0, 0, 1)

    def open(self):
        self._window = ModalView(size_hint=(1, 1))
        self._window.add_widget(self)
        self._window.background_color = (0, 0, 0, 1)  # Definir o fundo do ModalView como preto
        self._window.open()


class Login(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (0, 0, 0, 0)
        self.arg1 = None  # Inicializando arg1 como None
        self.arg2 = None  # Inicializando arg2 como None
        self.invalid_login = False
        self.invalid_senha = False

    def on_kv_post(self, base_widget):
        # Widgets são acessíveis após o arquivo KV ser carregado
        self.username_input = self.ids.username_input
        self.senha_input = self.ids.senha_input

        self.cadastrar_button = self.ids.cadastrar_button
        self.cadastrar_button.bind(on_release=partial(self.check_login))
        self.login_button = self.ids.login_button
        self.login_button.bind(on_release=partial(self.create_new_window))

    def check_login(self, instance):
        nome = self.username_input.text
        senha = self.senha_input.text

        user = login(mydb, nome, senha)

        if user:
            print("Login bem-sucedido!")
            telainicial = TelaInicial()
            telainicial.open()
            self.invalid_login = False
            self.invalid_senha = False
        else:
            print("Credenciais inválidas!")
            self.invalid_login = True
            self.invalid_senha = True

    def create_new_window(self, instance):
        new_window = NewWindow()
        new_window.open()
        Window.clearcolor = (0, 0, 0, 1)  # Mudar a cor de fundo para preto

    def open(self):
        self._window = ModalView(size_hint=(1, 1))
        self._window.add_widget(self)
        self._window.background_color = (0, 0, 0, 1)  # Definir o fundo do ModalView como preto
        self._window.open()

class NewWindow(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (0, 0, 0, 1)  # Mudar a cor de fundo para preto

    def on_kv_post(self, base_widget):
        # Widgets são acessíveis após o arquivo KV ser carregado
        self.username_input = self.ids.username_input
        self.email_input = self.ids.email_input
        self.celular_input = self.ids.celular_input
        self.senha_input = self.ids.senha_input

        self.button_cadastrar = self.ids.button_cadastrar
        self.button_cadastrar.bind(on_release=partial(self.register_user))
        self.botao_login = self.ids.botao_login
        self.botao_login.bind(on_release=partial(self.botao_voltar_login))

    def botao_voltar_login(self, instance):
        voltar_login = Login()
        voltar_login.open()

    def register_user(self, instance):
        user_data = {
            'nome': self.username_input.text,
            'email': self.email_input.text,
            'celular': self.celular_input.text,
            'senha': self.senha_input.text
        }
        register(mydb, user_data['nome'], user_data['email'], user_data['celular'], user_data['senha'])


    def open(self):
        self._window = ModalView(size_hint=(1, 1))
        self._window.add_widget(self)
        self._window.background_color = (0, 0, 0, 1)  # Definir o fundo do ModalView como preto
        self._window.open()

class TelaInicial(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (0, 0, 0, 0)
        self.arg1 = None  # Inicializando arg1 como None
        self.arg2 = None  # Inicializando arg2 como None

    def on_kv_post(self, base_widget):
        # Widgets são acessíveis após o arquivo KV ser carregado

        self.botao_ocorrencia = self.ids.botao_ocorrencia
        self.botao_ocorrencia.bind(on_release=partial(self.funcao_entrar_ocorrencia))
        self.minha_denuncia = self.ids.minha_denuncia
        self.minha_denuncia.bind(on_release=partial(self.entrar_minha_ocorrencia))
        self.denuncia_outra_pessoa = self.ids.denuncia_outra_pessoa
        self.denuncia_outra_pessoa.bind(on_release=partial(self.abrir_nova_ocorrencia))

    def funcao_entrar_ocorrencia(self, instance):
        func_ocorrencia = Ocorrencia()
        func_ocorrencia.open()

    def abrir_nova_ocorrencia(self, instance):
        abrir_ocorrencia = AbrirOcorrencia()
        abrir_ocorrencia.open()

    def entrar_minha_ocorrencia(self, instance):
        minha_ocorrencia = ListaOcorrencias()
        minha_ocorrencia.open()
        Window.clearcolor = (0, 0, 0, 1)

    def open(self):
        self._window = ModalView(size_hint=(1, 1))
        self._window.add_widget(self)
        self._window.background_color = (0, 0, 0, 1)  # Definir o fundo do ModalView como preto
        self._window.open()
    
class ListaOcorrencias(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (0, 0, 0, 0)
        self.arg1 = None  
        self.arg2 = None  

    def on_kv_post(self, base_widget):
        # Widgets são acessíveis após o arquivo KV ser carregado
        self.lista_ocorrencia = self.ids.lista_ocorrencia
        self.lista_ocorrencia.bind(on_release=partial(self.abrir_lista_assalto))
        self.lista_assedio = self.ids.lista_assedio
        self.lista_assedio.bind(on_release=partial(self.abrir_lista_assedio))
        self.voltar_telainicial = self.ids.voltar_telainicial
        self.voltar_telainicial.bind(on_release=partial(self.voltar_para_telainicial))

    def abrir_lista_assedio(self, instance):
        lista_assedio = ListaDenunciaAssedio()
        lista_assedio.open()

    def abrir_lista_assalto(self, instance):
        lista_assaltos = ListaDenunciaAssalto()
        lista_assaltos.open()

    def voltar_para_telainicial(self, instance):
        telainicial_voltar = TelaInicial()
        telainicial_voltar.open()
        Window.clearcolor = (0, 0, 0, 1)

    def open(self):
        self._window = ModalView(size_hint=(1, 1))
        self._window.add_widget(self)
        self._window.background_color = (0, 0, 0, 1)  # Definir o fundo do ModalView como preto
        self._window.open()

class AbrirOcorrencia(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (0, 0, 0, 0)
        self.arg1 = None  
        self.arg2 = None  

    def on_kv_post(self, base_widget):
        # Widgets são acessíveis após o arquivo KV ser carregado
        self.tipo_ocorrencia_proximo = self.ids.tipo_ocorrencia_proximo
        self.nome_completo = self.ids.nome_completo
        self.cpf = self.ids.cpf
        self.data_nascimento = self.ids.data_nascimento
        self.email = self.ids.email
        self.voltarparatelainicial = self.ids.voltarparatelainicial
        self.voltarparatelainicial.bind(on_release=partial(self.voltar_para_tela_inicial))
        self.ocorrencia_prox = self.ids.ocorrencia_prox
        self.botao_enviar_ocorrencia = self.ids.botao_enviar_ocorrencia
        self.botao_enviar_ocorrencia.bind(on_release=partial(self.insert_ocorrencia_amigo))
        self.endereço_amigo = self.ids.endereco_amigo
        self.reference = self.ids.reference

    def insert_ocorrencia_amigo(self, instance):
        Tipo_ocorrencia_proximo = self.tipo_ocorrencia_proximo.text
        Nome_completo_proximo = self.nome_completo.text
        Cpf_proximo = self.cpf.text
        Data_nasc_proximo = self.data_nascimento.text
        Email_ou_telefone_proximo = self.email.text
        Endereco_proximo = self.endereço_amigo.text
        Local_referencia = self.reference.text
        Descricao = self.ocorrencia_prox.text

        insert_proximo(mydb, Tipo_ocorrencia_proximo, Nome_completo_proximo, Cpf_proximo, Data_nasc_proximo, Email_ou_telefone_proximo, Endereco_proximo, Local_referencia, Descricao)

    def voltar_para_tela_inicial(self, instance):
        icone_casa = TelaInicial()
        icone_casa.open()

    def open(self):
        self._window = ModalView(size_hint=(1, 1))
        self._window.add_widget(self)
        self._window.background_color = (0, 0, 0, 1)  # Definir o fundo do ModalView como preto
        self._window.open()


class Ocorrencia(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (0, 0, 0, 0)
        self.arg1 = None  # Inicializando arg1 como None
        self.arg2 = None  # Inicializando arg2 como None

    def on_kv_post(self, base_widget):
        # Widgets são acessíveis após o arquivo KV ser carregado
        self.enviar_ocorrencia_botao = self.ids.enviar_ocorrencia_botao
        self.enviar_ocorrencia_botao.bind(on_release=partial(self.insert_ocorrencia))
        self.seta_voltar = self.ids.seta_voltar
        self.seta_voltar.bind(on_release=partial(self.apertar_voltar))
        self.tipo_ocorrencia = self.ids.tipo_ocorrencia
        self.nomeseu_completo = self.ids.nomeseu_completo
        self.seucpf = self.ids.seucpf
        self.suadata_nasc = self.ids.suadata_nasc
        self.seuemail = self.ids.seuemail
        self.seuendereco = self.ids.seuendereco
        self.suareferencia = self.ids.suareferencia
        self.suadescricao = self.ids.suadescricao

    def insert_ocorrencia(self, instance):
        tipo_ocorrencia = self.tipo_ocorrencia.text
        Nome = self.nomeseu_completo.text
        Cpf = self.seucpf.text
        Data_nasc = self.suadata_nasc.text
        Email_ou_telefone = self.seuemail.text
        Endereco = self.seuendereco.text
        Lugar_referencia = self.suareferencia.text
        Descricao = self.suadescricao.text

        insert(mydb, tipo_ocorrencia, Nome, Cpf, Data_nasc, Email_ou_telefone, Endereco, Lugar_referencia, Descricao)

    def apertar_voltar(self, instance):
        voltar_casinha = TelaInicial()
        voltar_casinha.open()

    def open(self):
        self._window = ModalView(size_hint=(1, 1))
        self._window.add_widget(self)
        self._window.background_color = (0, 0, 0, 1)  # Definir o fundo do ModalView como preto
        self._window.open()

class ListaDenunciaAssalto(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (1, 1, 1, 1)
        self.arg1 = None  # Inicializando arg1 como None
        self.arg2 = None  # Inicializando arg2 como None

    def on_kv_post(self, base_widget):
        # Widgets são acessíveis após o arquivo KV ser carregado
        self.listar_assalto = self.ids.listar_assalto
        self.listar_assalto.bind(on_release=partial(self.aparecer_lista))
        self.setinha = self.ids.setinha
        self.setinha.bind(on_release=partial(self.setinha_voltar))

    def aparecer_lista(self, instance):
        mydb = connect()
        dados = query(mydb)
        self.mostrar_lista(dados)  

    def mostrar_lista(self, dados):
        self.ids.lista.clear_widgets()

        # Criar um FloatLayout para a lista
        lista_layout = FloatLayout(size_hint_y=None)
        lista_layout_height = 0

        # Adicionar cada item da lista
        for dado in dados:
            label = Label(text=str(dado), font_size= 12, font_name= 'Arial', size_hint=(None, None), size=(self.width, 60))
            label.pos_hint = {'center_x': 0.5, 'top': 1.0 - lista_layout_height}
            lista_layout.add_widget(label)
            lista_layout_height += 0.1  # Ajuste conforme necessário para o espaçamento entre os itens

        # Adicionar o FloatLayout à ScrollView
        scroll_view = ScrollView(size_hint=(1, 0.2), pos_hint={'center_x': 0.5, 'center_y': 0.5}, do_scroll_y=True)
        scroll_view.add_widget(lista_layout)

        # Adicionar a ScrollView ao FloatLayout principal
        self.add_widget(scroll_view)


    def setinha_voltar(self, instance):
        setinha = ListaOcorrencias()
        setinha.open()  

    def setinha_voltar(self, instance):
        setinha = ListaOcorrencias()
        setinha.open()

    def open(self):
        self._window = ModalView(size_hint=(1, 1))
        self._window.add_widget(self)
        self._window.background_color = (0, 0, 0, 1)  # Definir o fundo do ModalView como preto
        self._window.open()

class ListaDenunciaAssedio(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (1, 1, 1, 1)
        self.arg1 = None  # Inicializando arg1 como None
        self.arg2 = None  # Inicializando arg2 como None

    def on_kv_post(self, base_widget):
        # Widgets são acessíveis após o arquivo KV ser carregado
        self.listar_assedio = self.ids.listar_assedio
        self.listar_assedio.bind(on_release=partial(self.abrir_lista))
        self.miniseta = self.ids.miniseta
        self.miniseta.bind(on_release=partial(self.miniseta_voltar))

    def abrir_lista(self, instance):
        mydb = connect()
        dados = lista(mydb)
        self.trazer_lista(dados)

    def trazer_lista(self, dados):
        self.ids.lista.clear_widgets()

        # Criar um FloatLayout para a lista
        lista_layout = FloatLayout(size_hint_y=None)
        lista_layout_height = 0

        # Adicionar cada item da lista
        for dado in dados:
            label = Label(text=str(dado), font_size= 12, font_name= 'Arial', size_hint=(None, None), size=(self.width, 60))
            label.pos_hint = {'center_x': 0.5, 'top': 1.0 - lista_layout_height}
            lista_layout.add_widget(label)
            lista_layout_height += 0.1  # Ajuste conforme necessário para o espaçamento entre os itens

        # Adicionar o FloatLayout à ScrollView
        scroll_view = ScrollView(size_hint=(1, 0.2), pos_hint={'center_x': 0.5, 'center_y': 0.5}, do_scroll_y=True)
        scroll_view.add_widget(lista_layout)

        # Adicionar a ScrollView ao FloatLayout principal
        self.add_widget(scroll_view)


    def miniseta_voltar(self, instance):
        volte = ListaOcorrencias()
        volte.open()

    def open(self):
        self._window = ModalView(size_hint=(1, 1))
        self._window.add_widget(self)
        self._window.background_color = (0, 0, 0, 1)  # Definir o fundo do ModalView como preto
        self._window.open()

class MyApp(App):
    def build(self):
        return TelaPrincipal()
        
if __name__ == '__main__':
    MyApp().run()


mydb.close()



