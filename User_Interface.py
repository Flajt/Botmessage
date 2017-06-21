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
            text: "Username"                                                    #Username ist chat
            font_size: "10sp"
            size_hint: 0.1,0.2
        TextInput:
            id: username
            multiline: False


        Label:
            text: "Password"                                                    #Password ist chat(wird Verschlüsselt angezeigt)
            font_size: "10sp"
            size_hint: 0.1,0.1
        TextInput:
            id: passwd
            multiline: False
            password: True

        Button:
            text: "vergessen"                                                   #noch keine Funktion
            size_hint: 0.1,1
            pos_hint:{'center_x':.50, 'right_y':.5}

        Button:
            text: "login"                                                       #wird eingeloggt und weitergeleitet
            pos_hint:{'left_x':.50, 'right_y':.5}
            on_press:root.login()

    #    Label:
    #        text:""
            #font_size: "10sp"
    #        size_hint: 0.1,0.10



<GirisOnayEkrani>:                                                              #nächste seite, nach der anmeldung

    BoxLayout:
        id: kutu
        orientation: "vertical"
        Button:
            text:"Menü"
            pos_hint: {'left_x':.50, 'right_y':.5}
            size_hint:0.15, 0.15

        Label:
            id: karsilama_yazisi
            text: "Wilkommen"
        Label:

        Button:
            text:"zurück"
            #pos_hint: {"x": .2, "y": .2}
            size_hint:0.1, 0.1
            on_press:GirisSistemiApp()



<GirisRedEkrani>:
    BoxLayout:
        orientation: "vertical"




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
            self.ids.passwd.text == "chat":
            self.manager.current = "giris_basarili"



    def incomingData(self, req, results):
        sicaklik = data["list"][0]["main"]["temp"]-273.15

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
    #Quellen:
            #https://www.gurayyildirim.com.tr/kivy-course-10-user-login-system-with-kivy-1203.html
            #https://kivy.org/docs/guide/widgets.html
