from kivy.app import App
from kivy import*
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.network.urlrequest import UrlRequest
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from subprocess import check_output
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
import threading
from kivy.base import runTouchApp
from kivy.uix.spinner import Spinner




Builder.load_string("""


<Firstpage>:
    FloatLayout:
        canvas:

            Rectangle:
                source:'katze.jpg'
                size: self.size
                #pos: (0,100)

    BoxLayout:
        orientation: "vertical"

        FloatLayout:

        Button:
            text:"to register"
            size_hint: 0.5,0.5
            pos_hint:{'left_x':.10, 'right_y':.10}
            on_press:root.star()



            canvas.before:

                #Color:
                #    rgb:0.62, 0.62, 0.62, 0.62
                Rectangle:
                    pos: self.pos
                    size: self.size




            Button:
                text:"Log In"
                size_hint: 1,1
                #pos_hint:{'center_x':.5000, 'left_y':.500}
                on_press:root.start()

        Label:
            size_hint: 0.5,0.5




<Startseite>:
    GridLayout:
        rows:9
        cols:


        FloatLayout:
        Label:

            size_hint:2,2
            canvas.before:
                Color:
                    rgb:0.62, 0.62, 0.62, 0.62
                Rectangle:
                    pos: self.pos
                    size: self.size


        Label:
            text: "Username"                                                    #Username im chat
            font_size: "15sp"
            canvas.before:
                Color:
                    rgb:0.62, 0.62, 0.62, 0.62


        TextInput:
            id: username
            multiline: False



        Label:
            text: "Password"                                                    #Password ist chat(wird Verschlüsselt angezeigt)
            #font_size: "15sp"
            size_hint: 0.1,0.1


        TextInput:
            id: passwd
            multiline: False
            password: True

        Label:

            font_size: "10sp"
            size_hint: 1,1
            bcolor: 0,1,0,1

        Button:
            text: "Log In"                                                       #wird eingeloggt und zur Hauptseite weitergeleitet
            pos_hint:{'right_x':.50, 'right_y':.5}
            on_press:root.login()

            Button:
                text: "To register"
                pos_hint:{'left_x':.10, 'right_y':.5}
                #size_hint: 7,7
                on_press: root.inlog()



        Label:
            #text: "Password"
            font_size: "15sp"
            size_hint: 1,1






        Button:
            text: "Forget"                                                   #noch keine Funktion
            size_hint: 1,1
            pos_hint:{'center_x':.50, 'right_y':.5}

<Startseite1>:
    GridLayout:
        rows:9
        cols:


        FloatLayout:
        Label:

            size_hint:2,2
            canvas.before:
                Color:
                    rgb:0.62, 0.62, 0.62, 0.62
                Rectangle:
                    pos: self.pos
                    size: self.size


        Label:
            text: "Username"                                                    #Username im chat
            font_size: "15sp"
            canvas.before:
                Color:
                    rgb:0.62, 0.62, 0.62, 0.62


        TextInput:
            id: username
            multiline: False



        Label:
            text: "Password"                                                    #Password ist chat(wird Verschlüsselt angezeigt)
            #font_size: "15sp"
            size_hint: 0.1,0.1


        TextInput:
            id: passwd
            multiline: False
            password: True

        Label:

            font_size: "10sp"
            size_hint: 1,1
            bcolor: 0,1,0,1

        Button:
            text: "Log In"                                                       #wird eingeloggt und zur Hauptseite weitergeleitet
            pos_hint:{'right_x':.50, 'right_y':.5}
            on_press:root.login()

            Button:
                text: "To register"
                pos_hint:{'left_x':.10, 'right_y':.5}
                size_hint: 7,7
                on_press:root.Eine()



        Label:
            #text: "Password"
            font_size: "15sp"
            size_hint: 1,1






        Button:
            text: "vergessen"                                                   #noch keine Funktion
            size_hint: 1,1
            pos_hint:{'center_x':.50, 'right_y':.5}


<Hauptseite>:
                                                                 #nächste seite, nach der anmeldung
    PageLayout:
        rows:1
        cols:1

        Button:

        Button:






<Anmelden>:
    GridLayout:
        rows:9
        cols:


    #    Label:
    #        text:"Konto"
    #        text_size: self.size
    #        halign: 'right'
    #        valign: 'middle'


    #    Label:
    #        text:" erstellen"
    #        text_size: self.size
    #        halign:"left"
    #        valign:"middle"
    #        size_hint:1,4

        FloatLayout:
        Label:
            text:""
            bgcolor:None
            canvas.before:
                Color:
                    rgb :0.62, 0.62, 0.62, 0.62
                Rectangle:
                    pos: self.pos
                    size: self.size



        FloatLayout:
        Label:
            text:"Registration"
            size_hint:2,2
            canvas.before:
                Color:
                    rgb:0.62, 0.62, 0.62, 0.62
                Rectangle:
                    pos: self.pos
                    size: self.size




        Label:
            text:"Mobile number"
            size_hint: 0.1,0.2


        TextInput:
            id:Handy Nummer
            multiline: False



        Label:
            text: "E-mail address"                                                    #Password ist chat(wird Verschlüsselt angezeigt)
            #font_size: "10sp"
            size_hint: 0.1,0.1

        TextInput:
            id:email
            multiline: False


        Label:
            text:"Password"
            font_size: "15sp"
            size_hint: 1,1



        TextInput:
            id:passwd
            multiline:False
            password:True


        Label:
            text:"Repeat password"
            front_size:"12"

        TextInput:
            text:
            id:passwd
            multiline:False
            password:True

        Label:                                                                  #Platzsparer

        Button:
            text: "Log In"
            pos_hint:{'left_x':.50, 'left_y':.50}
            on_press:root.login()



        Label:
            text:
            id:email
            multiline:False
            size_hint:1,4

        Button:
            text:"Already registered"
            pos_hint:{'center_x':.50, 'right_y':.5}
            size_hint:0,0
            on_press:root.log()



<Einstellung>:
    FloatLayout:

        Label:

            Button:
                text:"press"
        Label:
            text:"press on"
<GirisOnayEkrani>:                                                              #nächste seite, nach der anmeldung



    BoxLayout:
        id: kutu
        orientation: "vertical"
        Button:
            text:"Menü"
            pos_hint: {'left_x':.50, 'right_y':.5}
            size_hint:0.15, 0.15
            on_press:root.GirisSistemi()

        Button:
            text:"Einstellung"
            pos_hint: {'left_x':.50, 'right_y':.5}
            size_hint:0.15, 0.15
            #on_press:GirisSistemiApp()

        Label:
            id: karsilama_yazisi
            text: "Deine Chats"
        Label:


        Button:
            text:"zurück"
            #pos_hint: {"x": .2, "y": .2}
            size_hint:0.1, 0.1
            on_press:()

<GirisRedEkrani>:
    BoxLayout:
        orientation: "vertical"



<RootWidget>:
    id: kok
    Firstpage:
        id: red
        name:""
    Startseite:
        id: onay
        name: "erste"
    Startseite1:
        id: onay
        name: "ein"
    Startseite:
        id:onay
        name: "back"
    Hauptseite:
        id: onay
        name: "Meine Chats"
    Anmelden:
        id: onay
        name: "zweite"
    Anmelden:
        id: red
        name:"regi"

    Einstellung:
        id: onay
        name: "zwei"
    GirisRedEkrani:
        id: red
        name: "giris_hatali"



""")

