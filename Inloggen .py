from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.network.urlrequest import UrlRequest







Builder.load_string("""

<GirisEkrani>:
    GridLayout:
        rows:3
        cols:2


        Label:
            text: "Name:"
            font_size: "20sp"
            size_hint: 1,1

        TextInput:
            id: username        #Text Feld
            multiline: False
        Label:
            text: "kennwort:"
            font_size: "20sp"
        TextInput:
            id: passwd           #Text Feld verschlüsselt
            multiline: False
            password: True



        Button:
            text: "password fergot"
            size_hint: 0.5, 0.2
            on_press:test.py()
        Button:
            text: "Login"            #Weiterleiten zur nächsten Seite
            size_hint:2, 0.5
            on_press:root.login()


<GirisOnayEkrani>:

    BoxLayout:
        id: kutu
        orientation: "vertical"





        Button:
            rows:
            cols:
            text: "chats"
            on_press:
        Button:
            rows:
            cols:
            text: "Zurück"
            size_hint: 0.1, 0.1
            on_press:


<RootWidget>:
    id: kok
    GirisEkrani:
        id: giris
        name: "giris_ekrani"
    GirisOnayEkrani:
        id: onay
        name: "giris_basarili"
    GirisRedEkrani:
        id: red
        name: "giris_hatali"
""")

class GirisEkrani(Screen):
    def login(self):
        if self.ids.username.text == "chat" and\
            self.ids.passwd.text == "1234":
            print = ("Wilkommen")
            self.manager.current = "giris_basarili"

        else:
            print ("Hello")
            self.manager.current = "giris_hatali"


class GirisOnayEkrani(Screen):
    pass

class GirisRedEkrani(Screen):
    def anaEkranaDon(self):
        self.manager.current = "giris_ekrani"

class RootWidget(ScreenManager):
    pass

class GirisSistemiApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    GirisSistemiApp().run()
