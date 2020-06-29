from kivy.config import Config
Config.set('graphics', 'resizable', 0)
from kivy.core.window import Window
Window.size = (1000, 600)
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from threading import *
from kivy.cache import Cache
import paramiko
import os
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
kv = '''
main:
    BoxLayout:
        orientation: 'vertical'
        padding: root.width * 0.05, root.height * .05
        spacing: '5dp'
        BoxLayout:
            size_hint: [1,.85]
        BoxLayout:
            size_hint: [1,.15]
            GridLayout:
                cols: 2
                spacing: '5dp'
                Button:
                    text: 'Play'
                    bold: True
                    on_press: root.play()
                    background_color:1,1,1,100
                Button:
                    text: 'Setting'
                    bold: True
                    on_press: root.setting()
                    background_color:0,255,0,10
                Button:
                    text: 'Log Register'
                    bold: True
                    on_press: root.logsreg()
                    background_color:0,100,100,200
                Button:
                    text: 'Event Register'
                    bold: True
                    on_press: root.eventreg()
                    background_color:255,0,100,255
                Button:
                    text: 'Close'
                    bold: True
                    on_press: root.close()
                    background_color:255,0,0,100

'''
class main(BoxLayout):
    ipAddress = None
    port = 22
    user = None
    password = None
    def play(self):
        if self.ipAddress == None or self.port == None:
            box = GridLayout(cols=1)
            box.add_widget(Label(text="Ip or Port Not Set"))
            btn = Button(text="OK")
            btn.bind(on_press=self.closePopup)
            box.add_widget(btn)
            self.popup1 = Popup(title='Error', content=box, size_hint=(.8, .3))
            self.popup1.open()
        else:
            comando="ssh "+self.user+"@"+self.ipAddress+" killall -9 python3"
            print(comando)
            os.system(comando)
            comando="ssh "+self.user+"@"+self.ipAddress+" python-reconocimiento.py --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel --showimage yes"
            print(comando)
            os.system(comando)
    def closePopup(self, btn):
        self.popup1.dismiss()
    def stop(self):
        self.ids.status.text = "Play"
        Clock.unschedule(self.recv)
    def close(self):
        #comando = "ssh " + self.user + "@" + self.ipAddress + " python-reconocimiento.py --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel --showimage no"
        #print(comando)
        #os.system(comando)
        App.get_running_app().stop()
    def setting(self):
        box = GridLayout(cols=2)
        box.add_widget(Label(text="IpAddress: ", bold=True))
        self.st = TextInput(id="serverText")
        box.add_widget(self.st)
        box.add_widget(Label(text="User: ", bold=True))
        self.usert = TextInput(id="userText")
        box.add_widget(self.usert)
        box.add_widget(Label(text="Password: ", bold=True))
        self.passw = TextInput(id="psswdText")
        box.add_widget(self.passw)
        btn = Button(text="Set", bold=True)
        btn.bind(on_press=self.settingProcess)
        box.add_widget(btn)
        self.popup = Popup(title='Settings', content=box, size_hint=(.6, .4))
        self.popup.open()
    def settingProcess(self, btn):
        try:
            self.ipAddress = self.st.text
            self.user = self.usert.text
            self.password = self.passw.text
        except:
            pass
        self.popup.dismiss()
    def eventreg(self):
        if self.ipAddress == None or self.port == None:
            box = GridLayout(cols=1)
            box.add_widget(Label(text="Ip or Port Not Set"))
            btn = Button(text="OK")
            btn.bind(on_press=self.closePopup)
            box.add_widget(btn)
            self.popup1 = Popup(title='Error', content=box, size_hint=(.8, .3))
            self.popup1.open()
        else:
            self.accesodatos()
            box = GridLayout(cols=1, spacing=10, size_hint_y=None)
            box.add_widget(Label(text=self.Strlines, bold=True))
            btn = Button(text="exit", bold=True)
            btn.bind(on_press=self.settingProcess)
            box.add_widget(btn)
            self.popup = Popup(title='Registro de eventos', content=box)
            self.popup.open()
    def logsreg(self):
        if self.ipAddress == None or self.port == None:
            box = GridLayout(cols=1)
            box.add_widget(Label(text="Ip or Port Not Set"))
            btn = Button(text="OK")
            btn.bind(on_press=self.closePopup)
            box.add_widget(btn)
            self.popup1 = Popup(title='Error', content=box, size_hint=(.8, .3))
            self.popup1.open()
        else:
            self.accesologgs()
            box = GridLayout(cols=1, spacing=10, size_hint_y=None)
            box.add_widget(Label(text=self.Strlogs, bold=True))
            btn = Button(text="exit", bold=True)
            btn.bind(on_press=self.settingProcess)
            box.add_widget(btn)
            self.popup = Popup(title='Registro de entradas', content=box)
            self.popup.open()
    def accesodatos(self):
            host = self.ipAddress
            port = self.port
            username = self.user
            password = self.password
            command = "less SessionRecognition.txt"
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, port, username, password)
            stdin, stdout, stderr = ssh.exec_command(command)
            lines = stdout.readlines()
            command = "q"
            stdin, stdout, stderr = ssh.exec_command(command)
            self.Strlines = ''.join(lines)

    def accesologgs(self):
        host = self.ipAddress
        port = self.port
        username =  self.user
        password = self.password
        command = "lastlog -t2"
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password)
        stdin, stdout, stderr = ssh.exec_command(command)
        logs = stdout.readlines()
        command = "exit"
        stdin, stdout, stderr = ssh.exec_command(command)
        self.Strlogs = ''.join(logs)
class videoStreamApp(App):
    def build(self):
        return Builder.load_string(kv)
videoStreamApp().run()