class Firstpage(Screen):

    def star(self):
        self.manager.current = "regi"
    def start(self):
        self.manager.current = "erste"



class Startseite(Screen):
    def login(self):
        if self.ids.username.text == "chat" and\
            self.ids.passwd.text == "chat":
            self.manager.current = "Meine Chats"

    def inlog(self):
            self.manager.current = "regi"


    def incomingData(self, req, results):
        sicaklik = data["list"][0]["main"]["temp"]-273.15


class Firstpage(Screen):
    def login(self):
        if self.ids.username.text == "chat" and\
            self.ids.passwd.text == "chat":
            self.manager.current = "Meine Chats"





    def incomingData(self, req, results):
        sicaklik = data["list"][0]["main"]["temp"]-273.15

    #class Startseite(Screen):
    #        def inlog(self):
    #            self.manager.current = "regi"



class Hauptseite(Screen):
    def back(self):
        self.manager.current = "ein"

    class Hauptseite(Screen):
        def load(self):
            self.manager.current = "zwei"

class Anmelden(Screen):
    def log(self):
        self.manager.current = "back"

class Startseite1(Screen):
    pass






class Einstellung(Screen):
    pass

class GirisRedEkrani(Screen):
    def anaEkranaDon(self):
        self.manager.current = "giris_ekrani"

class RootWidget(ScreenManager):
    pass

class GirisSistemiApp(App):
    def build(self):
        return RootWidget()

class Manny(App):
    def next(self):
        return GirisSistemiApp()




if __name__ == "__main__":
    GirisSistemiApp().run()






    #Quellen:
            #https://www.gurayyildirim.com.tr/kivy-course-10-user-login-system-with-kivy-1203.html
            #https://kivy.org/docs/guide/widgets.html
